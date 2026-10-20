from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signup/reviewer', views.reviewerSignUp, name='reviewerSignUp'),
    path('signup/blogger', views.bloggerSignUp, name='bloggerSignUp')
]