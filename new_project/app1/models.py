from django.db import models

# Create your models here.
class Musician(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name +" "+ self.last_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()

    ratings = (
        (1, "wrost"),
        (2, "Bad"),
        (3, "Average"),
        (4, "Good"),
        (5, "Best"),
    )
    num_stars = models.IntegerField(choices=ratings)

    def __str__(self):
        return self.name + ", Rating: "+ str(self.num_stars)