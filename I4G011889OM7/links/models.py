from django.db import models
from django.contrib.auth import get_user_model

from I4G011889OM7.links.managers import ActiveLinkManager

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    decription = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20)
    author = get_user_model()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    objects = models.Manager()
    public = ActiveLinkManager()

