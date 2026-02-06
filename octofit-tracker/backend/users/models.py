from django.db import models
from teams.models import Team

class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.name
