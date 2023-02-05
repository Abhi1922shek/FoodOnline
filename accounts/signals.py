from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

# Django signals
# Decorators
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance) #creates user profile as soon as user is created
        
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            #create the userprofile if not exists
            UserProfile.objects.create(user=instance)   

# post_save.connect(post_save_create_profile_receiver, sender = User) one way of connecting to sender and receiver

# @receiver(pre_save, sender=User)
# def pre_save_profile_receiver(sender, instance, **kwargs):
#     print(instance.username , "this user is being saved")