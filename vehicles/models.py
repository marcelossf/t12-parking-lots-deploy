from django.db import models
from floors.models import SpotType


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)
    vehicle_type = models.CharField(
        max_length=20,
        choices=SpotType.choices,
    )
    arrived_at = models.DateTimeField(auto_now_add=True)
    amount_paid = models.IntegerField(null=True, default=None)
    paid_at = models.DateTimeField(null=True, default=None)
    vehicle_image = models.ImageField(null=True)

    spot = models.ForeignKey(
        "floors.Spot",
        on_delete=models.CASCADE,
        related_name="vehicles",
        null=True
    )