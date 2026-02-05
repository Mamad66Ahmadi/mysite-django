from django import template
from blog.models import Post
from blog.models import Category


register = template.Library()


@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status =1)
    categories = Category.objects.all()
    cat_dict = {}
    for category in categories:
        cat_dict[category] = posts.filter(category=category).count()
    
    # Sort by count in descending order
    sorted_categories = sorted(cat_dict.items(), key=lambda x: x[1], reverse=True)
    
    return {'categories': sorted_categories}