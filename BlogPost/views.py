from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    '''Function for Home Page of the App'''
    # return HttpResponse('Home Page')
    return render(request, 'homePage.html')

def about(request):
    '''Function defining about path'''
    # return HttpResponse('About')
    return render(request, 'about.html')
