from rest_framework import serializers
from .models import Vehicle


class VechicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            "id",
            "license_plate",
            "vehicle_type",
            "arrived_at",
            "amount_paid",
            "spot",
            "vehicle_image",
        ]

        # read_only = ['spot']