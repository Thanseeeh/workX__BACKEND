from django.urls import path
from .views import (
    FreelancerProfileView, 
    FreelancerProfileListView, 
    AuthenticatedFreelancerProfile, 
    AddFreelancerSkill, 
    FreelancerSkillsList, 
    UpdateFreelancerSkill, 
    AddFreelancerExperience, 
    FreelancerExperienceList, 
    UpdateFreelancerExperience,
    AddFreelancerEducation,
    FreelancerEducationList,
    UpdateFreelancerEducation,
    )

urlpatterns = [
    path('freelancer-createprofile/', FreelancerProfileView.as_view(), name='create-freelancer-profile'),
    path('freelancer-createprofile/<int:id>/', FreelancerProfileView.as_view(), name='update-freelancer-profile'),
    path('freelancer-profiles/', FreelancerProfileListView.as_view(), name='freelancer-profile-list'),
    path('freelancer-profile/', AuthenticatedFreelancerProfile.as_view(), name='freelancer-profile'),
    path('freelancer-addskill/', AddFreelancerSkill.as_view(), name='freelancer-addskill'),
    path('freelancer-skills/', FreelancerSkillsList.as_view(), name='freelancer-skills'),
    path('freelancer-skills/update/<int:skill_id>/', UpdateFreelancerSkill.as_view(), name='update_freelancer_skill'),
    path('freelancer-addexperience/', AddFreelancerExperience.as_view(), name='freelancer-addexperience'),
    path('freelancer-experience/', FreelancerExperienceList.as_view(), name='freelancer-experience'),
    path('freelancer-experience/update/<int:experience_id>/', UpdateFreelancerExperience.as_view(), name='update_freelancer_experience'),
    path('freelancer-addeducation/', AddFreelancerEducation.as_view(), name='freelancer-addeducation'),
    path('freelancer-education/', FreelancerEducationList.as_view(), name='freelancer-education'),
    path('freelancer-education/update/<int:education_id>/', UpdateFreelancerEducation.as_view(), name='update_freelancer_education'),
]
