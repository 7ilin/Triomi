from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from decor.models import Call
from decor.forms import CallForm

def home(request):
    return render(request, 'decor/home_page.html')


def contacts(request):
    return render(request, 'decor/contacts.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'decor/post_detail.html', {'post': post})

def call_me(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            call = form.save(commit=False)
            call.name = request.user
            call.created_date = timezone.now()
            call.save()
            return redirect('home')
    else:
        form = CallForm
    return render(request, 'decor/order.html', {'form': form})

# Create your views here.
