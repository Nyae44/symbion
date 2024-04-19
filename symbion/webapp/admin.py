from django.contrib import admin

# Register your models here.
from .models import Record 

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['date_created', 'first_name', 'last_name', 'email', 'phone','address','city', 'county']