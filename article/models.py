from django.db import models

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=3000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title