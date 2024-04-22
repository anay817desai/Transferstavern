from django.db import models
# Create your models here.
class Transferstavern(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(max_length=250)
    image_url = models.TextField(blank=True, null=True)
    
    

    def __str__(self):

        return self.title + " "