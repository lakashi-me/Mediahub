from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class MediaAsset(models.Model):
    CATEGORY_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="Uploaded and maintained by MediaHUB")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='image')
    media_file = CloudinaryField('media', resource_type='auto')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='media_assets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
