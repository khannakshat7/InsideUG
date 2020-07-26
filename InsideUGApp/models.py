from django.db import models

# Create your models here.

class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    stream = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    discription = models.TextField()
    smallImage = models.FileField(upload_to='coursesmall/')
    BigImage = models.FileField(upload_to='coursebig/')

    def __str__(self):
        return self.title