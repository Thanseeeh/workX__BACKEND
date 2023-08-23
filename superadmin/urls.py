from django.urls import path
from .views import BlockUnBlockUserView, BlockUnBlockFreelancerView, RegisterFreelancerView

urlpatterns = [
    path('block-unblock-user/<int:user_id>/', BlockUnBlockUserView.as_view(), name='block-unblock-user'),
    path('block-unblock-freelancer/<int:user_id>/', BlockUnBlockFreelancerView.as_view(), name='block-unblock-freelancer'),
    path('register-freelancer/<int:user_id>/', RegisterFreelancerView.as_view(), name='register-freelancer'),
]