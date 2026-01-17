from django.db import models

class StudentModel(models.Model):
	name = models.CharField(primary_key=True, max_length=50)
	working = models.CharField(max_length=100)
	beautiful=models.CharField(max_length=3)
	useful=models.CharField(max_length=3)
	suggested=models.CharField(max_length=3)
	suggestion=models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.name
