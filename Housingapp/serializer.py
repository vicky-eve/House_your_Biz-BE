from rest_framework import serializers
from .models import Tenant, House, Comment, User

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('id')

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id','name', 'price', 'location')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','text')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','is_tenant', 'is_landlord' )