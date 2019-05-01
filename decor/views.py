from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from decor.models import Call, Portfolio, Post, Rent
from decor.forms import CallForm, PostForm


def home(request):
    portfolios = Portfolio.objects.reverse()[:1]
    rents = Rent.objects.reverse()[:1]
    posts = Post.objects.reverse()[:2]
    return render(request, 'decor/home_page.html', {'rent': rents, 'portfolio': portfolios, 'posts': posts})


def contacts(request):
    return render(request, 'decor/contacts.html')


def call_me(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            call = form.save(commit=False)
            call.created_date = timezone.now()
            call.save()
            return redirect('home')
    else:
        form = CallForm
    return render(request, 'decor/order.html', {'form': form})


def portfolio(request):
    portfolios = Portfolio.objects.all()

    return render(request, 'decor/album.html', {'portfolio': portfolios})


def image_view(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'decor/image.html', {'portfolio': portfolio})


def rent(request):
    rents = Rent.objects.all()
    return render(request, 'decor/rent_album.html', {'rent': rents})


def rent_view(request, pk):
    rent = get_object_or_404(Rent, pk=pk)
    return render(request, 'decor/rent_image.html', {'rent': rent})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'decor/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'decor/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'decor/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'decor/post_edit.html', {'form': form})

# Create your views here.
