from .models import Account
from .serializers import AccountSerializer

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_url_kwarg = "account_id"

