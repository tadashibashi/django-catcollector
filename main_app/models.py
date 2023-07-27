import datetime
from django.db import models
from django.urls import reverse

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:cats_detail", kwargs={"pk": self.id})

_MEALS = (
    ('B', "Breakfast"),
    ('L', "Lunch"),
    ('D', "Dinner"),
)

class Feeding(models.Model):
    date = models.DateField(default=datetime.date.today)
    meal = models.CharField(
        max_length=1,
        choices=_MEALS,
        default=_MEALS[0][0]  # 'B'
    )
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

