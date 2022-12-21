from rest_framework import serializers
from .models import ParkingLot
from accounts.serializers import AccountSerializer

class ParkingLotSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    
    class Meta:
        model = ParkingLot
        fields = ["id", "name", "owner"]

        extra_kwargs = {"owner": {"read_only": True}}


class DetailParkingLotSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(read_only=True)
    
    class Meta:
        model = ParkingLot
        fields = ["id", "name", "owner"]

        extra_kwargs = {"owner": {"read_only": True}}

class ParkingLotSerializer(serializers.ModelSerializer):
    
    owner_username = serializers.SerializerMethodField()

    def get_owner_username(self, obj: ParkingLot) -> str:
        return obj.owner.username


    class Meta:
        model = ParkingLot
        fields = ["id", "name", "owner", "owner_username"]

        # extra_kwargs = {"owner": {"read_only": True}}
        # read_only_fields = ["owner"]