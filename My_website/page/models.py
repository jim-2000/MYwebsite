from django.db import models

# Create your models here.
class services(models.Model):
    title = models.CharField(max_length=28)
    abouth = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.title
    
class massage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 100)
    subjects = models.CharField(max_length = 20, blank=True)
    mass = models.TextField()

    def __str__(self):
        return self.name
    
class footer_Massage(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 80)
    tolk = models.TextField()
    
    def __str__(self):
        return self.name
    
    