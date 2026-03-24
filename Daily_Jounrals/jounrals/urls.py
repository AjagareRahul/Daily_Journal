from django.urls import path
from jounrals.views import *
urlpatterns = [
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
