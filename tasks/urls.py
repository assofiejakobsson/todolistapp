from django.urls import path
from tasks import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('task_lists/create/', views.create_task_list, name='create_task_list'),
    path('create/', views.task_create, name='task_create'),
    path('task_lists/<int:task_list_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]
