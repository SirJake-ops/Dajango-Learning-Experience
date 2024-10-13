from django.db import models
from .Base import BaseEntity


class ApplicationUser(BaseEntity):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        data = {
            "username": self.username,
            "user_email": self.user_email,
            "password": self.password,
            "user_type": self.user_type,
        }




