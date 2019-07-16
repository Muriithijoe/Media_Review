from django.shortcuts import render , redirect
from .models import DailyReview
from .forms import ReviewForm

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def new_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
        return redirect('home')

    else:
        form = ReviewForm()
    return render(request, 'write_review.html', {"form": form})
