from rest_framework import serializers
from accounts.models import Account
from accounts.serializers import UserViewSerializer
from .models import FreelancerProfile



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