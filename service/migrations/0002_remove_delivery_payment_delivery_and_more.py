# Generated by Django 4.2 on 2023-05-01 11:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import service.tasks


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='payment_delivery',
        ),
        migrations.AlterField(
            model_name='chef',
            name='experience',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Досвід не може бути менше 0.'), django.core.validators.MaxValueValidator(7, message='Досвід не може бути більше 7.')]),
        ),
        migrations.AlterField(
            model_name='chef',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[А-ЯІЇЄа-яіїєA-Za-z\\s]+$', message="Ім'я може містити тільки українські або латинські символи.")]),
        ),
        migrations.AlterField(
            model_name='chef',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[А-ЯІЇЄа-яіїєA-Za-z\\s]+$', message='Прізвище може містити тільки українські або латинські символи.')]),
        ),
        migrations.AlterField(
            model_name='chef',
            name='phone_number',
            field=models.CharField(help_text='Формат: 380123456789', max_length=20, validators=[django.core.validators.RegexValidator('^\\+?\\d{9,15}$', message='Введіть дійсний номер телефону.')]),
        ),
        migrations.AlterField(
            model_name='chef',
            name='position',
            field=models.CharField(choices=[('Шеф-кухар', 'Шеф-кухар'), ('Другий кухар', 'Другий кухар'), ('Третій кухар', 'Третій кухар'), ('Помічник кухаря', 'Помічник кухаря'), ('Мастер-кухар', 'Мастер-кухар')], max_length=50),
        ),
        migrations.AlterField(
            model_name='chef',
            name='salary',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0, message='Зарплата не може бути менше 0.')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(error_messages={'invalid': 'Введіть дійсну адресу електронної пошти.'}, max_length=100, validators=[django.core.validators.EmailValidator('@')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[А-ЯІЇЄа-яіїєA-Za-z\\s]+$', message="Ім'я може містити тільки українські або латинські символи.")]),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[А-ЯІЇЄа-яіїєA-Za-z\\s]+$', message='Прізвище може містити тільки українські або латинські символи.')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(help_text='Формат: 380123456789', max_length=20, validators=[django.core.validators.RegexValidator('^\\+?\\d{9,15}$', message='Введіть дійсний номер телефону.')]),
        ),
        migrations.AlterField(
            model_name='courier',
            name='delivery_count',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Кількість доставок не може бути менше 0.')]),
        ),
        migrations.AlterField(
            model_name='courier',
            name='email',
            field=models.CharField(error_messages={'invalid': 'Введіть дійсну адресу електронної пошти.'}, max_length=100, validators=[django.core.validators.EmailValidator('@')]),
        ),
        migrations.AlterField(
            model_name='courier',
            name='experience',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Досвід не може бути менше 0.'), django.core.validators.MaxValueValidator(7, message='Досвід не може бути більше 7.')]),
        ),
        migrations.AlterField(
            model_name='courier',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[А-ЯІЇЄа-яіїєA-Za-z\\s]+$', message="Ім'я може містити тільки українські або латинські символи.")]),
        ),
        migrations.AlterField(
            model_name='courier',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[А-ЯІЇЄа-яіїєA-Za-z\\s]+$', message='Прізвище може містити тільки українські або латинські символи.')]),
        ),
        migrations.AlterField(
            model_name='courier',
            name='phone_number',
            field=models.CharField(help_text='Формат: 380123456789', max_length=20, validators=[django.core.validators.RegexValidator('^\\+?\\d{9,15}$', message='Введіть дійсний номер телефону.')]),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateField(validators=[service.tasks.validate_past_or_today]),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_time',
            field=models.TimeField(validators=[service.tasks.validate_past_or_current_time]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_date',
            field=models.DateField(validators=[service.tasks.validate_past_or_today]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_time',
            field=models.TimeField(validators=[service.tasks.validate_past_or_current_time]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Мінімальна оцінка 1.'), django.core.validators.MaxValueValidator(5, message='Максимальна оцінка 5.')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_order', to='service.client', verbose_name='Клієнт'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(validators=[service.tasks.validate_past_or_today]),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.TimeField(validators=[service.tasks.validate_past_or_current_time]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(validators=[service.tasks.validate_past_or_today]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_time',
            field=models.TimeField(validators=[service.tasks.validate_past_or_current_time]),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('Готівкою', 'Готівкою'), ('Карткою', 'Карткою')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[А-ЯІЇЄа-яіїєA-Za-z\\s]+$', message='Назва піци може містити тільки українські або латинські символи та пробіли.')]),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='weight',
            field=models.IntegerField(choices=[(400, '400'), (500, '500'), (600, '600'), (800, '800')]),
        ),
        migrations.AlterField(
            model_name='pizzasize',
            name='crust_type',
            field=models.CharField(choices=[('Тонке', 'Тонке'), ('Пухке', 'Пухке'), ('Нью-йоркське', 'Нью-йоркське'), ('Чікагське', 'Чікагське'), ('Сицилійське', 'Сицилійське'), ('Наполеон', 'Наполеон'), ('Класичне', 'Класичне')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pizzasize',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='pizzasize',
            name='size_type',
            field=models.CharField(choices=[('25', '25'), ('30', '30'), ('35', '35'), ('40', '40')], max_length=20),
        ),
        migrations.AlterField(
            model_name='promo',
            name='discount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0, message='Знижка повинна бути більше або дорівнювати 0.')]),
        ),
        migrations.AlterField(
            model_name='promodate',
            name='discount_type',
            field=models.CharField(choices=[('Фіксована знижка', 'Фіксована знижка'), ('Сезонна знижка', 'Сезонна знижка'), ('Промоційна знижка', 'Промоційна знижка')], max_length=20),
        ),
    ]
