from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name



class PostModel(models.Model):
    title = models.CharField(max_length=255)
    head_image = models.ImageField(upload_to="upload/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text =RichTextField(blank=True,null=True)
    postdate = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.title + '|' + str( self.user) 


    def get_absolute_url(self):
        return reverse("home")
        