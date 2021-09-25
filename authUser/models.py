from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    auth_token = models.CharField(max_length=100)
    is_varified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tokens = models.CharField(max_length=500, default='AAPL,')

    def __str__(self):
        return self.user.username