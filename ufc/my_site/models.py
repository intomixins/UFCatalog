from django.db import models


class Fighter(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField()
    loses = models.IntegerField()
    draws = models.IntegerField()
    first_fight_data = models.DateField(blank=True, null=True)
    is_retired = models.BooleanField(default=False)
