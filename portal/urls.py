from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userdetail', UserDetailViewSet, basename='userdetail')
router.register(r'allmaster', AllMasterViewSet, basename='allmaster')
router.register(r'tokenmaster', TokenMasterViewSet, basename='tokenmaster')
router.register(r'rolemaster', RoleMasterViewSet, basename='rolemaster')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'wallet', WalletViewSet, basename='wallet')




urlpatterns = [
    path('', include(router.urls)),
    path('product/category/<int:category_sub_id>/', ProducttByCategory.as_view(), name='formmst-utilsub')
]