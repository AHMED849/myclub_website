from django.contrib import admin
from django.urls import path, include
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),   
    path('members/', include('members.urls')),
    path('events/', include('events.urls')),
  
]

