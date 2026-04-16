from django.urls import path
from Journals.views import home, create_journals,update_journal,delete_entry,registration,user_login,logout
urlpatterns=[
        path('',user_login,name='login'), 
    path('registration/',registration,name='registration'),   
    path('logout/',logout,name="logout"),
    path('home/',home,name='home'),
    path('create/',create_journals,name='create_journals'),
    path('update_journal/<int:id>',update_journal,name='update_journal'),
    path('delete/<int:id>',delete_entry,name='delete_entry'),
  
]