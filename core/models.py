from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
	name=models.CharField(max_length=50)
	user=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Task(models.Model):
	project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
	description=models.CharField(max_length=259)
	completed=models.BooleanField(default=False)

	def __str__(self):
		return self.description
