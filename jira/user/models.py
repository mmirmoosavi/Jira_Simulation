from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    # Add other user-related fields

    def __str__(self):
        return self.user_name