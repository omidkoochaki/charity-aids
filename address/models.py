from django.db import models


class Address(models.Model):
    state = models.CharField(max_length=32, default='خراسان جنوبی')
    city = models.CharField(max_length=32, default='فردوس')
    address = models.TextField(null=False, blank=False)
