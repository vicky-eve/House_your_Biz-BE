
from django.contrib.auth.decorators import login_required
from Housingapp.models import Tenant, House, Comment, User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import TenantSerializer, CommentSerializer, HouseSerializer, UserSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.http import  Http404


#api views
class TenantList(APIView):
    def get(self, request, format=None):
        all_tenants = Tenant.objects.all()
        serializers = TenantSerializer(all_tenants, many=True)
        return Response(serializers.data)
        

    def post(self, request, format=None):
        serializers = TenantSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class TenantDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_tenant(self, pk):
        try:
            return Tenant.objects.get(pk=pk)
        except Tenant.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        tenant = self.get_tenant(pk)
        serializers = TenantSerializer(tenant)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        tenant = self.get_tenant(pk)
        serializers = TenantSerializer(tenant, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tenant = self.get_tenant(pk)
        tenant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentList(APIView):
    def get(self, request, format=None):
        all_comments = Comment.objects.all()
        serializers = CommentSerializer(all_comments, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class CommentDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        comment = self.get_comment(pk)
        serializers = CommentSerializer(comment)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        comment = self.get_comment(pk)
        serializers = CommentSerializer(comment, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_comment(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HouseList(APIView):
    def get(self, request, format=None):
        all_houses = House.objects.all()
        serializers = HouseSerializer(all_houses, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = HouseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

    

class HouseDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_house(self, pk):
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        house = self.get_house(pk)
        serializers = HouseSerializer(house)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        house = self.get_House(pk)
        serializers = HouseSerializer(house, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        house = self.get_house(pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    def get(self, request, format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

    

class UserDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        post = self.get_user(pk)
        serializers = UserSerializer(post)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        user = self.get_user(pk)
        serializers = UserSerializer(user, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



