from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    id=models.IntegerField(primary_key=True)
    author=models.ForeignKey(to='auth.user', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date=timezone.now()
        self.save()
    
    def __str__(self):
        return self.title