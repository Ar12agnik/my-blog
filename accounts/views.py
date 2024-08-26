from django.shortcuts import render
from django.contrib.auth import get_user_model
from newsfeed.models import Blog
# Create your views here.
def profile(request):
    loggin= request.user.is_authenticated
    user=request.user
    blogs=Blog.objects.filter(user=user)
    return render(request, 'accounts/profile.html',{'user':user,'blogs':blogs,'loggin':loggin,'update':True})

def view_profile(request,username):
    loggin= request.user.is_authenticated
    User = get_user_model()
    user=User.objects.get(username=username)
    logged_in_user=request.user
    print(logged_in_user==user)
    if logged_in_user==user:
        blogs=Blog.objects.filter(user=user)
        return render(request, 'accounts/profile.html',{'user':user,'blogs':blogs,'loggin':loggin,'update':True})
    else:
        blogs=Blog.objects.filter(user=user)
        return render(request, 'accounts/profile.html',{'user':user,'blogs':blogs,'loggin':loggin})