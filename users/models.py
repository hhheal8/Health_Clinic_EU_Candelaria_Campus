from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class EucUsers(AbstractUser):

  ROLE_CHOICES = (
    ("admin", "Admin"),
    ("student", "Student")
  )
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False, blank=False)

  def __str__(self):
    return self.username