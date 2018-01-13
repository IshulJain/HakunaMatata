from django.conf.urls import url
from views import *


app_name = 'home'

urlpatterns = [
	url(r'^ad/$', postAd, name='postAd'),
	url(r'^search/$', search, name='search'),
	url(r'^wishlist/(?P<ad_id>[0-9]+)/$', wishlist, name='wishlist'),
	
]