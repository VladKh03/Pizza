from django.forms import ModelForm

from service.models import Client


class SearchFirst(ModelForm):
    class Meta:
        model = Client
        fields = ['client_order', 'phone_number']