from django.db import models


def sub_two_number(a, b):
    return a + b;


class ChoiceMock(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)