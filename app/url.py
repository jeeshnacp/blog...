
from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('login', views.login_view, name='login'),
    path('signup',views.user_register,name='signup'),
    path('user_home',views.user_home,name='user_home'),
    path('logout',views.logout_view,name='logout'),
    path('viewuser',views.view_user,name='viewuser'),

]