from django.db import models
from django.utils import timezone
import datetime

# Items of MyLogo.
# Add null=True per the suggestion below 
# https://docs.djangoproject.com/en/2.0/topics/migrations/#postgresql
# "...the only caveat is that adding columns with default 
# values will cause a full rewrite of the table, for a time proportional to its size
# For this reason, it’s recommended you always create new columns with null=True, 
# as this way they will be added immediately...."

class Suppliers(models.Model):
    no_char = models.CharField(max_length=30, null=True)
    name_char = models.CharField(max_length=60, null=True)
    location_char = models.CharField(max_length=80, null=True)
    country_char = models.CharField(max_length=60, null=True)
    contact_char = models.CharField(max_length=60, null=True)
    registration_date = models.DateTimeField(null=True, blank=True)
    def registration_inputed(self):
        now = timezone.now()
        return now - datetime.timedelta(days=2) <= self.registration_date <= now
    registration_inputed.admin_order_field = 'registration_date'
    registration_inputed.boolean = True
    registration_inputed.short_description = 'Registered recently?'

class Hats(models.Model):
    suppliersno = models.ForeignKey(Suppliers, on_delete=models.CASCADE, null=True)
    type_char = models.CharField(max_length=30, null=True)
    size_char = models.CharField(max_length=20, null=True)
    color_char = models.CharField(max_length=20, null=True)
    price_number = models.IntegerField(default=0, null=True)
    memo_text = models.TextField(null=True, blank=True)
    entry_date = models.DateTimeField(null=True, blank=True)

class Garments(models.Model):
    suppliersno = models.ForeignKey(Suppliers, on_delete=models.CASCADE, null=True)
    type_char = models.CharField(max_length=30, null=True)
    size_char = models.CharField(max_length=20, null=True)
    color_char = models.CharField(max_length=20, null=True)
    price_number = models.IntegerField(default=0, null=True)
    manu_char = models.CharField(max_length=30, null=True)
    memo_text = models.TextField(null=True, blank=True)
    entry_date = models.DateTimeField(null=True, blank=True)
    def just_entered(self):
        return self.entry_date >= timezone.now() - datetime.timedelta(days=1)