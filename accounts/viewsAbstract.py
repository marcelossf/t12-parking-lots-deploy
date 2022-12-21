
from .models import Account
from .serializers import AccountSerializer

from utils.common_views import PostGetCommonView
from utils.detail_common_views import (GetPatchDeleteDetailView)


class RegisterView(PostGetCommonView):
    view_serializer = AccountSerializer
    view_queryset = Account.objects.all()

class AccountDetailView(GetPatchDeleteDetailView):
    view_serializer = AccountSerializer
    view_queryset = Account.objects.all()
    url_param_name = "account_id"

