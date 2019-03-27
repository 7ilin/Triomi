from django.contrib import admin
from .models import Call


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display  = ('name', 'phone_number', 'created_date')
# Register your models here.
