from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking by {self.name} on {self.date} at {self.time}"


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploaded_images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} upload"
