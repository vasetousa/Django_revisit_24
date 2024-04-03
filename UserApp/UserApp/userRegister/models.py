from django.contrib.auth import models as auth_models, get_user_model
from django.db import models

from UserApp.userRegister.managers import AppUserManager

''' Almost completely custom model, always create your own class User, inheriting from AbstractBaseUser,
using email/password for credentials
'''


class AppUser(auth_models.AbstractBaseUser):
    # we chose the email/password for credentials
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    # make sure you have these 3 fields in order to use Admin panel
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    # !!!! Those 2 are imperative !!!!
    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission.
        """
        # For simplicity, return True here. Modify as needed based on your permission logic.
        return True

    def has_module_perms(self, app_label):
        """
        Return True if the user has permission to view the app `app_label`.
        """
        # For simplicity, return True here. Modify as needed based on your permission logic.
        return True

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=30)

    date_of_birth = models.DateField(
        verbose_name="Date of Birth",
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
