# Create your models here.
from datetime import datetime

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'Клієнт {self.client_id}'


class PizzaSize(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_type = models.CharField(max_length=20)
    crust_type = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f'Розмір піци {self.size_id}'


class Pizza(models.Model):
    pizza_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    description = models.CharField(max_length=200)
    size_pizza = models.ForeignKey('PizzaSize', on_delete=models.CASCADE, related_name='size_pizza',
                                   null=True,
                                   blank=True)

    def __str__(self):
        return f'Піца {self.pizza_id}'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    client_order = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client_order',
                                     null=True, blank=True)
    courier_order = models.ForeignKey('Courier', on_delete=models.CASCADE, related_name='courier_order',
                                      null=True, blank=True)
    payment_order = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='payment_order',
                                      null=True, blank=True)
    delivery_order = models.ForeignKey('Delivery', on_delete=models.CASCADE, related_name='delivery_order',
                                       null=True, blank=True)
    feedback_order = models.ForeignKey('Feedback', on_delete=models.CASCADE, related_name='feedback_order',
                                       null=True, blank=True)
    promo_order = models.ForeignKey('Promo', on_delete=models.CASCADE, related_name='promo_order',
                                    null=True, blank=True)
    pizza_order = models.ForeignKey('Pizza', on_delete=models.CASCADE, related_name='pizza_order',
                                    null=True, blank=True)
    chef_order = models.ForeignKey('Chef', on_delete=models.CASCADE, related_name='chef_order',
                                   null=True, blank=True)
    order_date = models.DateField()
    order_time = models.TimeField()
    delivery_address = models.CharField(max_length=200)
    amount = models.FloatField(default=0)

    def __str__(self):
        return f'Замовлення {self.order_id}'

    def save(self, *args, **kwargs):
        price = self.pizza_order.size_pizza.price
        promo = self.promo_order.discount

        self.amount = price - promo
        return super().save(*args, **kwargs)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_type = models.CharField(max_length=20)
    payment_date = models.DateField()
    payment_time = models.TimeField()
    promo_payment = models.ForeignKey('Promo', on_delete=models.CASCADE, related_name='promo_payment', null=True,
                                      blank=True)

    def __str__(self):
        return f'Оплата {self.payment_id}'


class Courier(models.Model):
    courier_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    delivery_count = models.IntegerField()
    experience = models.IntegerField()

    def __str__(self):
        return f'Курєр {self.courier_id}'


class Chef(models.Model):
    chef_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.FloatField()
    experience = models.IntegerField()
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'Шеф {self.chef_id}'


class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    delivery_comment = models.CharField(max_length=200)
    payment_delivery = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='payment_delivery',
                                         null=True, blank=True)

    def __str__(self):
        return f'Доставка {self.delivery_id}'


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback_text = models.CharField(max_length=200)
    rating = models.IntegerField()
    feedback_date = models.DateField()
    feedback_time = models.TimeField()
    client_feedback = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client_feedback', null=True,
                                        blank=True)

    def __str__(self):
        return f'Відгук {self.feedback_id}'


class Promo(models.Model):
    promo_id = models.AutoField(primary_key=True)
    promo_name = models.CharField(max_length=50)
    discount = models.FloatField()
    valid_term = models.IntegerField(default=1)
    promo_date = models.ForeignKey('PromoDate', on_delete=models.CASCADE, related_name='promo_date', null=True,
                                   blank=True)

    def __str__(self):
        return f'Промокод {self.promo_id}'

    def save(self, *args, **kwargs):
        end = datetime.strptime(str(self.promo_date.end_date), "%Y-%m-%d")
        start = datetime.strptime(str(self.promo_date.start_date), "%Y-%m-%d")
        delta = end - start
        self.valid_term = delta.days
        return super().save(*args, **kwargs)


class PromoDate(models.Model):
    promodate_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    discount_type = models.CharField(max_length=20)

    def __str__(self):
        return f'Номер промокоду {self.promodate_id}'

    def save(self, *args, **kwargs):
        promo_list = list(self.promo_date.all().values_list('promo_id', flat=True))
        for promo_id in promo_list:
            order = (Order.objects.filter(promo_order=promo_id))
            if order.first():
                print("pos")
            else:
                return super().save(*args, **kwargs)


@receiver(post_save, sender=PromoDate)
def update_valid_term(sender, instance, **kwargs):
    promo_list = list(Promo.objects.filter(promo_date=instance).values_list('promo_id', flat=True))
    for promo_id in promo_list:
        order = (Order.objects.filter(promo_order=promo_id))
        if order.first():
            pass
        else:
            promos = Promo.objects.filter(promo_date=instance)
            for promo in promos:
                duration = instance.end_date - instance.start_date
                promo.valid_term = duration.days
                promo.save()
