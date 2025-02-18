from django.db import models
from django.contrib.auth.models import User

class UserImages(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE) #binding
    face_image= models.ImageField(upload_to="User_faces/")
    
    def __str__(self):
        return self.user.username


