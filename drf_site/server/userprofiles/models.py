from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=50, blank=True)
    mobile_no = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar_url = models.CharField(default='http://www.gravatar.com/avatar?d=mm', max_length=200, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            print ("create_user_profile: %s" % instance)
            Profile.objects.create(user=instance,
                                   nick_name=instance.first_name+' '+instance.last_name,
                                   )

    @receiver(user_signed_up)
    def new_user_signup(sender, **kwargs):
        _user = kwargs['user']
        print ('-- social signed up: %s' % _user)

        social_user = SocialAccount.objects.get(user_id=_user.id)

        profile_picture_url ='http://www.gravatar.com/avatar?d=mm'

        if social_user.provider == 'facebook':
            profile_picture_url = 'https://graph.facebook.com/'+ social_user.uid +'/picture?width=50&height=50'
        elif social_user.provider == 'google':
            profile_picture_url = social_user.extra_data['picture']

        _user.profile.avatar_url = profile_picture_url
        _user.profile.update_fields=["avatar_url"]


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
