from django.db import models
from musicians.models import Musician


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=15)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        choices=[
            (1, "1 star"),
            (2, "2 star"),
            (3, "3 star"),
            (4, "4 star"),
            (5, "5 star"),
        ]
    )

    def __str__(self):
        return self.name