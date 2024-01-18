from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from rest_framework.response import Response
from rest_framework import status,permissions,viewsets,generics
from .serializers import *
from django.http import HttpResponse

# def hello_portal(request):
#     return HttpResponse("Hello, Portal!")
class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer

class AllMasterViewSet(viewsets.ModelViewSet):
    queryset = AllMaster.objects.all()
    serializer_class = AllMasterSerializer

class TokenMasterViewSet(viewsets.ModelViewSet):
    queryset = TokenMaster.objects.all()
    serializer_class = TokenMasterSerializer

class RoleMasterViewSet(viewsets.ModelViewSet):
    queryset = RoleMaster.objects.all()
    serializer_class = RoleMasterSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProducttByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_sub_id = self.kwargs['category_sub_id']
        return Product.objects.filter(category__id=category_sub_id)
    
class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
