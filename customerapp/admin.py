from django.contrib import admin
from customerapp.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name', 'phone',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
