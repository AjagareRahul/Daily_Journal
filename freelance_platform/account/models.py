from django.db import models
from django.contrib.auth.models import User

# Profile model - links to built-in Django User model
class Profile(models.Model):
    # One-to-one relationship with Django's User model
    # on_delete=CASCADE means if User is deleted, Profile is also deleted
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    # Short biography text field (optional)
    bio=models.TextField()
    # Skills as a string field (max 200 characters)
    skills=models.CharField(max_length=200)
    
    # String representation of the profile (shown in admin panel)
    def __str__(self):
        return self.user.username
    