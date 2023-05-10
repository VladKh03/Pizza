# Create your models here.
from datetime import datetime

from django.core.validators import MaxValueValidator, EmailValidator, RegexValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from service.tasks import validate_past_or_today, validate_past_or_current_time


class Client(models.Model):
    first_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Ім\'я може містити тільки українські або латинські символи.'
            )
        ], verbose_name = "Імя клієнта"
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Прізвище може містити тільки українські або латинські символи.'
            )
        ], verbose_name = "Прізвище клієнта"
    )
    email = models.CharField(max_length=100,
                             validators=[EmailValidator("@")],
                             error_messages={'invalid': 'Введіть дійсну адресу електронної пошти.'},
                             verbose_name = "Email клієнта"
                             )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message='Введіть дійсний номер телефону.')],
        help_text='Формат: 380123456789',
        verbose_name = "Номер телефону клієнта"
    )
    client_order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='client_order',
                                     null=True, blank=True, verbose_name="Замовлення")
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PizzaSize(models.Model):
    SIZE_CHOICES = [
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
    ]
    size_type = models.CharField(max_length=20, choices=SIZE_CHOICES, verbose_name = "Розмір піци")
    CRUST_CHOICES = [
        ('Тонке', 'Тонке'),
        ('Пухке', 'Пухке'),
        ('Нью-йоркське', 'Нью-йоркське'),
        ('Чікагське', 'Чікагське'),
        ('Сицилійське', 'Сицилійське'),
        ('Наполеон', 'Наполеон'),
        ('Класичне', 'Класичне'),
    ]
    crust_type = models.CharField(max_length=20, choices=CRUST_CHOICES, verbose_name = "Тип тіста піци")
    price = models.FloatField(validators=[MinValueValidator(0)], verbose_name = "Ціна піци")

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
        ], verbose_name = "Назва піци"
    )
    weight = models.IntegerField(choices=WEIGHT_CHOICES, verbose_name = "Вага піци")
    description = models.CharField(max_length=200, verbose_name = "Опис піци")
    size_pizza = models.ForeignKey('PizzaSize', on_delete=models.CASCADE, related_name='size_pizza',
                                   null=True,
                                   blank=True,
                                   verbose_name = "Розмір піци")
    pizza_chef = models.ForeignKey('Chef', on_delete=models.CASCADE, related_name='pizza_chef',
                                    null=True, blank=True, verbose_name="Кухар")

    def __str__(self):
        return f'{self.name}'




class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('Готівкою', 'Готівкою'),
        ('Карткою', 'Карткою'),
    )

    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name = "Тип оплати")
    payment_date = models.DateField(validators=[validate_past_or_today], verbose_name = "Дата оплати")
    payment_time = models.TimeField(validators=[validate_past_or_current_time], verbose_name = "Час оплати")
    promo_payment = models.OneToOneField('Promo', on_delete=models.CASCADE, related_name='promo_payment', null=True,
                                      blank=True, verbose_name = "Промокод")

    def __str__(self):
        return f'Оплата №{self.id}'


class Courier(models.Model):
    first_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Ім\'я може містити тільки українські або латинські символи.'
            )
        ], verbose_name = "Імя курєра"
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Прізвище може містити тільки українські або латинські символи.'
            )
        ], verbose_name = "Прізвище курєра"
    )
    email = models.CharField(max_length=100,
                             validators=[EmailValidator("@")],
                             error_messages={'invalid': 'Введіть дійсну адресу електронної пошти.'}
                             , verbose_name="Email курєра"
                             )
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message='Введіть дійсний номер телефону.')],
        help_text='Формат: 380123456789',
        verbose_name = "Номер телефона курєра"
    )
    delivery_count = models.IntegerField(validators=[
        MinValueValidator(0, message='Кількість доставок не може бути менше 0.')
    ], verbose_name = "Кількість доставок")
    experience = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Досвід не може бути менше 0.'),
            MaxValueValidator(7, message='Досвід не може бути більше 7.')
        ], verbose_name = "Стаж роботи курєра"
    )
    delivery_courier = models.ForeignKey('Delivery', on_delete=models.CASCADE, related_name='delivery_courier',
                                       null=True, blank=True, verbose_name="Доставка")

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
        ], verbose_name = "Імя кухаря"
    )
    last_name = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                r'^[А-ЯІЇЄа-яіїєA-Za-z\s]+$',
                message='Прізвище може містити тільки українські або латинські символи.'
            )
        ], verbose_name = "Прізвище кухаря"
    )
    salary = models.FloatField(validators=[MinValueValidator(0, message='Зарплата не може бути менше 0.')], verbose_name = "Заробітня плата кухаря")
    experience = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Досвід не може бути менше 0.'),
            MaxValueValidator(7, message='Досвід не може бути більше 7.')
        ], verbose_name = "Стаж роботи кухаря"
    )
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name = "Посада кухаря")
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^\+?\d{9,15}$', message='Введіть дійсний номер телефону.')],
        help_text='Формат: 380123456789',
        verbose_name = "Номер телефону"
    )
    chef_order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='chef_order',
                                   null=True, blank=True, verbose_name="Замовлення")

    def __str__(self):
        return f'Кухар {self.first_name} {self.last_name}'


class Delivery(models.Model):
    delivery_date = models.DateField(validators=[validate_past_or_today], verbose_name = "Дата доставки")
    delivery_time = models.TimeField(validators=[validate_past_or_current_time], verbose_name = "Час доставки")
    delivery_comment = models.CharField(max_length=200, verbose_name = "Коментар до доставки")
    payment_delivery = models.OneToOneField('Payment', on_delete=models.CASCADE, related_name='payment_delivery',
                                      null=True, blank=True, verbose_name="Оплата")

    def __str__(self):
        return f'Доставка {self.id}'


class Feedback(models.Model):
    feedback_text = models.CharField(max_length=200, verbose_name = "Текст відгуку")
    rating = models.IntegerField(validators=[
        MinValueValidator(1, message='Мінімальна оцінка 1.'),
        MaxValueValidator(5, message='Максимальна оцінка 5.')], verbose_name = "Оцінка")
    feedback_date = models.DateField(validators=[validate_past_or_today], verbose_name = "Дата відгука")
    feedback_time = models.TimeField(validators=[validate_past_or_current_time], verbose_name = "Час відгука")
    client_feedback = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client_feedback', null=True,
                                        blank=True, verbose_name = "Клієнт")

    def __str__(self):
        return f'Відгук {self.id}'


class Promo(models.Model):
    promo_name = models.CharField(max_length=50, verbose_name = "Назва промокода")
    discount = models.FloatField(
        validators=[MinValueValidator(0, message='Знижка повинна бути більше або дорівнювати 0.')], verbose_name = "Знижка промокода")
    valid_term = models.IntegerField(default=1, verbose_name = "Термін дії промокода")
    promo_date = models.ForeignKey('PromoDate', on_delete=models.CASCADE, related_name='promo_date', null=True,
                                   blank=True, verbose_name = "Тип промокода")
    promo_order = models.OneToOneField('Order', on_delete=models.CASCADE, related_name='promo_order',
                                       null=True, blank=True, verbose_name="Замовлення")


    def __str__(self):
        return f'Промокод {self.promo_name}'

    def save(self, *args, **kwargs):
        end = datetime.strptime(str(self.promo_date.end_date), "%Y-%m-%d")
        start = datetime.strptime(str(self.promo_date.start_date), "%Y-%m-%d")
        delta = end - start
        self.valid_term = max(delta.days, 1)
        return super().save(*args, **kwargs)


class PromoDate(models.Model):
    start_date = models.DateField(verbose_name = "Дата початку дії")
    end_date = models.DateField(verbose_name = "Дата кінця дії")
    DISCOUNT_CHOICES = [
        ('Фіксована знижка', 'Фіксована знижка'),
        ('Сезонна знижка', 'Сезонна знижка'),
        ('Промоційна знижка', 'Промоційна знижка'),
    ]

    discount_type = models.CharField(max_length=20, choices=DISCOUNT_CHOICES, verbose_name = "Тип знижки")

    def __str__(self):
        return f'{self.id}'

    def save(self, *args, **kwargs):
        try:
            promo_list = list(self.promo_date.all())
            for i in promo_list:
                if (i.promo_order):
                    break
                else:
                    promos = Promo.objects.filter(promo_date=self)
                    duration = self.end_date - self.start_date
                    promos.update(valid_term=max(duration.days, 1))
                    super().save(*args, **kwargs)
                    break
        except:
            super().save(*args, **kwargs)


@receiver(post_save, sender=PromoDate)
def update_valid_term(sender, instance, **kwargs):
    promo_list = list(Promo.objects.filter(promo_date=instance))
    for i in promo_list:
        if(i.promo_order):
            break
        else:
            promos = Promo.objects.filter(promo_date=instance)
            for promo in promos:
                duration = instance.end_date - instance.start_date
                promo.valid_term = duration.days
                promo.save()


class Order(models.Model):
    courier_order = models.ForeignKey('Courier', on_delete=models.CASCADE, related_name='courier_order',
                                      null=True, blank=True, verbose_name = "Курєр")
    order_date = models.DateField(validators=[validate_past_or_today], verbose_name = "Дата замовлення")
    order_time = models.TimeField(validators=[validate_past_or_current_time], verbose_name = "Час замовлення")
    delivery_address = models.CharField(max_length=200, verbose_name = "Адреса замовлення")
    amount = models.FloatField(default=0, verbose_name = "Сума замовлення")


    def __str__(self):
        return f'Замовлення {self.id} {self.delivery_address}'

    def save(self, *args, **kwargs):
        try:
            res = 0
            promo = (Promo.objects.filter(promo_order=self.id).first())
            pizzas = (Pizza.objects.filter(pizza_order=self.id))
            for pizza in pizzas:
                prices = (PizzaSize.objects.filter(size_pizza=pizza.id))
                for price in prices:
                    res += price.price
            self.amount = res - promo.discount
            return super().save(*args, **kwargs)
        except:
            self.amount = 0
            return super().save(*args, **kwargs)


