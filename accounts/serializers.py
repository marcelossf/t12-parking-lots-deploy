from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    parking_lots_count = serializers.SerializerMethodField()

    def get_parking_lots_count(self, obj: Account):
        pl_count = obj.parking_lots.count()

        return pl_count

    def create(self, validated_data: dict) -> Account:

        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():

            if key == "password":
                instance.set_password(value)

            else:
                setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Account
        # fields = '__all__'
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser",
            "shift",
            "parking_lots_count"
        ]
        
        extra_kwargs = {'password': {'write_only': True}}