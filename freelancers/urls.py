from django.urls import path
from .views import FreelancerProfileView, FreelancerProfileListView, AuthenticatedFreelancerProfile, AddFreelancerSkill, FreelancerSkillsList, UpdateFreelancerSkill

urlpatterns = [
    path('freelancer-createprofile/', FreelancerProfileView.as_view(), name='create-freelancer-profile'),
    path('freelancer-createprofile/<int:id>/', FreelancerProfileView.as_view(), name='update-freelancer-profile'),
    path('freelancer-profiles/', FreelancerProfileListView.as_view(), name='freelancer-profile-list'),
    path('freelancer-profile/', AuthenticatedFreelancerProfile.as_view(), name='freelancer-profile'),
    path('freelancer-addskill/', AddFreelancerSkill.as_view(), name='freelancer-addskill'),
    path('freelancer-skills/', FreelancerSkillsList.as_view(), name='freelancer-skills'),
    path('freelancer-skills/update/<int:skill_id>/', UpdateFreelancerSkill.as_view(), name='update_freelancer_skill'),
]
