from rest_framework import serializers
from .models import *


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

class AllMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllMaster
        fields = '__all__'

class TokenMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TokenMaster
        fields = '__all__'

class RoleMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleMaster
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    Category_title = serializers.StringRelatedField(source='category.title', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    def get_category_name(self, obj):
        return obj.category.title if obj.category else None
    
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'    
    
    




