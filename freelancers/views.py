from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from accounts.models import Account
from rest_framework import status, generics
from .models import FreelancerProfile
from .serializers import FreelancerProfileSerializer

# Create your views here.


class FreelancerProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)


    def get(self, request:Response):
        id = request.query_params['id']

        try:
            profile = FreelancerProfile.objects.get(id=id)
            serializer = FreelancerProfileSerializer(profile, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({'message': 'Data not found'}, status=status.HTTP_400_BAD_REQUEST)
        
    
    def put(self, request:Response):
        id = request.query_params['id']
        profile = FreelancerProfile.objects.get(id = id)
        serializer = FreelancerProfileSerializer(instance=profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': "updaded successfully"})
        else:
            return Response({'message':'Failed'})