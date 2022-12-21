from rest_framework import serializers
from .models import Floor, Spot, SpotType


class FloorSerializer(serializers.ModelSerializer):

    motorcycle_spots = serializers.IntegerField(write_only=True)
    car_spots = serializers.IntegerField(write_only=True)
    spot_counts = serializers.SerializerMethodField()

    class Meta:
        model = Floor
        fields = [
            "id",
            "name",
            "spot_priority",
            "parking_lot",
            "motorcycle_spots",
            "car_spots",
            "spot_counts",
        ]
        read_only_fields = ["parking_lot"]

        # extra_kwargs = {"owner": {"read_only": True}}
        # read_only_fields = ["owner"]

    def get_spot_counts(self, obj: Floor) -> dict:
        car_spots = obj.spots.filter(variety=SpotType.CAR).count()
        motorcycle_spots = obj.spots.filter(variety=SpotType.MOTORCYCLE).count()

        return {
            'car_spots': car_spots,
            'motorcycle': motorcycle_spots
        }

    def create(self, validated_data: dict) -> Floor:

        car_spots_qnt = validated_data.pop('car_spots')
        motorcycle_spots_qnt = validated_data.pop('motorcycle_spots')

        floor_obj = Floor.objects.create(**validated_data)

        # for _ in range(car_spots_qnt):
        #     Spot.objects.create(variety=SpotType.CAR, floor=floor_obj)

        # for _ in range(motorcycle_spots_qnt):
        #     Spot.objects.create(variety=SpotType.MOTORCYCLE, floor=floor_obj)

        car_objects = [
            Spot(variety=SpotType.CAR, floor=floor_obj) for _ in range(car_spots_qnt)
        ]
        motorcycle_objects = [
            Spot(variety=SpotType.MOTORCYCLE, floor=floor_obj) for _ in range(motorcycle_spots_qnt)
        ]

        Spot.objects.bulk_create(car_objects + motorcycle_objects)

        return floor_obj
    