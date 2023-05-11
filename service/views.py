from django.shortcuts import render

from service.forms import SearchFirst
from service.models import Client


# Create your views here.
def index(request):
    return render(request, 'service/index.html')

#birth_date


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
    return render(request, 'service/second.html')


def third(request):
    return render(request, 'service/third.html')


def fourth(request):
    return render(request, 'service/fourth.html')


def fifth(request):
    return render(request, 'service/fifth.html')


def sixth(request):
    return render(request, 'service/sixth.html')


def seventh(request):
    return render(request, 'service/seventh.html')


def eighth(request):
    return render(request, 'service/eighth.html')


def ninth(request):
    return render(request, 'service/ninth.html')