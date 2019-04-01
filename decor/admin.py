from django.contrib import admin
from decor.models import Call, Portfolio


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_date', 'status')


admin.site.register(Portfolio)



# Register your models here.
