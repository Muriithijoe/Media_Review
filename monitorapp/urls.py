from django.urls import path
from .views import homepage , new_review , review , ReviewCreateView, ReviewReadView ,ReviewUpdateView

urlpatterns = [
    path('',homepage, name='home'),
    path('newreview/', new_review, name='newreview'),
    path('review/', review, name='review'),
    path('create/', ReviewCreateView.as_view(), name='create_review'),
    path('read/', ReviewReadView.as_view(), name='read_review'),
    path('update/', ReviewUpdateView.as_view(), name='update_review'),
]
