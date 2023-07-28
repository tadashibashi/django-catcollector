from django.forms import ModelForm
from .models import Feeding, Cat


class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ["date", "meal"]

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ["name", "breed", "description", "age"]
