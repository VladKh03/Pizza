# Create your models here.
from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name}'


class PizzaSize(models.Model):
    size_type = models.CharField(max_length=20)
    crust_type = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return f'Розмір піци {self.size_type}'


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    description = models.CharField(max_length=200)
    size_pizza = models.ForeignKey('PizzaSize', on_delete=models.CASCADE, related_name='size_pizza',
                                   null=True,
                                   blank=True)

    def __str__(self):
        return f'Піца {self.name}'


class Order(models.Model):
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
        return f'Замовлення {self.id}'

    def save(self, *args, **kwargs):
        price = self.pizza_order.size_pizza.price
        promo = self.promo_order.discount

        self.amount = price - promo
        return super().save(*args, **kwargs)


class Payment(models.Model):
    payment_type = models.CharField(max_length=20)
    payment_date = models.DateField()
    payment_time = models.TimeField()
    promo_payment = models.ForeignKey('Promo', on_delete=models.CASCADE, related_name='promo_payment', null=True,
                                      blank=True)

    def __str__(self):
        return f'Оплата {self.id}'


class Courier(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    delivery_count = models.IntegerField()
    experience = models.IntegerField()

    def __str__(self):
        return f'Курєр {self.id}'


class Chef(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.FloatField()
    experience = models.IntegerField()
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'Шеф {self.id}'


class Delivery(models.Model):
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    delivery_comment = models.CharField(max_length=200)
    payment_delivery = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='payment_delivery',
                                         null=True, blank=True)

    def __str__(self):
        return f'Доставка {self.id}'


class Feedback(models.Model):
    feedback_text = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MaxValueValidator(5)])
    feedback_date = models.DateField()
    feedback_time = models.TimeField()
    client_feedback = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client_feedback', null=True,
                                        blank=True)

    def __str__(self):
        return f'Відгук {self.id}'


class Promo(models.Model):
    promo_name = models.CharField(max_length=50)
    discount = models.FloatField()
    valid_term = models.IntegerField(default=1)
    promo_date = models.ForeignKey('PromoDate', on_delete=models.CASCADE, related_name='promo_date', null=True,
                                   blank=True)

    def __str__(self):
        return f'Промокод {self.id}'

    def save(self, *args, **kwargs):
        end = datetime.strptime(str(self.promo_date.end_date), "%Y-%m-%d")
        start = datetime.strptime(str(self.promo_date.start_date), "%Y-%m-%d")
        delta = end - start
        self.valid_term = max(delta.days, 1)
        return super().save(*args, **kwargs)


class PromoDate(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    discount_type = models.CharField(max_length=20)

    def __str__(self):
        return f'Номер промокоду {self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        promo_list = list(self.promo_date.all().values_list('id', flat=True))
        for promo_id in promo_list:
            order = Order.objects.filter(promo_order_id=promo_id)
            if not order.exists():
                promos = Promo.objects.filter(promo_date=self)
                duration = self.end_date - self.start_date
                promos.update(valid_term=max(duration.days, 1))
                break

@receiver(post_save, sender=PromoDate)
def update_valid_term(sender, instance, **kwargs):
    promo_list = list(Promo.objects.filter(promo_date=instance).values_list('id', flat=True))
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
