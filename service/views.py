from django.shortcuts import render

from service.forms import SearchFirst, SearchSecond, SearchThird, SearchFourth, SearchFifth, SearchSixth, SearchSeventh, \
    SearchEighth, SearchNinth
from service.models import Client, Order, Pizza, Payment, Courier, Chef, Delivery, Feedback, Promo


# Create your views here.
def index(request):
    return render(request, 'service/index.html')

def first(request):
    form = SearchFirst()
    clients = Client.objects.all()
    if request.method == "POST":
        form = SearchFirst(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            client_order = form.cleaned_data['client_order']
            clients = Client.objects.filter(phone_number=phone_number, client_order=client_order)
    return render(request, 'service/first.html', {'clients': clients, 'form': form})


def second(request):
    form = SearchSecond()
    orders = Order.objects.all()
    if request.method == "POST":
        form = SearchSecond(request.POST)
        if form.is_valid():
            delivery_address = form.cleaned_data['delivery_address']
            courier_order = form.cleaned_data['courier_order']
            orders = Order.objects.filter(delivery_address=delivery_address, courier_order=courier_order)
    return render(request, 'service/second.html', {'orders': orders, 'form': form})


def third(request):
    form = SearchThird()
    pizzas = Pizza.objects.all()
    if request.method == "POST":
        form = SearchThird(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pizza_chef = form.cleaned_data['pizza_chef']
            pizzas = Pizza.objects.filter(name=name, pizza_chef=pizza_chef)
    return render(request, 'service/third.html', {'pizzas': pizzas, 'form': form})


def fourth(request):
    form = SearchFourth()
    payments = Payment.objects.all()
    if request.method == "POST":
        form = SearchFourth(request.POST)
        if form.is_valid():
            payment_date = form.cleaned_data['payment_date']
            promo_payment = form.cleaned_data['promo_payment']
            payments = Payment.objects.filter(payment_date=payment_date, promo_payment=promo_payment)
    return render(request, 'service/fourth.html', {'payments': payments, 'form': form})


def fifth(request):
    form = SearchFifth()
    couriers = Courier.objects.all()
    if request.method == "POST":
        form = SearchFifth(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            delivery_courier = form.cleaned_data['delivery_courier']
            couriers = Courier.objects.filter(first_name=first_name, delivery_courier=delivery_courier)
    return render(request, 'service/fifth.html', {'couriers': couriers, 'form': form})


def sixth(request):
    form = SearchSixth()
    chefs = Chef.objects.all()
    if request.method == "POST":
        form = SearchSixth(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            chef_order = form.cleaned_data['chef_order']
            chefs = Chef.objects.filter(first_name=first_name, chef_order=chef_order)
    return render(request, 'service/sixth.html', {'chefs': chefs, 'form': form})


def seventh(request):
    form = SearchSeventh()
    deliveries = Delivery.objects.all()
    if request.method == "POST":
        form = SearchSeventh(request.POST)
        if form.is_valid():
            delivery_date = form.cleaned_data['delivery_date']
            payment_delivery = form.cleaned_data['payment_delivery']
            deliveries = Delivery.objects.filter(delivery_date=delivery_date, payment_delivery=payment_delivery)
    return render(request, 'service/seventh.html', {'deliveries': deliveries, 'form': form})




def eighth(request):
    form = SearchEighth()
    feedbacks = Feedback.objects.all()
    if request.method == "POST":
        form = SearchEighth(request.POST)
        if form.is_valid():
            feedback_date = form.cleaned_data['feedback_date']
            client_feedback = form.cleaned_data['client_feedback']
            feedbacks = Feedback.objects.filter(feedback_date=feedback_date, client_feedback=client_feedback)
    return render(request, 'service/eighth.html', {'feedbacks': feedbacks, 'form': form})


def ninth(request):
    form = SearchNinth()
    promos = Promo.objects.all()
    if request.method == "POST":
        form = SearchNinth(request.POST)
        if form.is_valid():
            promo_name = form.cleaned_data['promo_name']
            promo_order = form.cleaned_data['promo_order']
            promos = Promo.objects.filter(promo_name=promo_name, promo_order=promo_order)
    return render(request, 'service/ninth.html', {'promos': promos, 'form': form})