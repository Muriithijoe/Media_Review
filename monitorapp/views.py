from django.shortcuts import render , redirect
from .models import DailyReview
from .forms import ReviewForm
import datetime;
from bootstrap_modal_forms.generic import BSModalCreateView

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def new_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.save(using='monitoring')
        return redirect('review')

    else:
        form = ReviewForm(request.POST)
    return render(request, 'write_review.html', {"form": form})

def review(request):
    reviews = DailyReview.objects.all()
    return render(request, 'reviews.html', {"reviews": reviews})
