from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profiles(models.Model):
    image = models.ImageField(upload_to='images/',default='DEFAULT VALUE')
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    contact = models.IntegerField()
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    @classmethod
    def get_profile_by_name(cls,name):
        profile = Profiles.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def filter_profile_by_id(cls,id):
        profile = Profiles.objects.filter(user = id).first()
        return profile
    
    @classmethod
    def get_profile_by_id(cls,id):
        profile = Profiles.objects.get(user = id)
        return profile
    
class Projects(models.Model):
    image = models.ImageField(upload_to='images/',default='DEFAULT VALUE')
    details = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    posted = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('-posted',)
    
    def save_project(self):
        self.save()
        
    def delete_project(self):
        self.delete()
    
    @classmethod
    def get_project_by_id(cls,id):
        project = Projects.objects.get(pk=id)
        return project
    
    @classmethod
    def get_profile_projects(cls,profile):
        projects = Projects.object.filter(profile__pk = profile)
        return projects
    
    @classmethod
    def get_all_projects(cls):
        projects = Projects.objects.all()
        return projects
        
class Reviews(models.Model):
    review = models.CharField(max_length=150)
    posted = models.DateField(auto_now=True)
    rate = models.IntegerField()
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_review(self):
        self.save()
        
    def delete_comments(self):
        self.delete()
        
    @classmethod
    def get_review_by_image(cls,id):
        review = Review.objects.filter(image__pk = id)
        return review

class RatemeLetterRecipients(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()