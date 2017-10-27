from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from allauth.account.signals import user_signed_up, user_logged_in
from allauth.socialaccount.signals import social_account_updated, social_account_added
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
        #    print ("create_user_profile: %s %s" % (instance, instance.id))
            Profile.objects.create(user=instance,
                                   nick_name=instance.first_name+' '+instance.last_name,
                                   )

    @receiver(post_save, sender=SocialAccount)
    def create_user(sender, instance, created, **kwargs):
        if created:
            _user = User.objects.get(id=instance.user_id)
            print ("create_social_user: %s %s %s" % (instance, instance.id, _user.id))
            profile_picture_url ='http://www.gravatar.com/avatar?d=mm'

            if instance.provider == 'facebook':
                profile_picture_url = 'https://graph.facebook.com/'+ instance.uid +'/picture?width=100&height=100'
            elif instance.provider == 'google':
                profile_picture_url = instance.extra_data['picture']

            _user.profile.avatar_url = profile_picture_url
            _user.profile.update_fields=["avatar_url"]
            _user.profile.save()


'''
    # see allauth/socialaccount/helpers.py
    @receiver(social_account_added)
    def user_added(sociallogin, **kwargs):
        print ('--- social added: %s' % sociallogin.user.id)

    @receiver(social_account_updated)
    def user_updated(sociallogin, **kwargs):
        print ('--- social signed up: %s' % sociallogin.user.id)
'''
'''
    #@receiver(user_logged_in)
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
'''
