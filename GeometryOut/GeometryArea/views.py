from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse('Area home do G_area')


def zipcode_view(request):
    return render(request, 'visual/index.html')
