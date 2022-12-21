from .serializers import ParkingLotSerializer
from .models import ParkingLot
from utils.common_views import PostGetCommonView
from utils.detail_common_views import (GetPatchDeleteDetailView)


class ParkinLotView(PostGetCommonView):
    view_serializer = ParkingLotSerializer
    view_queryset = ParkingLot.objects.all()

    """ SERVE PARA SOBRESCREVER O METODO GET E ALTERAR, COMO QUISER, O RETORNO DA RESPOSTA 
     def get(self, request: Request) -> Response:
         response = super().get(request)
         response.data = {"data": response.data}

         return response """


class ParkingLotDetailView(GetPatchDeleteDetailView):
    view_serializer = ParkingLotSerializer
    view_queryset = ParkingLot.objects.all()

    # Para customizar o que vem da url
    url_param_name = "parkin_lot_id"

    