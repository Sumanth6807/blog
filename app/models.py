from django.db import models

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=50)
    mail=models.CharField(max_length=50)
    category=models.IntegerField()
    gender=models.TextField()

    def __str__(self):
        return self.name

class library(models.Model):
    booktitle=models.CharField(max_length=50)
    studentname=models.CharField(max_length=50)
    studentid=models.IntegerField()
    publicationid=models.IntegerField()
    author=models.ForeignKey(author,on_delete=models.CASCADE)

    def __str__(self):
        return self.studentname


