from django.db import models
from django.contrib.auth.models import User
from django_prometheus.models import ExportModelOperationsMixin
import uuid

    
class Note(ExportModelOperationsMixin('note'), models.Model):
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
