from django.db import models

from ..address.models import Address
from ..covered_people.models import Person


class _TypeChoices:

    @staticmethod
    def get_choices():
        return (
            ('AID_TYPE_CASH', 'کمک نقدی'),
            ('AID_TYPE_NONE_CASH', 'کمک غیر نقدی')
        )


class Charity(models.Model):
    name = models.CharField(
        max_length=64
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name='Charity'
    )
    phone_number = models.CharField(
        max_length=11
    )
    manager_name = models.CharField(
        max_length=32
    )
    manager_phone = models.CharField(
        max_length=11
    )


class Plan(models.Model):
    title = models.CharField(
        max_length=32
    )
    total_budget = models.FloatField(
        default=0.0
    )
    spent_budget = models.FloatField(
        default=0.0
    )
    organizer = models.CharField(
        default='بدون طرح'
    )

    def has_budget(self):
        return (
            self.spent_budget < self.total_budget,
            self.total_budget - self.spent_budget
        )


class Aid(models.Model):
    title = models.CharField(
        max_length=32
    )
    type = models.CharField(
        max_length=16,
        choices=_TypeChoices.get_choices(),
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    amount = models.FloatField(
        default=0.0,
    )
    person = models.ForeignKey(
        Person,
        related_name='aids',
        on_delete=models.PROTECT
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        related_name='aids'
    )

