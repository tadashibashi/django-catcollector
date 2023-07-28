import datetime
from django.db import models
from django.urls import reverse

class Toy(models.Model):
    name = models.CharField(max_length=64, default="no name")
    color = models.CharField(max_length=64, default="no color")

    def __str__(self):
        return f"{self.color} {self.name}"

    def get_html_name(self):
        return "<span style='color:" + self.color + ";'>" + self.color.title() + \
            "</span> " + self.name.title()


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:cats_detail", kwargs={"pk": self.id})

MEALS = (
    ('B', "Breakfast"),
    ('L', "Lunch"),
    ('D', "Dinner"),
)

class Feeding(models.Model):
    date = models.DateField(default=datetime.date.today)
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]  # 'B'
    )
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']