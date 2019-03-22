from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Movie(models.Model):
    title = models.CharField(max_length = 70, unique=True)
    poster = models.ImageField(upload_to="images/")
    stock = models.IntegerField(default = 1)
    rented = models.IntegerField(default = 0)
    sumary = models.TextField(max_length = 200)

    def rent(self):
        self.stock -= 1
        self.rented += 1

    def give_back(self):
        self.stock += 1
        self.rented -= 1

    def __str__(self):
        return self.title

class RentedMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rented_movies = models.ManyToManyField(RentedMovie)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()