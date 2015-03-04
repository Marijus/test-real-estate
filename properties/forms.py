from address.forms import AddressField
from django import forms

class AddressForm(forms.Form):
  address = AddressField()