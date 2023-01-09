from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from ..charity.models import Charity


class User(AbstractBaseUser):
    charity = models.ForeignKey(
        Charity,
        on_delete=models.CASCADE,
        related_name='staff'
    )
    mobile = models.CharField(max_length=11)
    full_name = models.CharField(max_length=32)

    USERNAME_FIELD = 'mobile'
