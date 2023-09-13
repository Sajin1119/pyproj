from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phonenumber = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name




class Blogs(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(default='Default Description')
    authname = models.CharField(max_length=15)
    img = models.ImageField(upload_to='blog', blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Internship(models.Model):
    fullname=models.CharField( max_length=50)
    usn=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    collegename=models.CharField(max_length=50) 
    offer_status=models.CharField(max_length=50)
    start_date=models.CharField(max_length=50)
    end_date=models.CharField(max_length=50)
    proj_report=models.CharField(max_length=50)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname