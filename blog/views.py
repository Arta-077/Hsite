from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from blog.models import Post , Comment
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.db.models import Count
from blog.forms import CommentForm
from django.contrib import messages
from django.shortcuts import redirect

def BlogHome_view(request, **kwargs):
    posts = Post.objects.filter(status=True)
    posts = posts.annotate(comments_count=Count('comment'))
    posts = posts.order_by('-created_date')

    if kwargs.get('cat_name') != None:
        posts = posts.filter(status=True, category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(status=True, author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(status=True, tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html', context)

def BlogSingle_view(request,pid): 
    post = get_object_or_404(Post.objects.filter(status=True), id=pid)

    comments = Comment.objects.filter(post=post.id, approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully')
            return redirect('blog:singleblog', pid=post.id)
        else:
            messages.add_message(request, messages.ERROR, 'ERROR')
    form = CommentForm()
    
    context = {'post':post, 'comments':comments, 'form':form}
    return render(request , 'blog/blog-single.html' , context)


def test_view(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post , id=pid)
    
    context = {'post':post}
    return render(request , 'blog/test.html' ,context )

def BlogCategory_view(request,cat_name):
    posts = Post.objects.filter(status=True , category__name=cat_name)

    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html', context)


def BlogSearch_view(request):
    posts = Post.objects.filter(status=True) 

    if s := request.GET.get('search'): 
        posts = posts.filter(content__icontains=s) 

    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html', context)





