from django.contrib import admin

from UserApp.userRegister.models import AppUser, Profile


# Register your models here.
@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'phone_number']
    sortable_by = ['last_name', 'first_name']
