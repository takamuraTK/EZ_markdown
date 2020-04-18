from django.db import models
from django.utils import timezone

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=3000)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title