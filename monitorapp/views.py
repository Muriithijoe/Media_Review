from django.shortcuts import render , redirect
from .models import DailyReview
from .forms import ReviewForm
import datetime;
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy

# Create your views here.
class ReviewCreateView(BSModalCreateView):
    template_name = 'write_review.html'
    form_class = ReviewForm
    success_message = 'Success: Review was created.'
    success_url = reverse_lazy('review')

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
