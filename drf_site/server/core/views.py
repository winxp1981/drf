from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

@api_view()
def null_view(request):
    print ('hello')
    return Response(status=status.HTTP_400_BAD_REQUEST)
