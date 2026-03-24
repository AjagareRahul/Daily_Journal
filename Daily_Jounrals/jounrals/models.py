from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    choose_moods=[
         ('happy', '😊 Happy'),
        ('neutral', '😐 Neutral'),
        ('sad', '😢 Sad'),
        
    ]
    title=models.CharField(max_length=200)
    mood = models.CharField(max_length=10, choices=choose_moods)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title