from .serializers import ParkingLotSerializer, DetailParkingLotSerializer
from .models import ParkingLot
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrParkingLotOwner


class ParkingLotView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ParkingLotSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DetailParkingLotSerializer

        return ParkingLotSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ParkingLot.objects.all()

        return ParkingLot.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    """ SERVE PARA SOBRESCREVER O METODO GET E ALTERAR, COMO QUISER, O RETORNO DA RESPOSTA 
     def get(self, request: Request) -> Response:
         response = super().get(request)
         response.data = {"data": response.data}

         return response """


class ParkingLotDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrParkingLotOwner]

    serializer_class = ParkingLotSerializer
    queryset = ParkingLot.objects.all()

    lookup_url_kwarg = "parking_lot_id"
