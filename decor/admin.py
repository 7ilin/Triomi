from django.contrib import admin
from decor.models import Call, Portfolio, Post, Rent


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_date', 'status')


admin.site.register(Portfolio)
admin.site.register(Post)
admin.site.register(Rent)



# Register your models here.
