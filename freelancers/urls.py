from django.urls import path
from .views import FreelancerProfileView

urlpatterns = [
    path('freelancer-profile/', FreelancerProfileView.as_view(), name='create-freelancer-profile'),
    path('freelancer-profile/<int:id>/', FreelancerProfileView.as_view(), name='update-freelancer-profile'),
]
