# Create your models here.
from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, EmailValidator, RegexValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from service.tasks import validate_past_or_today, validate_past_or_current_time


class Client(models.Model):
    first_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Ім\'я може містити тільки українські або латинські символи.'
            )
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Прізвище може містити тільки українські або латинські символи.'
            )
        ]
    )
    email = models.CharField(max_length=100,
                             validators=[EmailValidator("@")],
                             error_messages={'invalid': 'Введіть дійсну адресу електронної пошти.'}
                             )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message='Введіть дійсний номер телефону.')],
        help_text='Формат: 380123456789',
    )

    def __str__(self):
        return f'Клієнт {self.first_name} {self.last_name}'


class PizzaSize(models.Model):
    SIZE_CHOICES = [
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
    ]
    size_type = models.CharField(max_length=20, choices=SIZE_CHOICES)
    CRUST_CHOICES = [
        ('Тонке', 'Тонке'),
        ('Пухке', 'Пухке'),
        ('Нью-йоркське', 'Нью-йоркське'),
        ('Чікагське', 'Чікагське'),
        ('Сицилійське', 'Сицилійське'),
        ('Наполеон', 'Наполеон'),
        ('Класичне', 'Класичне'),
    ]
    crust_type = models.CharField(max_length=20, choices=CRUST_CHOICES)
    price = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'Розмір піци {self.size_type}'


class Pizza(models.Model):
    WEIGHT_CHOICES = [
        (400, '400'),
        (500, '500'),
        (600, '600'),
        (800, '800'),
    ]
    name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Назва піци може містити тільки українські або латинські символи та пробіли.'
            )
        ]
    )
    weight = models.IntegerField(choices=WEIGHT_CHOICES)
    description = models.CharField(max_length=200)
    size_pizza = models.ForeignKey('PizzaSize', on_delete=models.CASCADE, related_name='size_pizza',
                                   null=True,
                                   blank=True)

    def __str__(self):
        return f'Піца {self.name}'




class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('Готівкою', 'Готівкою'),
        ('Карткою', 'Карткою'),
    )

    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    payment_date = models.DateField(validators=[validate_past_or_today])
    payment_time = models.TimeField(validators=[validate_past_or_current_time])
    promo_payment = models.ForeignKey('Promo', on_delete=models.CASCADE, related_name='promo_payment', null=True,
                                      blank=True)

    def __str__(self):
        return f'Оплата {self.payment_type}'


class Courier(models.Model):
    first_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Ім\'я може містити тільки українські або латинські символи.'
            )
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Прізвище може містити тільки українські або латинські символи.'
            )
        ]
    )
    email = models.CharField(max_length=100,
                             validators=[EmailValidator("@")],
                             error_messages={'invalid': 'Введіть дійсну адресу електронної пошти.'}
                             )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message='Введіть дійсний номер телефону.')],
        help_text='Формат: 380123456789',
    )
    delivery_count = models.IntegerField(validators=[
        MinValueValidator(0, message='Кількість доставок не може бути менше 0.')
    ])
    experience = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Досвід не може бути менше 0.'),
            MaxValueValidator(7, message='Досвід не може бути більше 7.')
        ]
    )

    def __str__(self):
        return f'Курєр {self.first_name} {self.last_name}'


class Chef(models.Model):
    POSITION_CHOICES = [
        ('Шеф-кухар', 'Шеф-кухар'),
        ('Другий кухар', 'Другий кухар'),
        ('Третій кухар', 'Третій кухар'),
        ('Помічник кухаря', 'Помічник кухаря'),
        ('Мастер-кухар', 'Мастер-кухар'),
    ]

    first_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Ім\'я може містити тільки українські або латинські символи.'
            )
        ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Прізвище може містити тільки українські або латинські символи.'
            )
        ]
    )
    salary = models.FloatField(validators=[MinValueValidator(0, message='Зарплата не може бути менше 0.')])
    experience = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Досвід не може бути менше 0.'),
            MaxValueValidator(7, message='Досвід не може бути більше 7.')
        ]
    )
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message='Введіть дійсний номер телефону.')],
        help_text='Формат: 380123456789',
    )

    def __str__(self):
        return f'Шеф {self.first_name} {self.last_name}'


class Delivery(models.Model):
    delivery_date = models.DateField(validators=[validate_past_or_today])
    delivery_time = models.TimeField(validators=[validate_past_or_current_time])
    delivery_comment = models.CharField(max_length=200)
    payment_delivery = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='payment_delivery',
                                         null=True, blank=True)

    def __str__(self):
        return f'Доставка {self.id}'


class Feedback(models.Model):
    feedback_text = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[
        MinValueValidator(1, message='Мінімальна оцінка 1.'),
        MaxValueValidator(5, message='Максимальна оцінка 5.')])
    feedback_date = models.DateField(validators=[validate_past_or_today])
    feedback_time = models.TimeField(validators=[validate_past_or_current_time])
    client_feedback = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client_feedback', null=True,
                                        blank=True)

    def __str__(self):
        return f'Відгук {self.id}'


class Promo(models.Model):
    promo_name = models.CharField(max_length=50)
    discount = models.FloatField(
        validators=[MinValueValidator(0, message='Знижка повинна бути більше або дорівнювати 0.')])
    valid_term = models.IntegerField(default=1)
    promo_date = models.ForeignKey('PromoDate', on_delete=models.CASCADE, related_name='promo_date', null=True,
                                   blank=True)

    def __str__(self):
        return f'Промокод {self.promo_name}'

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
        try:
            promo_list = list(self.promo_date.all().values_list('id', flat=True))
            if len(promo_list) == 0:
                super().save(*args, **kwargs)
            for promo_id in promo_list:
                order = Order.objects.filter(promo_order_id=promo_id)
                if order.exists():
                    break
                else:
                    promos = Promo.objects.filter(promo_date=self)
                    duration = self.end_date - self.start_date
                    promos.update(valid_term=max(duration.days, 1))
                    super().save(*args, **kwargs)
                    break
        except:
            print("pop")
            super().save(*args, **kwargs)


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


class Order(models.Model):

    client_order = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client_order',
                                     null=True, blank=True, verbose_name = "Клієнт")
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
    order_date = models.DateField(validators=[validate_past_or_today])
    order_time = models.TimeField(validators=[validate_past_or_current_time])
    delivery_address = models.CharField(max_length=200)
    amount = models.FloatField(default=0)


    def __str__(self):
        return f'Замовлення {self.delivery_address}'

    def save(self, *args, **kwargs):
        price = self.pizza_order.size_pizza.price
        promo = self.promo_order.discount

        self.amount = price - promo
        return super().save(*args, **kwargs)


