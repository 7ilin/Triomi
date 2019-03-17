from django.shortcuts import render


def home(request):
    return render(request, 'decor/home_page.html')


def contacts(request):
    return render(request, 'decor/contacts.html')

# Create your views here.
