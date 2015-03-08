from django.db import models
from djorm_pgarray.fields import TextArrayField


class IpMonitor(models.Model):
    ip_address = models.CharField(max_length=253, primary_key=True)
    lookup_interval = models.IntegerField()
    next_lookup = models.DateTimeField()
    last_lookup = models.DateTimeField(null=True)
    last_hosts = TextArrayField(default=[])


class IpAlert(models.Model):
    ip_address = models.CharField(max_length=253)
    alert_text = models.CharField(max_length=100)
    alert_time = models.DateTimeField()