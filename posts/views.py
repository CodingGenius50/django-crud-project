
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment  # ✔️ এটা ঠিক
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts:post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:home')  # যদি main urls.py তে name='home' থাকে
    else:
        form = PostForm()  # 👈 এটা else ব্লকে থাকবে

    # সবশেষে return করতে হবে
    return render(request, 'posts/create_post.html', {'form': form})

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # যেই পোস্ট edit করতে চাই সেটি নাও
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # instance=post দিয়ে পুরনো ডাটা ফর্মে দেখাবে
        if form.is_valid():
            form.save()
            return redirect('posts:home')  # save হলে home page
    else:
        form = PostForm(instance=post)  # GET request হলে ফর্মে পুরনো ডাটা দেখাবে

    return render(request, 'posts/update_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':  # confirmation দিয়ে delete
        post.delete()
        return redirect('posts:home')
    return render(request, 'posts/delete_post.html', {'post': post})
