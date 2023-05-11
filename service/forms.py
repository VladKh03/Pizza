from datetime import datetime

from django.forms import ModelForm
from django import forms
from service.models import Client, Order, Pizza, Payment, Courier, Chef, Delivery, Feedback, Promo


class SearchFirst(ModelForm):
    class Meta:
        model = Client
        fields = ['client_order', 'phone_number']

class SearchSecond(ModelForm):
    class Meta:
        model = Order
        fields = ['courier_order', 'delivery_address']
class SearchThird(ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_chef', 'name']
class SearchFourth(forms.Form):
    promo_payment = forms.CharField(max_length=100, label='Промокод')
    payment_date = forms.DateField(input_formats=['%d.%m.%Y'], label='Дата оплати')

class SearchFifth(ModelForm):
    class Meta:
        model = Courier
        fields = ['delivery_courier', 'first_name']
class SearchSixth(ModelForm):
    class Meta:
        model = Chef
        fields = ['chef_order', 'first_name']
class SearchSeventh(forms.Form):
    payment_delivery = forms.CharField(max_length=100, label='Оплата')
    delivery_date = forms.DateField(input_formats=['%d.%m.%Y'], label='Дата доставки')

class SearchEighth(ModelForm):
    class Meta:
        model = Feedback
        fields = ['client_feedback', 'feedback_date']
class SearchNinth(forms.Form):
    promo_order = forms.CharField(max_length=100, label='Замовлення')
    promo_name = forms.CharField(max_length=100, label='Назва промокода')
    class Meta:
        model = Promo
        fields = ['', 'promo_name']


