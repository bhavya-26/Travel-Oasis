from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'travel_oasis/home_page.html', {})

def qgender(request):
    return render(request, 'travel_oasis/qgender.html', {})


def qclimate(request):
    return render(request, 'travel_oasis/qclimate.html', {})

def qsolo(request):
    return render(request, 'travel_oasis/qsolo.html', {})

def qduration(request):
    return render(request, 'travel_oasis/qduration.html', {})