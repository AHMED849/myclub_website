from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login_user/', views.login_user, name="login_user"),
    path('register_user/', views.register_user, name="register_user"),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('update_profile/', views.update_profile, name='update_profile'),  
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
  

