from django.urls import path
# Import all views from account app (home, create_profile, update_profile, my_profile)
from account.views import *

# URL patterns for the account app
urlpatterns=[
    # Home page - displays all profiles (empty string = root URL)
    path('',home,name='home'),
    # Create profile page (redirects to update if profile exists)
    path('create_profile/',create_profile,name='create_profile'),
    # Update profile page - expects integer id parameter
    path('update_profile/<int:id>',update_profile,name='update_profile'),
    # My profile - redirects to update or create based on profile existence
    path('my_profile/',my_profile,name='my_profile'),
]