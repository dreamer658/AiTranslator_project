from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_video, name = 'upload_video') 
    #'upload/' is the url pattern to match, upload video is the view function to call
]

