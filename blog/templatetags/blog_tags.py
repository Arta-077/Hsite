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


@register.filter
def brief_naturaltime(value):
    if not value:
        return ""
    # خروجی معمولاً به صورت "1 month, 2 weeks..." است
    # ما آن را بر اساس کاما جدا کرده و فقط بخش اول را برمی‌گردانیم
    first_part = str(value).split(',')[0]
    
    # اگر کلمه "ago" در کل رشته بود و در بخش اول نبود، آن را اضافه می‌کنیم
    if "ago" not in first_part and "ago" in str(value):
        first_part += " ago"
        
    return first_part

