from rest_framework import serializers
from accounts.models import Account
from accounts.serializers import UserViewSerializer
from superadmin.serializers import CategorySerializer
from freelancers.serializers import FreelancerSerializer
from freelancers.models import FreelancerGigs, FreelancerProfile
from .models import UserProfile


# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'is_verified', 'is_active']


# UserProfile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('user',)


# UserProfileListing
class UserProfileListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'


# GigsListing
class GigsListingSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    freelancer = FreelancerSerializer()
    class Meta:
        model = FreelancerGigs
        fields = '__all__'


# GigSingleView
class GigDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    freelancer = FreelancerSerializer()
    freelancer_profile_photo = serializers.SerializerMethodField()

    class Meta:
        model = FreelancerGigs
        fields = '__all__'

    def get_freelancer_profile_photo(self, obj):
        try:
            freelancer_profile = FreelancerProfile.objects.get(freelancer=obj.freelancer)
            return freelancer_profile.profile_photo.url
        except FreelancerProfile.DoesNotExist:
            return None
