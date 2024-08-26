from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import BlogForm,CommentForm
from django.contrib.auth import logout
from accounts.forms import update_user
from django.contrib.auth import authenticate,login
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    auth = request.user.is_authenticated
    user = request.user if auth else None
    if request.method=='GET':
        if user:
            print(type(user.user_bio))
            if user.user_bio is None or user.user_bio=='':
                form=update_user()
                return render(request,'accounts/update_user.html',{'form':form})
    if request.method=='POST':
        print("post")
        form=update_user(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'accounts/update_user.html',{'form':form})
    
    blogs = Blog.objects.all().order_by('-id')
    
    context = {
        'blogs': blogs,
        'user': user,
        'auth': auth
    }
    
    return render(request, 'blogs/index.html', context)
def update_users(request):
    if request.method=='GET':
        form=update_user()
        return render(request,'accounts/update_user.html',{'form':form})
    if request.method=='POST':
        print("post")
        form=update_user(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
class create_blog(LoginRequiredMixin,View):
    def get(self,request):
        blog_form=BlogForm()
        return render(request,'blogs/create_blog.html',{'blog_form':blog_form})
    def post(self,request):
        blog_form=BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('index')
        else:
            return render(request,'blogs/create_blog.html',{'blog_form':blog_form})
class comment_view(LoginRequiredMixin,View):
    def get(self,request,blog_id):
        blog=Blog.objects.get(id=blog_id)
        comment_form=CommentForm()
        return render(request,'blogs/comment.html',{'comment_form':comment_form,'blog':blog})
    def post(self,request,blog_id):
        blog=Blog.objects.get(id=blog_id)
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.blog=blog
            comment.save()
            return redirect('index')
        else:
            return render(request,'blogs/comment.html',{'comment_form':comment_form,'blog':blog})
def read_article(request,blog_id):
    auth = request.user.is_authenticated
    user = request.user if auth else None
    
    try:
        blog=Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return redirect('index')
    comment=Comment.objects.filter(post=blog).order_by('-created_at')
    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            print("valid")
            comment=comment_form.save()
            comment.post=blog
            comment.save()
            return redirect('read_article',blog_id)
        else:
            return render(request,'blogs/read_article.html',{'blog':blog,'comments':comment,'comment_form':comment_form,'auth':auth})
    else:
        comment_form=CommentForm(initial={'post':blog,'user':request.user})
        return render(request,'blogs/read_article.html',{'blog':blog,'comments':comment,'comment_form':comment_form,'auth':auth})
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'blogs/login.html')
    def post(self,request):
        print('POST')
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('login')
class Register(View):
    def get(self,request,msg=None):
        return render(request,'blogs/register.html',{'msg':msg})
    def post(self,request):
        full_name=request.POST['full_name']
        phone=request.POST['phone']
        full_name=full_name.split(' ')
        first_name=full_name[0]
        last_name=full_name[1]
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        user=get_user_model()
        if user.objects.filter(username=username).exists():
            return redirect('register','Username already exists')
        elif password!=confirm_password:
            return redirect('register','Passwords do not match')
        else:
            user.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,phone_number=phone)
            return redirect('login')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')