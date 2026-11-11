from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.reviewerSignUp, name='signup'),
    path('login/', views.reviewerLogin, name='login'),
    path('home/', views.reviewerHome, name='reviewerHome'),
    path('logout/', views.logoutUser, name='logout'),
]