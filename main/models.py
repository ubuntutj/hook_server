from django.db import models

class UserData(models.Model):
	title = models.CharField("title", max_length=200)
	description = models.CharField("description", max_length=100)
	url = models.CharField("url", max_length=100)
	photo = models.ImageField("photo", upload_to="images/")

	def __str__(self):
		return "{} {} {} {}".format(self.title, self.description, self.url, self.photo)