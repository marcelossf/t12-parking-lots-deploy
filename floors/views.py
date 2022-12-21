from rest_framework import generics
from .serializers import FloorSerializer
from .models import Floor
from parking_lots.models import ParkingLot
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from parking_lots.permissions import IsAdminOrParkingLotOwner


class FloorView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    serializer_class = FloorSerializer

    def get_queryset(self):
        parking_lot_id = self.kwargs["parking_lot_id"]
        parking_lot_obj = get_object_or_404(ParkingLot, pk=parking_lot_id)

        floors = Floor.objects.filter(parking_lot=parking_lot_obj)

        return floors

    def perform_create(self, serializer):
        parking_lot_id = self.kwargs["parking_lot_id"]
        parking_lot_obj = get_object_or_404(ParkingLot, pk=parking_lot_id)

        self.check_object_permissions(self.request, parking_lot_obj)

        serializer.save(parking_lot=parking_lot_obj)
