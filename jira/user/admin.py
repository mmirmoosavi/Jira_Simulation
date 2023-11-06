from django.contrib import admin

from user.models import User


# add simple admin for user model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

