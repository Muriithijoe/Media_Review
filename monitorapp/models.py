from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class DailyReview(models.Model):
    date = models.DateField()
    media_link = models.TextField(validators=[URLValidator()],null=True)
    nation = models.TextField(max_length = 500)
    standard = models.TextField(max_length = 500)

    def save_review(self):
        self.save()
