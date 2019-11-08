from django.db import models


# Create your models here.
class State(models.Model):
    time_span = models.IntegerField(blank=False, null=False)
    is_weekend = models.BooleanField(blank=False, null=False)


class Record(models.Model):
    action = models.CharField(max_length=50, blank=False, null=False)
    reward = models.IntegerField(blank=False, null=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
