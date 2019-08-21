from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE")
    user_image = models.ImageField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=40, default="Male")

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
