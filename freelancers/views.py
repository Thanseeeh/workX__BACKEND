from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from .models import FreelancerProfile
from .serializers import FreelancerProfileSerializer, FreelancerProfileListSerializer

class FreelancerProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        try:
            profile = FreelancerProfile.objects.get(freelancer=request.user)
            serializer = FreelancerProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FreelancerProfile.DoesNotExist:
            return Response({'message': 'Freelancer profile not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            profile, created = FreelancerProfile.objects.get_or_create(freelancer=request.user)
            user = Account.objects.get(email=request.user)
            user.is_profile = True
            user.save()
        except Exception as e:
            return Response({'message': 'Failed to create/update freelancer profile'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FreelancerProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            if 'profile_photo' in request.FILES:
                profile.profile_photo = request.FILES['profile_photo']

            serializer.save()
            return Response({'message': 'Created/Updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class FreelancerProfileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profiles = FreelancerProfile.objects.all()
        serializer = FreelancerProfileListSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
