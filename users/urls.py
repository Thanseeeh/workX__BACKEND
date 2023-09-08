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
]
