from django.shortcuts import render , redirect
from .models import DailyReview
from .forms import ReviewForm
import datetime;
from django.views import generic
from bootstrap_modal_forms.generic import (BSModalCreateView, BSModalReadView,  BSModalUpdateView)
from django.urls import reverse_lazy

# Create your views here.
class ReviewCreateView(BSModalCreateView):
    template_name = 'create_review.html'
    form_class = ReviewForm
    success_message = 'Success: Review was created.'
    success_url = reverse_lazy('review')

class ReviewReadView(BSModalReadView):
    model = DailyReview
    template_name = 'templates/read_review.html'

class ReviewUpdateView(BSModalUpdateView):
    model = DailyReview
    template_name = 'templates/update_book.html'
    form_class = ReviewForm
    success_message = 'Success: Review was updated.'
    success_url = reverse_lazy('read_review')

def homepage(request):
    return render(request,'homepage.html')

def new_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.save(using='monitoring')
        return redirect('review')

    else:
        form = ReviewForm(request.POST)
        print = "Imekataa"
    return render(request, 'write_review.html', {"form": form})

def review(request):
    reviews = DailyReview.objects.all()
    return render(request, 'reviews.html', {"reviews": reviews})
