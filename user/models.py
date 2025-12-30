from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # AbstractUser already has username, email, password, etc.
    # Add any custom fields here if needed
    
    def __str__(self):
        return self.username
    
