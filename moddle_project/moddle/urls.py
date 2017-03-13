from django.conf.urls import include, url
from moddle import views

# mapping url to different django appilcation.
# This means the url mapping in the template should be referred to the app_name.
# E.g. {% url 'rango:about' %}
#app_name='rango'


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^about/$', views.about, name='about'),
    #url(r'^contact_us/$', views.contact_us, name='contact_us'),
    #url(r'^faq/$', views.faq, name='faq'),
    #url(r'^search/$', views.search, name='search'), 
    #url(r'^bike/(?P<bike_id_slug>[\w\-]+)/$', views.bike_profile, name='bike_profile'),
    #url(r'^(?P<user_name_slug>[\w\-]+)/$', views.index, name='user_profile'),
    #url(r'^(?P<user_name_slug>[\w\-]+)/mybookings/$', views.view_bookings, name='view_bookings'),
    #url(r'^(?P<user_name_slug>[\w\-]+)/addbike/$', views.upload_bike, name='upload_bike'),
    #url(r'^(?P<bike_id_slug>[\w\-]+)/request/$', views.request_bike, name='request_bike'),
]