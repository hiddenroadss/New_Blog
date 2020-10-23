from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify

from time import time


def generate_slug(title):
    new_slug = slugify(title)
    unique_slug = new_slug + '-' + str(int(time()))
    return unique_slug


class Blog(models.Model):
    title = models.CharField('Title', max_length=50)
    slug = models.SlugField('Slug', max_length=50, blank=True)
    content = models.TextField('Content')
    date_created = models.DateTimeField('Created', auto_now_add=True)
    date_modified = models.DateTimeField('Last modified', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})
