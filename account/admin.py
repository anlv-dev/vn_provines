from django.contrib import admin
from .models import Account
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name','last_name', 'username','date_joined', 'is_staff', 'is_admin')
    search_fields = ('email', 'date_joined')
    readonly_fields = ('date_joined', 'last_login')  # make fields immutable
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()

admin.site.register(Account, AccountAdmin)

