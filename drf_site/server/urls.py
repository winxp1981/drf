"""drf_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from room.views import RoomViewSet, TaskViewSet, RoomImageViewSet
from userprofiles.views import UserViewSet #, ProfileViewSet
from core.views import FacebookLogin
from core.views import GoogleLogin
from core.views import null_view
from allauth.account.views import confirm_email as allauthemailconfirmation

router = DefaultRouter()
router.register(prefix='rooms', viewset=RoomViewSet, base_name='room_detail')
router.register(prefix='roomsimage', viewset=RoomImageViewSet)
router.register(prefix='user', viewset=UserViewSet)   # redirect user info rest api url to /user
#router.register(prefix='profile', viewset=ProfileViewSet)
router.register(r'tasks', TaskViewSet, base_name='tasks')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
]


''' temporary for media url '''
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
