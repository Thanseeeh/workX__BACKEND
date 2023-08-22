from django.urls import path
from .views import FreelancerProfileView, FreelancerProfileListView

urlpatterns = [
    path('freelancer-createprofile/', FreelancerProfileView.as_view(), name='create-freelancer-profile'),
    path('freelancer-createprofile/<int:id>/', FreelancerProfileView.as_view(), name='update-freelancer-profile'),
    path('freelancer-profiles/', FreelancerProfileListView.as_view(), name='freelancer-profile-list'),
]
