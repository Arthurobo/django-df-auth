"""URLs module"""
from django.conf import settings
from django.urls import re_path as url 
from .views import exchange_token#, SocialSignUp

from social_core.utils import setting_name
from social_django import views


extra = getattr(settings, setting_name('TRAILING_SLASH'), True) and '/' or ''

app_name = 'social'

urlpatterns = [
    # authentication / association
    url(r'^signin/(?P<backend>[^/]+){0}$'.format(extra), views.auth,
        name='begin'),
    url(r'^connect/(?P<backend>[^/]+){0}$'.format(extra), views.complete,
        name='complete'),
    # disconnection
    # url(r'^disconnect/(?P<backend>[^/]+){0}$'.format(extra), views.disconnect,
    #     name='disconnect'),
    # url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>\d+){0}$'
    #     .format(extra), views.disconnect, name='disconnect_individual'),

    # Url to get tokens
    url(r'social/(?P<backend>[^/]+)/$', exchange_token,),
    
]