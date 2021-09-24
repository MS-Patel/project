from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Landing)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'phone', 'balance')


admin.site.register(models.UserOtp)
