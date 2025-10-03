from django.shortcuts import render


from django.http import HttpResponse

def Home_view(request):
    return HttpResponse('<h1>HOME Page</h1>')

def About_view(request):
    return HttpResponse('<h1>About Page</h1>')

def Contact_view(request):
    return HttpResponse('<h1>Contact Page</h1>')




