from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(upload_to="myfile")
    title=models.CharField(max_length=70)
    date= models.DateField(auto_now_add=True)