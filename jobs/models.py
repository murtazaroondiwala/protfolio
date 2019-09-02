from django.db import models

# Create your models here.
class Job(models.Model):
    # title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length = 200, default='SOME STRING')
    period= models.CharField(max_length = 200, default='SOME STRING')
    summary = models.TextField(max_length = 1000)

    def __str__(self):
        return self.title

class Education(models.Model):
    edu_image = models.ImageField(upload_to='images/')
    edu_title = models.CharField(max_length = 200, default='SOME STRING')
    edu_period = models.CharField(max_length = 200, default='SOME STRING')

    def __str__(self):
        return self.edu_title

class Painting(models.Model):
    painting_image = models.ImageField(upload_to='images/')
    painting_title = models.CharField(max_length = 200, default='SOME STRING')

    def __str__(self):
        return self.painting_title