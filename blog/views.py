
from django.shortcuts import render


from django.http import HttpResponse
from blog.models import Post

def BlogHome_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts' : posts}
    return render(request , 'blog\\blog-home.html', context)

def BlogSingle_view(request):
    return render(request , 'blog\\blog-single.html')

def test_view(request):
    
    return render(request , 'blog\\test.html' )


