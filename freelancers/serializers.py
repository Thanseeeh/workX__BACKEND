from rest_framework import serializers
from accounts.serializers import UserViewSerializer
from .models import FreelancerProfile


class FreelancerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerProfile
        exclude = ('freelancer',)