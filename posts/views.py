from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm


# Create your views here.

def home(request):
    return render(request, 'posts/home.html')

def feed(request):
    form = PostForm()
    posts = Post.objects.all().order_by('-created_at')
    if request.user.is_authenticated:
        liked_post_ids = request.user.likes.values_list('post_id', flat=True)
    else:
        liked_post_ids = []

    cform = CommentForm()
    return render(request, 'posts/feed.html', {
        'post_form': form,
        'posts': posts,
        'cform': cform,
        'liked_post_ids': liked_post_ids
    })


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    return redirect('feed')
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        # se già esiste, togli il like
        like.delete()
    return redirect('feed')

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    return redirect('feed')

