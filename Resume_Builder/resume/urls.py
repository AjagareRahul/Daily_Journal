from resume.views import *
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('create/',create,name='create'),
]
