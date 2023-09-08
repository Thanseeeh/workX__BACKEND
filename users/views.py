from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from .models import UserProfile
from .serializers import UserProfileSerializer, UserProfileListSerializer, GigsListingSerializer, GigDetailSerializer
from superadmin.models import Category
from superadmin.serializers import CategorySerializer
from freelancers.models import FreelancerGigs, FreelancerProfile, FreelancerSkills
from freelancers.serializers import GigsSerializer


# UserProfile
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({'message': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            profile = UserProfile.objects.get(user=request.user)
            user = Account.objects.get(email = request.user)
            user.is_profile = True
            user.save()
        except UserProfile.DoesNotExist:
            return Response({'message': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# UserProfileListing
class UserProfileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profiles = UserProfile.objects.all()
        serializer = UserProfileListSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# UserProfileDetails
class AuthenticatedUserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = UserProfile.objects.get(user=request.user)
            serializer = UserProfileListSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({'message': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
    

# CategoryListing
class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# GigsListing
class GigsListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            gigs = FreelancerGigs.objects.all()
            serializer = GigsListingSerializer(gigs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Gigs not found'}, status=status.HTTP_404_NOT_FOUND)
        

# LocationListing
class LocationListView(APIView):
    def get(self, request, format=None):
        try:
            unique_states = FreelancerProfile.objects.values_list('state', flat=True).distinct()
            return Response({'states': list(unique_states)}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# SkillsListing
class SkillsListView(APIView):
    def get(self, request, format=None):
        try:
            unique_skills = FreelancerSkills.objects.values_list('skill', flat=True).distinct()
            return Response({'skills': list(unique_skills)}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# SingleViewOfGigs
class GigDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            gig = FreelancerGigs.objects.get(id=id)
            serializer = GigDetailSerializer(gig)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FreelancerGigs.DoesNotExist:
            return Response({'message': 'Gig not found'}, status=status.HTTP_404_NOT_FOUND)