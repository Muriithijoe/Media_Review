from django import forms
from .models import DailyReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = DailyReview
