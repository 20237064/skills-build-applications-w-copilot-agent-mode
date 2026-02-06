from django.db import models
from users.models import User

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	type = models.CharField(max_length=50)
	description = models.TextField()
	duration = models.IntegerField()  # minutes
	def __str__(self):
		return f"{self.user.name} - {self.type}"
