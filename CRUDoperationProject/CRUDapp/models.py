from django.db import models

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "users"

