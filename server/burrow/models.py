from django.db import models
from django.contrib.auth import get_user_model
from location_field.forms.plain import PlainLocationField


class Burrow(models.Model):
    uuid = models.BigAutoField(primary_key=True)
    owl_count = models.IntegerField()
    location = PlainLocationField()
    date_discovered = models.DateField()
    last_checked = models.DateField()
    last_checked_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
