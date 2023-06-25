from django.db import models

# Create your models here.
class HeadLine(models.Model):
    title = models.CharField(max_length=250)
    image = models.URLField(null=True,blank=True)
    url = models.TextField()
    
    def __str__(self):
        return self.title