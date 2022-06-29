from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# Create your models here.

phone_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$", message=_('Enter Bangladeshi Number with country code'))


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)
    picture = models.ImageField(upload_to='profile_pics')
