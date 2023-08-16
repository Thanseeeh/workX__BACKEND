from rest_framework import serializers
from accounts.serializers import UserViewSerializer
from .models import FreelancerProfile


class FreelancerProfileSerializer(serializers.ModelSerializer):
    freelancer = UserViewSerializer(read_only=True, many=False)

    # category = CompanyCategorySerializer(read_only=True, many=False)
    # department = CategoryDepartmentSerializer(read_only=True, many=False)

    class Meta:
        model = FreelancerProfile
        fields = '__all__'