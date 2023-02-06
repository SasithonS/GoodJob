from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.signup, name='signup'),
    path('signup_emp', views.signup_emp, name='signup_emp'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('jobber_profile/<int:id>', views.jobber_profile, name='jobber_profile'),
    path('jobber_check/<int:id>', views.jobber_check, name='jobber_check'),
    path('emp_check/<int:id>', views.emp_check, name='emp_check'),
    path('jobber_update/<int:id>', views.jobber_update, name='jobber_update'),
    path('emp_profile/<int:id>', views.emp_profile, name='emp_profile'),
    path('emp_update/<int:id>', views.emp_update, name='emp_update'),
    path('admin_profile/<int:id>', views.admin_profile, name='admin_profile'),
    path('admin_update/<int:id>', views.admin_update, name='admin_update'),
]