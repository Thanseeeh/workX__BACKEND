from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from freelancers.models import FreelancerProfile
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import CategorySerializer
from .models import Category

# Create your views here.


class BlockUnBlockUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            instance = Account.objects.get(id=user_id)
            instance.is_active = not instance.is_active
            instance.save()

            return Response({"message": "User status changed"}, status=status.HTTP_200_OK)
        
        except Account.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

class BlockUnBlockFreelancerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            instance = Account.objects.get(id=user_id)
            instance.is_active = not instance.is_active
            instance.save()

            return Response({"message": "User status changed"}, status=status.HTTP_200_OK)
        
        except Account.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

class RegisterFreelancerView(APIView):

    def post(self, request, user_id):
        try:
            instance = FreelancerProfile.objects.get(freelancer_id=user_id)
            instance.is_registered = True
            instance.save()

            return Response({"message": "Freelancer Registered"}, status=status.HTTP_200_OK)
        
        except Account.DoesNotExist:
            return Response({"message": "Freelancer not found"}, status=status.HTTP_404_NOT_FOUND)
        

class AddCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            category = serializer.save(is_active=True)
            return Response({"message": "Category created successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BlockUnBlockCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, cat_id):
        try:
            instance = Category.objects.get(id=cat_id)
            instance.is_active = not instance.is_active
            instance.save()

            return Response({"message": "Category status changed"}, status=status.HTTP_200_OK)
        
        except Category.DoesNotExist:
            return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
