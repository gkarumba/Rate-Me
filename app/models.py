from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profiles(models.Model):
    image = models.ImageField(blank=True,)
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
    