
from django.shortcuts import render , get_object_or_404


from django.http import HttpResponse
from blog.models import Post

def BlogHome_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts' : posts}
    return render(request , 'blog\\blog-home.html', context)

def BlogSingle_view(request,pid): 
    post = get_object_or_404(Post , id=pid)
    
    context = {'post':post}
    return render(request , 'blog\\blog-single.html' , context)

def test_view(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post , id=pid)
    
    context = {'post':post}
    return render(request , 'blog\\test.html' ,context )


