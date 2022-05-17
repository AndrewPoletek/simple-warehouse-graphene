from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ItemPattern(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    sugessted_price = models.DecimalField(decimal_places=3, max_digits=10)

class Warehouse(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    read_access = models.ManyToManyField(User, related_name='read_access_users')
    write_access = models.ManyToManyField(User, related_name='write_access_users')
    name = models.CharField(max_length=250, verbose_name="Warehouse name")

class Items(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    count = models.IntegerField()
    price = models.DecimalField(decimal_places=3, max_digits=10)
    archived = models.BooleanField(default=False)

class ShiftType(models.Model):
    name = models.CharField(max_length=250)
    short_code = models.CharField(max_length=10)

class ShiftLog(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='creator_user')
    approver = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, related_name='approver_user')
    outside = models.BooleanField(default=False)
    shift_date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Items, on_delete=models.PROTECT)
    shift_type = models.ForeignKey(ShiftType, on_delete=models.PROTECT)
