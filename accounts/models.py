from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class OfficerProfile(models.Model):
	user 		= models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=100, default='')
	location    = models.CharField(max_length=100, default='')
	phone		= models.IntegerField(default=0)
	image 		= models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return str(self.user)
                


def create_profile(sender, **kwargs):
	if kwargs['created']:
		officer_profile = OfficerProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)




