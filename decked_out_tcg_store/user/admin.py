from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fname', 'lname', 'shipping_address_line_1', 'shipping_address_line_2', 'shipping_address_town', 'shipping_address_county', 'shipping_address_eircode')
    search_fields = ('user__username', 'user__email', 'fname', 'lname')

