from django.db import models

# Create your models here.
class JournalEntry(models.Model):
    CHOOSE_CHOICES=[
        ('HAPPY','😃HAPPY'),
        ('NATURAL','😐NATURAL'),
        ('SAD','😢SAD'),
    ]
    title=models.CharField(max_length=200)
    mood=models.CharField(max_length=200,choices=CHOOSE_CHOICES)
    description=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title   