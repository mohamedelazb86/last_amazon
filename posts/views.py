from django.shortcuts import render,redirect
from .models import Post,Review
from .forms import PostForm,ReviewForm

def post_list(request):
    posts=Post.objects.all()

    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            form.save()
            return redirect('/posts/')
    else:
        form=PostForm()

    context={
        'posts':posts,
        'form':form
    }
    return render(request,'posts/post_list.html',context)

def post_detail(request,slug):
    post=Post.objects.get(slug=slug)
    reviews=Review.objects.filter(post=post)
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.post=post
            myform.save()
            return redirect(f'/posts/{post.slug}')
    else:
        form=ReviewForm()
    context={
        'post':post,
        'reviews':reviews,
        'form':form
    }
    return render(request,'posts/post_detail.html',context)

def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()

            return redirect('/posts/')
    else:
        form=PostForm()
    return render(request,'posts/update_post.html',{'form':form})

def update_post(request,slug):
    post=Post.objects.get(slug=slug)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/posts/')
    else:
        form=PostForm(instance=post)
    return render(request,'posts/update_post.html',{'form':form})

def delete_post(request,slug):
    post=Post.objects.get(slug=slug)
    post.delete()
    return redirect('/posts/')
