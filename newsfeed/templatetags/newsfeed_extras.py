from django import template
from ..models import Blog
from ..forms import BlogForm
register=template.Library()
@register.inclusion_tag('blogs/latest_blogs.html')
def show_latest_blogs():
    latest_blogs=Blog.objects.order_by('-id')[0:5]
    return {'blogs':latest_blogs}
@register.inclusion_tag('blogs/word_limit.html')
def word_limit(content):
    return {'content':content[:20]}
@register.inclusion_tag('blogs/blog_form.html')
def show_blog_form(user):
    form=BlogForm(initial={'user':user})
    
    return {'form':form}
