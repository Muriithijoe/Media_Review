from django.urls import path

from .views import homepage , new_review , review

urlpatterns = [
    path('',homepage, name='home'),
    path('newreview/', new_review, name='newreview'),
    path('review/', review, name='review')
]
