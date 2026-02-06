from django.db import models
from users.models import User

class Leaderboard(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.user.name} - {self.points}"
