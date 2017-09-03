from django.db import models

# Create your models here.
from django.urls import reverse


class Flavor(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    scoops_remaining = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("flavors:detail", kwargs={"slug": self.slug})
