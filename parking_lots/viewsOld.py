from rest_framework.views import APIView, Request, Response, status
from .models import ParkingLot
from .serializers import ParkingLotSerializer
from django.shortcuts import get_object_or_404

class ParkinLotView(APIView):
    def get(self, request: Request) -> Response:

        parkings = ParkingLot.objects.all()
        serializer = ParkingLotSerializer(parkings, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ParkingLotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class ParkingLotDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:

        parking = get_object_or_404(ParkingLot, id=pk)
        serializer = ParkingLotSerializer(parking)

        return Response(serializer.data, status.HTTP_200_OK)


    def patch(self, request: Request, pk) -> Response:

        parking = get_object_or_404(ParkingLot, id=pk)
        serializer = ParkingLotSerializer(parking, request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pk) -> Response:

        parking = get_object_or_404(ParkingLot, id=pk)
        parking.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)