"""moddle_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from moddle import views
from django.conf.urls.static import static

#Attempt to make a RESTful API for the map page
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'coords', views.CoordinatesViewSet)
router.register(r'bikes', views.BikeViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^faq/$', views.faq, name='faq'),
    
    #Attempt to make a RESTful API for the map page
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^map/$', views.map, name='map'),
    
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),	
    # url for transmitting user lat-long info to database
    url(r'^storelatlong/$', views.storelatlong, name='storelatlong'),	
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>[\w\-]+)/$', views.user_profile, name='user_profile'),
    url(r'^(?P<username>[\w\-]+)/mybookings/$', views.view_bookings, name='view_bookings'),
    url(r'^(?P<username>[\w\-]+)/addbike/$', views.upload_bike, name='upload_bike'),
    url(r'^bike/(?P<bike_id_slug>[\w\-]+)/$', views.bike_profile, name='bike_profile'),
    url(r'^bike/(?P<bike_id_slug>[\w\-]+)/delete/$', views.delete_bike, name='delete_bike'),
    url(r'^booking/(?P<booking_id>[\w\-]+)/approve/$', views.approve_booking, name='approve_booking'),
    url(r'^booking/(?P<booking_id>[\w\-]+)/reject/$', views.reject_booking, name='reject_booking'),
    url(r'^booking/(?P<booking_id>[\w\-]+)/delete/$', views.delete_booking, name='delete_booking'),
    url(r'^(?P<bike_id_slug>[\w\-]+)/request/$', views.request_bike, name='request_bike'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
