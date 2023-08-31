from rest_framework import serializers
from accounts.models import Account
from accounts.serializers import UserViewSerializer
from .models import FreelancerProfile, FreelancerSkills, FreelancerExperience, FreelancerEducation, FreelancerGigs, Image



class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'is_verified', 'is_active']


class FreelancerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerProfile
        exclude = ('freelancer',)


class FreelancerProfileListSerializer(serializers.ModelSerializer):
    freelancer = FreelancerSerializer()

    class Meta:
        model = FreelancerProfile
        fields = '__all__'


class FreelancerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerSkills
        fields = '__all__'


class FreelancerEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerEducation
        fields = '__all__'


class FreelancerExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerExperience
        fields = '__all__'


class GigImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', )


class GigsSerializer(serializers.ModelSerializer):
    gig_images = serializers.SerializerMethodField()

    class Meta:
        model = FreelancerGigs
        fields = '__all__'

    def get_gig_images(self, obj):
        images = Image.objects.filter(gig=obj)
        serializer = GigImageSerializer(instance=images, many=True)
        return serializer.data