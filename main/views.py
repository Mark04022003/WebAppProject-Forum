
from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from main.models import Post
from main.serializers import PostSerializer

def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = User.objects.all().count()
    num_categories = forums.count()
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []

    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "title": "HCMIU - Forum"
    }
    return render(request, "forums.html", context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        commenr_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=commenr_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
        comment_obj.replies.add(new_reply.id)


    context = {
        "post":post,
        "title": "HCMIU - Forum: "+post.title,
    }
    update_views(request, post)

    return render(request, "detail.html", context)

def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category).order_by('-date')
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    context = {
        "posts":posts,
        "forum": category,
        "title": "HCMIU - Forum: Posts"
    }

    return render(request, "posts.html", context)


@login_required
def create_post(request):
    if not request.user.is_active:
        messages.error(request, "You must verify your email before creating posts.")
        return redirect("home")

    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                author = Author.objects.get(user=request.user)
            except Author.DoesNotExist:
                messages.error(request, "No author profile found for your account.")
                return redirect("home")
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "title": "HCMIU - Forum: Create New Post"
    })
    return render(request, "create_post.html", context)

def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "HCMIU - Forum: Latest 10 Posts"
    }

    return render(request, "latest-posts.html", context)

def search_result(request):

    return render(request, "search.html")

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.user.user != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect("home")

    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect("detail", slug=post.slug)

    context = {
        "form": form,
        "title": "HCMIU - Forum: Edit Post",
        "post": post,
    }
    return render(request, "edit_post.html", context)

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.user.user != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect("home")

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect("home")

    context = {
        "post": post,
        "title": "HCMIU - Forum: Delete Post"
    }
    return render(request, "delete_post.html", context)
