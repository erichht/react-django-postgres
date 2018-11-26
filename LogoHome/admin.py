from django.contrib import admin

# Register your models here.
from .models import Hats, Suppliers, Garments

class HatsInline(admin.TabularInline):
    model = Hats
    extra = 1

class SuppliersAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date Information',        {'fields': ['registration_date']}),
        ('Supplier Information',    {'fields': ['no_char', 'name_char'], 'classes':['collapse']}),
        ('Location Information',    {'fields': ['location_char', 'country_char']}),
        ('Other Information',       {'fields': ['contact_char']}),
    ]
    inlines = [HatsInline]
    list_display = ('no_char','name_char','registration_date','registration_inputed')
    list_filter = ['registration_date']
    search_fields = ['no_char']

admin.site.register(Suppliers, SuppliersAdmin)

admin.site.register(Hats)
admin.site.register(Garments)