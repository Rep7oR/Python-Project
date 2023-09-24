from django.db import models

# Create your models here.
class table(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class team(models.Model):
    name=models.CharField(max_length=15)
    img=models.ImageField(upload_to='team_pic')
    desc=models.TextField()

    def __str__(self):
        return self.name
