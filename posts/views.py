from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    return render(request, 'posts/home.html')

def feed(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('feed')
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')  # newest first
    return render(request, 'posts/feed.html', {'form': form, 'posts': posts})

