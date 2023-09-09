from django.urls import path
from .views import (
    UserProfileView, 
    UserProfileListView, 
    CategoryListView, 
    GigsListView, 
    LocationListView, 
    SkillsListView, 
    AuthenticatedUserProfile,
    GigDetailView,
    FreelancerDetailView,
    FreelancerSkillDetailView,
    FreelancerEducationDetailView,
    FreelancerExperienceDetailView,
    FreelancerGigDetailView,
    )

urlpatterns = [
    path('user-createprofile/', UserProfileView.as_view(), name='create-user-profile'),
    path('user-createprofile/<int:id>/', UserProfileView.as_view(), name='update-user-profile'),
    path('user-profiles/', UserProfileListView.as_view(), name='user-profile-list'),
    path('user-profile/', AuthenticatedUserProfile.as_view(), name='user-profile'),
    path('user-categories/', CategoryListView.as_view(), name='categories'),
    path('user-gigs/', GigsListView.as_view(), name='gigs'),
    path('user-locations/', LocationListView.as_view(), name='locations'),
    path('user-skills/', SkillsListView.as_view(), name='skills'),
    path('user-gigs/<int:id>/', GigDetailView.as_view(), name='gig-detail'),
    path('user-freelancer/<int:gig_owner_id>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('user-freelancer-skill/<int:gig_owner_id>/', FreelancerSkillDetailView.as_view(), name='freelancer-skilldetail'),
    path('user-freelancer-education/<int:gig_owner_id>/', FreelancerEducationDetailView.as_view(), name='freelancer-educationdetail'),
    path('user-freelancer-experience/<int:gig_owner_id>/', FreelancerExperienceDetailView.as_view(), name='freelancer-experiencedetail'),
    path('user-freelancer-gig/<int:gig_owner_id>/', FreelancerGigDetailView.as_view(), name='freelancer-gigdetail'),
]
