from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from accounts.models import Account
from .models import FreelancerProfile, FreelancerSkills, FreelancerExperience, FreelancerEducation
from rest_framework.generics import RetrieveAPIView
from .serializers import FreelancerProfileSerializer, FreelancerProfileListSerializer, FreelancerSkillSerializer, FreelancerExperienceSerializer, FreelancerEducationSerializer



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
    


class AuthenticatedFreelancerProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = FreelancerProfile.objects.get(freelancer=request.user)
            serializer = FreelancerProfileListSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FreelancerProfile.DoesNotExist:
            return Response({'message': 'Freelancer profile not found'}, status=status.HTTP_404_NOT_FOUND)
        


class AddFreelancerSkill(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = FreelancerSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FreelancerSkillsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            skills = FreelancerSkills.objects.filter(freelancer=request.user)
            serializer = FreelancerSkillSerializer(skills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Skills not found'}, status=status.HTTP_404_NOT_FOUND)
        


class UpdateFreelancerSkill(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, skill_id):
        try:
            skill = get_object_or_404(FreelancerSkills, pk=skill_id, freelancer=request.user)
            skill.delete()
            return Response({'message': 'Skill deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except FreelancerSkills.DoesNotExist:
            return Response({'message': 'Skill not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Failed to delete skill'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class AddFreelancerExperience(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = FreelancerExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FreelancerExperienceList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            experience = FreelancerExperience.objects.filter(freelancer=request.user)
            serializer = FreelancerExperienceSerializer(experience, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Experience not found'}, status=status.HTTP_404_NOT_FOUND)
        


class UpdateFreelancerExperience(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, experience_id):
        try:
            experience = get_object_or_404(FreelancerExperience, pk=experience_id, freelancer=request.user)
            experience.delete()
            return Response({'message': 'Experience deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except FreelancerExperience.DoesNotExist:
            return Response({'message': 'Experience not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Failed to delete Experience'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class AddFreelancerEducation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = FreelancerEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FreelancerEducation(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            education = FreelancerEducation.objects.filter(freelancer=request.user)
            serializer = FreelancerEducationSerializer(education, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Education not found'}, status=status.HTTP_404_NOT_FOUND)
        


class UpdateFreelancerEducation(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, education_id):
        try:
            education = get_object_or_404(FreelancerEducation, pk=education_id, freelancer=request.user)
            education.delete()
            return Response({'message': 'Education deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except FreelancerEducation.DoesNotExist:
            return Response({'message': 'Education not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Failed to delete Education'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)