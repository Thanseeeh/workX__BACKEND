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
    AddGigs,
    GigsList,
    UpdateGigs,
    BlockUnBlockGigsView,
    FreelancerGigsOrderListView,
    FreelancerAcceptOrderView,
    FreelancerStartWorkView,
    FreelancerCompleteWorkView,
    FreelancerCloseDealView,
    TotalAmountEarningView,
    GigsCount,
    )

urlpatterns = [
    path('freelancer-createprofile/', FreelancerProfileView.as_view(), name='create-freelancer-profile'),
    path('freelancer-createprofile/<int:id>/', FreelancerProfileView.as_view(), name='update-freelancer-profile'),
    path('freelancer-profiles/', FreelancerProfileListView.as_view(), name='freelancer-profile-list'),
    path('freelancer-profile/', AuthenticatedFreelancerProfile.as_view(), name='freelancer-profile'),
    path('freelancer-addskill/', AddFreelancerSkill.as_view(), name='freelancer-addskill'),
    path('freelancer-skills/', FreelancerSkillsList.as_view(), name='freelancer-skills'),
    path('freelancer-skills/update/<int:skill_id>/', UpdateFreelancerSkill.as_view(), name='update_freelancer_skill'),
    path('freelancer-addeducation/', AddFreelancerEducation.as_view(), name='freelancer-addeducation'),
    path('freelancer-education/', FreelancerEducationList.as_view(), name='freelancer-education'),
    path('freelancer-education/update/<int:education_id>/', UpdateFreelancerEducation.as_view(), name='update_freelancer_education'),
    path('freelancer-addexperience/', AddFreelancerExperience.as_view(), name='freelancer-addexperience'),
    path('freelancer-experience/', FreelancerExperienceList.as_view(), name='freelancer-experience'),
    path('freelancer-experience/update/<int:experience_id>/', UpdateFreelancerExperience.as_view(), name='update_freelancer_experience'),
    path('freelancer-addgigs/', AddGigs.as_view(), name='freelancer-addgigs'),
    path('freelancer-gigs/', GigsList.as_view(), name='freelancer-gigs'),
    path('freelancer-gigs/update/<int:gigs_id>/', UpdateGigs.as_view(), name='update_freelancer_gigs'),
    path('block-unblock-gigs/<int:gig_id>/', BlockUnBlockGigsView.as_view(), name='block-unblock-gig_id'),
    path('freelancer-orderslist/', FreelancerGigsOrderListView.as_view(), name='freelancer-list-order'),
    path('freelancer-acceptorder/<int:order_id>/', FreelancerAcceptOrderView.as_view(), name='accept-order'),
    path('freelancer-startwork/<int:order_id>/', FreelancerStartWorkView.as_view(), name='start-work'),
    path('freelancer-complete-work/<int:order_id>/', FreelancerCompleteWorkView.as_view(), name='complete-work'),
    path('freelancer-close-deal/<int:order_id>/', FreelancerCloseDealView.as_view(), name='close-deal'),
    path('freelancer-totalamount/', TotalAmountEarningView.as_view(), name='total-amount-earnings'),
    path('freelancer-gigs-count/', GigsCount.as_view(), name='gigs-count'),
]
