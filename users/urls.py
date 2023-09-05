from django.urls import path
from .views import UserProfileView, UserProfileListView, CategoryListView, GigsListView, LocationListView

urlpatterns = [
    path('user-createprofile/', UserProfileView.as_view(), name='create-freelancer-profile'),
    path('user-createprofile/<int:id>/', UserProfileView.as_view(), name='update-freelancer-profile'),
    path('user-profiles/', UserProfileListView.as_view(), name='freelancer-profile-list'),
    path('user-categories/', CategoryListView.as_view(), name='categories'),
    path('user-gigs/', GigsListView.as_view(), name='gigs'),
    path('user-locations/', LocationListView.as_view(), name='locations')
]
