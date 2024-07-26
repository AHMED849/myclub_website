from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import mpesa_callback


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('finances/', views.finances, name='finances'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-failure/', views.payment_failure, name='payment_failure'),
    path('tasks/', views.tasks, name='tasks'),
    path('settings/', views.settings, name='settings'),  
    path('help/', views.help, name='help'),
    path('mpesa_callback/', views.mpesa_callback, name='mpesa_callback'),
    path('initiate_stk_push/', views.initiate_stk_push, name='initiate_stk_push'),
    path('accesstoken/', views.get_access_token, name='get_access_token'),

]