from django.urls import path
from .views import UserProfileView, UserProfileListView

urlpatterns = [
    path('user-createprofile/', UserProfileView.as_view(), name='create-freelancer-profile'),
    path('user-createprofile/<int:id>/', UserProfileView.as_view(), name='update-freelancer-profile'),
    path('user-profiles/', UserProfileListView.as_view(), name='freelancer-profile-list'),
]
