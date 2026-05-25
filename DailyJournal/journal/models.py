from django.db import models

# Create your models here.

class Journal(models.Model):
    MOOD_CHOICES=[
        ('happy','Happy'),
        ('sad','Sad'),
        ('excited','Excited'),
        ('angry','Angry'),
    ]
    
    title=models.CharField(max_length=100)
    content=models.TextField()
    mood=models.CharField(max_length=20,choices=MOOD_CHOICES)
    date=models.DateField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title
    