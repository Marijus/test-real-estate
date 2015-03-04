from django.shortcuts import render
from properties.forms import AddressForm


def index(request):
    return render(request, "index.html", {"form": AddressForm})