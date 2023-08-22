from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from .models import UserProfile
from .serializers import UserProfileSerializer, UserProfileListSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(freelancer=request.user)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({'message': 'Freelancer profile not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(freelancer=request.user)
            user = Account.objects.get(email = request.user)
            user.is_profile = True
            user.save()
        except UserProfile.DoesNotExist:
            return Response({'message': 'Freelancer profile not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserProfileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profiles = UserProfile.objects.all()
        serializer = UserProfileListSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
