from django.contrib import admin

from service.models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'client_order')
    list_filter = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'client_order__id')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'client_order__id')
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'client_order')
    ordering = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'client_order__id')

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'description', 'size_pizza', 'pizza_chef')
    list_filter = ('id', 'name', 'weight', 'description', 'size_pizza__size_type', 'pizza_chef__last_name')
    search_fields = ('id', 'name', 'weight', 'description', 'size_pizza__size_type', 'pizza_chef__last_name')
    fields = ('name', 'weight', 'description', 'size_pizza', 'pizza_chef')
    ordering = ('id', 'name', 'weight', 'description', 'size_pizza__size_type', 'pizza_chef__last_name')


@admin.register(PizzaSize)
class PizzaSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size_type', 'crust_type', 'price')
    list_filter = ('id', 'size_type', 'crust_type', 'price')
    search_fields = ('id', 'size_type', 'crust_type', 'price')
    fields = ('size_type', 'crust_type', 'price')
    ordering = ('id', 'size_type', 'crust_type', 'price')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_type', 'payment_date', 'payment_time', 'promo_payment')
    list_filter = ('id', 'payment_type', 'payment_date', 'payment_time', 'promo_payment__promo_name')
    search_fields = ('id', 'payment_type', 'payment_date', 'payment_time', 'promo_payment__promo_name')
    fields = ('payment_type', 'payment_date', 'payment_time', 'promo_payment')
    ordering = ('id', 'payment_type', 'payment_date', 'payment_time', 'promo_payment__promo_name')


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience', 'delivery_courier')
    list_filter = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience', 'delivery_courier__delivery_date')
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience', 'delivery_courier__delivery_date')
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience', 'delivery_courier')
    ordering = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_count', 'experience', 'delivery_courier__delivery_date')


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number', 'chef_order')
    list_filter = ('id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number', 'chef_order__id')
    search_fields = ('id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number', 'chef_order__id')
    fields = ('first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number', 'chef_order')
    ordering = ('id', 'first_name', 'last_name', 'salary', 'experience', 'position', 'phone_number', 'chef_order__id')


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'delivery_date', 'delivery_time', 'delivery_comment', 'payment_delivery')
    list_filter = ('id', 'delivery_date', 'delivery_time',
                   'delivery_comment', 'payment_delivery__id')
    search_fields = (
        'id', 'delivery_date', 'delivery_time',
        'delivery_comment', 'payment_delivery__id')
    fields = ('delivery_date', 'delivery_time', 'delivery_comment', 'payment_delivery')
    ordering = ('id', 'delivery_date', 'delivery_time',
                'delivery_comment', 'payment_delivery__id')


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
    list_display = ('id', 'promo_name', 'discount', 'valid_term', 'promo_date', 'promo_order')
    list_filter = ('id', 'promo_name', 'discount', 'valid_term', 'promo_date__discount_type', 'promo_order__id')
    search_fields = ('id', 'promo_name', 'discount', 'valid_term', 'promo_date__discount_type', 'promo_order__id')
    fields = ('promo_name', 'discount', 'promo_date', 'promo_order')
    ordering = ('id', 'promo_name', 'discount', 'valid_term', 'promo_date__discount_type', 'promo_order__id')


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
        'id', 'courier_order', 'order_date', 'order_time', 'delivery_address', 'amount')
    list_filter = ('id', 'courier_order__last_name',
                 'order_date', 'order_time', 'delivery_address', 'amount')
    search_fields = ('id', 'courier_order__last_name',
                     'order_date', 'order_time', 'delivery_address', 'amount')
    fields = ('courier_order',
        'order_date', 'order_time', 'delivery_address')
    ordering = ('id', 'courier_order__last_name',
             'order_date', 'order_time', 'delivery_address', 'amount')
