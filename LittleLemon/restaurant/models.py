from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.no_of_guests},  {self.booking_date.strftime('%d-%m-%Y %H:%M')}"


class Menu(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()


    def __str__(self):
        return f'{self.title} : {str(self.price)}'