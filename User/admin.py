from django.contrib import admin

from .models import User
# Register the User model with the admin site
# admin.site.register(User)
@admin.register(User)
class UserModels(admin.ModelAdmin):
    list_display = ['name','email','password']