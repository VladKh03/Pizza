from django.contrib import admin

from service.models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('id', 'first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')
    fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('id', 'first_name', 'last_name', 'email', 'phone_number')


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'description', 'size_pizza')
    list_filter = ('id', 'name', 'weight', 'description', 'size_pizza__size_type')
    search_fields = ('id', 'name', 'weight', 'description', 'size_pizza__size_type')
    fields = ('name', 'weight', 'description', 'size_pizza')
    ordering = ('id', 'name', 'weight', 'description', 'size_pizza__size_type')


@admin.register(PizzaSize)
class PizzaSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size_type', 'crust_type', 'price')
    list_filter = ('id', 'size_type', 'crust_type', 'price')
    search_fields = ('id', 'size_type', 'crust_type', 'price')
    fields = ('size_type', 'crust_type', 'price')
    ordering = ('id', 'size_type', 'crust_type', 'price')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_type', 'payment_date', 'payment_time')
    list_filter = ('id', 'payment_type', 'payment_date', 'payment_time')
    search_fields = ('id', 'payment_type', 'payment_date', 'payment_time')
    fields = ('payment_type', 'payment_date', 'payment_time')
    ordering = ('id', 'payment_type', 'payment_date', 'payment_time')


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')
    list_filter = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')
    ordering = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')
    list_filter = ('id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')
    search_fields = ('id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')
    fields = ('first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')
    ordering = ('id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'delivery_date', 'delivery_time', 'delivery_comment')
    list_filter = ('id', 'delivery_date', 'delivery_time',
                   'delivery_comment')
    search_fields = (
        'id', 'delivery_date', 'delivery_time',
        'delivery_comment')
    fields = ('delivery_date', 'delivery_time', 'delivery_comment')
    ordering = ('id', 'delivery_date', 'delivery_time',
                'delivery_comment')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'feedback_date', 'feedback_time', 'client_feedback', 'feedback_text')
    list_filter = (
        'id', 'rating', 'feedback_date', 'feedback_time', 'client_feedback__last_name', 'feedback_text')
    search_fields = (
        'id', 'rating', 'feedback_date', 'feedback_time', 'client_feedback__last_name', 'feedback_text')
    fields = ('rating', 'feedback_date', 'feedback_time', 'client_feedback', 'feedback_text')
    ordering = (
        'id', 'rating', 'feedback_date', 'feedback_time', 'client_feedback__last_name', 'feedback_text')


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'promo_name', 'discount', 'valid_term', 'promo_date')
    list_filter = ('id', 'promo_name', 'discount', 'valid_term', 'promo_date__discount_type')
    search_fields = ('id', 'promo_name', 'discount', 'valid_term', 'promo_date__discount_type')
    fields = ('promo_name', 'discount', 'promo_date')
    ordering = ('id', 'promo_name', 'discount', 'valid_term', 'promo_date__discount_type')


@admin.register(PromoDate)
class PromoDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'discount_type')
    list_filter = ('id', 'start_date', 'end_date', 'discount_type')
    search_fields = ('id', 'start_date', 'end_date', 'discount_type')
    fields = ('start_date', 'end_date', 'discount_type')
    ordering = ('id', 'start_date', 'end_date', 'discount_type')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'client_order', 'payment_order', 'delivery_order', 'feedback_order', 'promo_order', 'pizza_order',
        'chef_order', 'order_date', 'order_time', 'delivery_address', 'amount')
    list_filter = ('id', 'client_order__last_name', 'payment_order__payment_type', 'delivery_order__id',
                   'feedback_order__rating', 'promo_order__promo_name', 'pizza_order__name',
                   'chef_order__last_name', 'order_date', 'order_time', 'delivery_address', 'amount')
    search_fields = ('id', 'client_order__last_name', 'payment_order__payment_type', 'delivery_order__id',
                     'feedback_order__rating', 'promo_order__promo_name', 'pizza_order__name',
                     'chef_order__last_name', 'order_date', 'order_time', 'delivery_address', 'amount')
    fields = (
        'client_order', 'payment_order', 'delivery_order', 'feedback_order', 'promo_order', 'pizza_order', 'chef_order',
        'order_date', 'order_time', 'delivery_address')
    ordering = ('id', 'client_order__last_name', 'payment_order__payment_type', 'delivery_order__id',
                'feedback_order__rating', 'promo_order__promo_name', 'pizza_order__name',
                'chef_order__last_name', 'order_date', 'order_time', 'delivery_address', 'amount')
