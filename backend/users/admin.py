from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Subscribtion, User


@admin.register(Subscribtion)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'id',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('email', 'first_name')
