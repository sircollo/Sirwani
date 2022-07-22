from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Projects(models.Model):
  name = models.CharField(max_length=50)
  title = models.CharField(max_length=50)
  description = models.TextField()
  image = CloudinaryField('Projects')
  preview = models.URLField(default=None)
  
  def __str__(self):
    return self.name
  
  
class FeedBack(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  message = models.TextField()
  date_sent = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name