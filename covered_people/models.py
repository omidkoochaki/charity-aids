from django.db import models

from CharityAids.address.models import Address


class Family(models.Model):
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name='family',
    )
    family_name = models.CharField(
        max_length=32
    )
    head_phone_number = models.CharField(
        max_length=11
    )


class Person(models.Model):
    full_name = models.CharField(
        max_length=32,
    )
    national_code = models.CharField(
        max_length=10,
        validators=[
            # TODO: add validator here
        ]
    )
    family = models.ForeignKey(
        Family,
        on_delete=models.PROTECT,
        related_name='members'
    )


