from django.http import Http404, HttpResponse
from django.shortcuts import render
from posts.models import Post

# Create your views here.


def post_list(request) -> HttpResponse:
    slug = request.GET.get("slug", "")
    print(slug)
    return render(request, "posts/list.html")


def post(request, slug) -> HttpResponse:
    try:
        curr_post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post not found")

    return render(request, "posts/post.html", {"post": curr_post})
