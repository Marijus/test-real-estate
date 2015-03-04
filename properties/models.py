from django.db import models
from address.models import AddressField


class Property(models.Model):
    # test = models.CharField(max_length=50)
    address = AddressField(blank=True, null=True)