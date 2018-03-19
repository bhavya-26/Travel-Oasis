from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'travel_oasis/home_page.html', {})