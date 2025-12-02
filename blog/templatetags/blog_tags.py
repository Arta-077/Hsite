from django import template
from blog.models import Post , Category

register=template.Library()


@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status = 1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status = 1)
    categories = Category.objects.all()
    cat_dict = {}
    for category in categories:
        cat_dict[category] = posts.filter(category=category).count()
    return {'cat_dict':cat_dict}
