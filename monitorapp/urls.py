from django.urls import path

from .views import homepage , new_review , review , ReviewCreateView

urlpatterns = [
    path('',homepage, name='home'),
    path('newreview/', new_review, name='newreview'),
    path('review/', review, name='review'),
    path('create/', ReviewCreateView, name='create_review'),
]
