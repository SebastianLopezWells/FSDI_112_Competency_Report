from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

#from symbol import return_stmt


# Create your models here.
class Satus(models.Model):  # esto se debe de llamar Satus
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Satus,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
