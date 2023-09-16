from decimal import Decimal
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from accounts.models import Account
from users.models import GigsOrder
from users.serializers import GigsOrderListSerializer
from .models import FreelancerProfile, FreelancerSkills, FreelancerExperience, FreelancerEducation, FreelancerGigs
from .serializers import (
    FreelancerProfileSerializer, 
    FreelancerProfileListSerializer, 
    FreelancerSkillSerializer, 
    FreelancerExperienceSerializer, 
    FreelancerEducationSerializer, 
    GigsSerializer,
    )



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



class AddFreelancerEducation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = FreelancerEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FreelancerEducationList(APIView):
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
        


class AddGigs(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = GigsSerializer(data=request.data)
        if serializer.is_valid():
            gig = serializer.save(freelancer=request.user)

            if 'images1' in request.FILES:
                gig.image1 = request.FILES['images1']
            if 'images2' in request.FILES:
                gig.image2 = request.FILES['images2']
            if 'images3' in request.FILES:
                gig.image3 = request.FILES['images3']
            
            gig.is_active = True
            gig.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class GigsList(APIView):
    def get(self, request, *args, **kwargs):
        try:
            gigs = FreelancerGigs.objects.filter(freelancer=request.user)
            serializer = GigsSerializer(gigs, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Gigs not found'}, status=status.HTTP_404_NOT_FOUND)
        


class UpdateGigs(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, gigs_id):
        try:
            gigs = get_object_or_404(FreelancerGigs, pk=gigs_id, freelancer=request.user)
            gigs.delete()
            return Response({'message': 'Gigs deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except FreelancerGigs.DoesNotExist:
            return Response({'message': 'Gigs not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Failed to delete Gigs'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class BlockUnBlockGigsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, gig_id):
        try:
            instance = FreelancerGigs.objects.get(id=gig_id)
            instance.is_active = not instance.is_active
            instance.save()

            return Response({"message": "Gig status changed"}, status=status.HTTP_200_OK)
        
        except FreelancerGigs.DoesNotExist:
            return Response({"message": "Gig not found"}, status=status.HTTP_404_NOT_FOUND)
        


class FreelancerGigsOrderListView(APIView):
    def get(self, request):
        try:
            orders = GigsOrder.objects.filter(freelancer=request.user)
            serializer = GigsOrderListSerializer(orders, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        


class FreelancerAcceptOrderView(APIView):
    def put(self, request, order_id):
        try:
            order = GigsOrder.objects.get(id=order_id)
            order.status = 'Accepted'
            order.save()

            serializer = GigsOrderListSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except GigsOrder.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        


class FreelancerStartWorkView(APIView):
    def put(self, request, order_id):
        try:
            order = GigsOrder.objects.get(id=order_id)
            order.status = 'Work Started'
            order.save()

            serializer = GigsOrderListSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except GigsOrder.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        


class FreelancerCompleteWorkView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, order_id):
        try:
            order = GigsOrder.objects.get(id=order_id, freelancer=request.user)
            
            new_amount = Decimal(request.data.get('new_amount', order.new_amount))
            commission_percentage = Decimal('0.035')
            commission = commission_percentage * new_amount
            total_amount = new_amount + commission

            order.new_amount = request.data.get('new_amount', order.new_amount)
            order.total_amount = total_amount
            order.order_raw_images = request.data.get('order_raw_images', order.order_raw_images)
            order.status = 'Completed'
            order.save()

            serializer = GigsOrderListSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except GigsOrder.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)