from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class DailyReview(models.Model):
    date = models.DateField()
    media_link = models.TextField(validators=[URLValidator()],blank=True)
    nation = models.TextField(max_length = 500,blank=True)
    standard = models.TextField(max_length = 500,blank=True)
    business_daily = models.TextField(max_length = 500,blank=True)

    def save_review(self):
        self.save()
