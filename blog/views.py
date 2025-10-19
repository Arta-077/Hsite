
from django.shortcuts import render


from django.http import HttpResponse

def BlogHome_view(request):
    return render(request , 'blog\\blog-home.html')

def BlogSingle_view(request):
    return render(request , 'blog\\blog-single.html')




