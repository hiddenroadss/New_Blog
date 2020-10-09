from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	title = models.CharField('Title', max_length= 250)
	slug = models.SlugField('Slug', max_length=50)
	content = models.TextField('Content')
	date_created = models.DateField('Created', auto_now_add=True)
	date_modified = models.DateField('Last modified', auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
