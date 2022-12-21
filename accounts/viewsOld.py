from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Account
from .serializers import AccountSerializer

class RegisterView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer