""" from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('accounts/login/', views.login_view, name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] """
