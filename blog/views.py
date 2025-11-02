
from django.shortcuts import render


from django.http import HttpResponse
from blog.models import Post

def BlogHome_view(request):
    return render(request , 'blog\\blog-home.html')

def BlogSingle_view(request):
    return render(request , 'blog\\blog-single.html')

def test_view(request):
    publish_posts = Post.objects.filter(status=True)
    private_posts = Post.objects.filter(status=False)
    context = {'publish_posts' : publish_posts , 'private_posts' : private_posts}
    return render(request , 'blog\\test.html' , context)


