from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('executives/', views.executives, name='executives'),
   path('project_progress/', views.project_progress, name='project_progress'),
   path('project_needs/', views.project_needs, name='project_needs'),
   
]
