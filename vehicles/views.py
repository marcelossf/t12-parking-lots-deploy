from rest_framework import generics
from .models import Vehicle
from .serializers import VechicleSerializer
from parking_lots.models import ParkingLot
from django.shortcuts import get_object_or_404
from floors.models import Spot
from rest_framework.exceptions import NotFound

class VechicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VechicleSerializer

    def perform_create(self, serializer):
        parking_lot_id = self.kwargs["parking_lot_id"]
        parking_lot_obj = get_object_or_404(ParkingLot, pk=parking_lot_id)
        vehicle_type = serializer.validated_data["vehicle_type"]

        found_spot = (
            Spot.objects.filter(
                floor__parking_lot=parking_lot_obj,
                is_free=True,
                variety=vehicle_type,
            )
            .order_by("floor__spot_priority")
            .first()
        )

        if not found_spot:
            raise NotFound('Vaga não encontrada')

        found_spot.is_free = False
        found_spot.save()

        serializer.save(spot=found_spot)
