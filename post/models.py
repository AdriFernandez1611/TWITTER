from django.db import models

# Create your models here.

class Post(models.Model):
    titulo= models.CharField(max_length=40)
    descripcion= models.TextField()
    #imagen= models.ImageField(upload_to="media", blank=True, null=True)
    autor= models.ForeignKey("auth.User", on_delete= models.CASCADE, blank=True)
    
    