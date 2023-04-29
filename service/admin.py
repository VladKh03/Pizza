from django.contrib import admin

from service.models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('client_id', 'first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('client_id', 'first_name', 'last_name', 'email', 'phone_number')
    fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('client_id', 'first_name', 'last_name', 'email', 'phone_number')


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('pizza_id', 'name', 'weight', 'description', 'size_pizza')
    list_filter = ('pizza_id', 'name', 'weight', 'description', 'size_pizza__size_id')
    search_fields = ('pizza_id', 'name', 'weight', 'description', 'size_pizza__size_id')
    fields = ('name', 'weight', 'description', 'size_pizza')
    ordering = ('pizza_id', 'name', 'weight', 'description', 'size_pizza__size_id')


@admin.register(PizzaSize)
class PizzaSizeAdmin(admin.ModelAdmin):
    list_display = ('size_id', 'size_type', 'crust_type', 'price')
    list_filter = ('size_id', 'size_type', 'crust_type', 'price')
    search_fields = ('size_id', 'size_type', 'crust_type', 'price')
    fields = ('size_type', 'crust_type', 'price')
    ordering = ('size_id', 'size_type', 'crust_type', 'price')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'payment_type', 'payment_date', 'payment_time')
    list_filter = ('payment_id', 'payment_type', 'payment_date', 'payment_time')
    search_fields = ('payment_id', 'payment_type', 'payment_date', 'payment_time')
    fields = ('payment_type', 'payment_date', 'payment_time')
    ordering = ('payment_id', 'payment_type', 'payment_date', 'payment_time')


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('courier_id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')
    list_filter = ('courier_id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')
    search_fields = ('courier_id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')
    ordering = ('courier_id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience')


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('chef_id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')
    list_filter = ('chef_id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')
    search_fields = ('chef_id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')
    fields = ('first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')
    ordering = ('chef_id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'delivery_id', 'delivery_date', 'delivery_time', 'payment_delivery', 'delivery_comment')
    list_filter = ('delivery_id', 'delivery_date', 'delivery_time', 'payment_delivery__payment_id',
                   'delivery_comment')
    search_fields = (
        'delivery_id', 'delivery_date', 'delivery_time', 'payment_delivery__payment_id',
        'delivery_comment')
    fields = ('delivery_date', 'delivery_time', 'payment_delivery', 'delivery_comment')
    ordering = ('delivery_id', 'delivery_date', 'delivery_time', 'payment_delivery__payment_id',
                'delivery_comment')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_id', 'rating', 'feedback_date', 'feedback_time', 'client_feedback', 'feedback_text')
    list_filter = (
        'feedback_id', 'rating', 'feedback_date', 'feedback_time', 'client_feedback__client_id', 'feedback_text')
    search_fields = (
        'feedback_id', 'rating', 'feedback_date', 'feedback_time', 'client_feedback__client_id', 'feedback_text')
    fields = ('rating', 'feedback_date', 'feedback_time', 'client_feedback', 'feedback_text')
    ordering = (
        'feedback_id', 'rating', 'feedback_date', 'feedback_time', 'client_feedback__client_id', 'feedback_text')


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('promo_id', 'promo_name', 'discount', 'valid_term', 'promo_date')
    list_filter = ('promo_id', 'promo_name', 'discount', 'valid_term', 'promo_date__promodate_id')
    search_fields = ('promo_id', 'promo_name', 'discount', 'valid_term', 'promo_date__promodate_id')
    fields = ('promo_name', 'discount', 'promo_date')
    ordering = ('promo_id', 'promo_name', 'discount', 'valid_term', 'promo_date__promodate_id')


@admin.register(PromoDate)
class PromoDateAdmin(admin.ModelAdmin):
    list_display = ('promodate_id', 'start_date', 'end_date', 'discount_type')
    list_filter = ('promodate_id', 'start_date', 'end_date', 'discount_type')
    search_fields = ('promodate_id', 'start_date', 'end_date', 'discount_type')
    fields = ('start_date', 'end_date', 'discount_type')
    ordering = ('promodate_id', 'start_date', 'end_date', 'discount_type')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id', 'client_order', 'payment_order', 'delivery_order', 'feedback_order', 'promo_order', 'pizza_order',
        'chef_order', 'order_date', 'order_time', 'delivery_address', 'amount')
    list_filter = ('order_id', 'client_order__client_id', 'payment_order__payment_id', 'delivery_order__delivery_id',
                   'feedback_order__feedback_id', 'promo_order__promo_id', 'pizza_order__pizza_id',
                   'chef_order__chef_id', 'order_date', 'order_time', 'delivery_address', 'amount')
    search_fields = ('order_id', 'client_order__client_id', 'payment_order__payment_id', 'delivery_order__delivery_id',
                     'feedback_order__feedback_id', 'promo_order__promo_id', 'pizza_order__pizza_id',
                     'chef_order__chef_id', 'order_date', 'order_time', 'delivery_address', 'amount')
    fields = (
        'client_order', 'payment_order', 'delivery_order', 'feedback_order', 'promo_order', 'pizza_order', 'chef_order',
        'order_date', 'order_time', 'delivery_address')
    ordering = ('order_id', 'client_order__client_id', 'payment_order__payment_id', 'delivery_order__delivery_id',
                'feedback_order__feedback_id', 'promo_order__promo_id', 'pizza_order__pizza_id', 'chef_order__chef_id',
                'order_date', 'order_time', 'delivery_address', 'amount')
