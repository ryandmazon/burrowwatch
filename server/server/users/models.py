from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import CharField, EmailField, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Default custom user model for server.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    name = CharField(_("Name of User"), blank=True, max_length=255)
    email = EmailField(_("Email"), max_length=255, unique=True)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    is_superuser = BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

