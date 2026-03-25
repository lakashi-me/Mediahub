from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    USER_TYPE_ROLES = (
        ('student', 'Student'),
        ('teacher', 'Teacher')
    )
    # table columns
    user_type = models.CharField(max_length=10, choices=USER_TYPE_ROLES)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    ## methods to act on attributes
    def __str__(self):
        return f"{self.username} - {self.email}"
    def is_teacher(self):
        return self.user_type == 'teacher'
    def is_student(self):
        return self.user_type == 'student'