from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):
    def create_user(
        self,
        phone_number: str,
        password: str = None,
        is_staff=False,
        is_superuser=False):
        if not phone_number:
            raise ValueError("User must have an PhoneNumber")

        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(
        self, phone_number: str,  password: str):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user


class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, verbose_name='PhoneNumber', unique=True)
    username = None

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
