from django.contrib import admin
from userauths.models import Profile, User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin): # Enable import/export for Product model
    list_display = ["username", "full_name", "email", "phone", ]
    list_display_links=["username","email"]
    search_fields = ["username", "full_name", "email", "phone", ]



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Define what fields should be shown in the list display
    list_display = ["get_username", "full_name", "get_user_email", "get_user_phone", "gender", "country", "state", "city"]
    
    # Define clickable links for more details (only if it's relevant)
    list_display_links = ["get_username", "get_user_email"]

    # Enable search on relevant fields
    search_fields = ["user__username", "full_name", "user__email", "user__phone", "country", "state", "city"]

    # Optionally, add filters to narrow down by fields like gender or country
    list_filter = ["gender", "country", "state"]

    # You can add a method to display the username or email properly
    def get_username(self, obj):
        return obj.user.username
    get_username.admin_order_field = 'user__username'  # Allow sorting by username
    get_username.short_description = 'Username'  # Custom column header

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.admin_order_field = 'user__email'  # Allow sorting by email
    get_user_email.short_description = 'Email'  # Custom column header

    def get_user_phone(self, obj):
        return obj.user.phone
    get_user_phone.admin_order_field = 'user__phone'  # Allow sorting by phone number
    get_user_phone.short_description = 'Phone'  # Custom column header
