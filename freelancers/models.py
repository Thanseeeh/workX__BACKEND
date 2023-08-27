from django.db import models
from accounts.models import Account

# Create your models here.


class FreelancerProfile(models.Model):

    FREELANCER_STATUS = [
        ('fresher', 'fresher'),
        ('intermediate', 'intermediate'),
        ('professional', 'professional')
    ]
    freelancer = models.ForeignKey(Account, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile', blank=True, null=True)
    title = models.CharField(max_length=20, blank=True)
    about = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True) 
    level = models.CharField(default='fresher', choices=FREELANCER_STATUS, max_length=20)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    year_of_experience = models.PositiveIntegerField(null=True, blank=True, default=0)
    age = models.PositiveIntegerField(blank=True, null=True)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.freelancer)
    

class FreelancerSkills(models.Model):
    skill = models.CharField(max_length=30, blank=True, unique=True)
    freelancer = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.skill)


class FreelancerExperience(models.Model):
    title = models.CharField(max_length=30, unique=True, blank=True)
    company = models.CharField(max_length=30, blank=True)
    year = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    freelancer = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
    

class FreelancerEducation(models.Model):
    course = models.CharField(max_length=30, unique=True, blank=True)
    college = models.CharField(max_length=30, blank=True)
    year = models.CharField(max_length=10, blank=True)
    freelancer = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)