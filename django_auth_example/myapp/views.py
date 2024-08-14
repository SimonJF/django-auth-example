from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Comment, default_user
from .forms import CommentForm


def index(request):
    comments = Comment.objects.order_by("-id")
    context = {
        "comments": comments,
        "form": CommentForm()
    }
    return render(request, "myapp/index.html", context)

def post_comment(request):
    if request.method != "POST":
        return HttpResponseRedirect("/myapp")

    form = CommentForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        c = Comment(user=default_user(), comment=data["body"])
        c.save()
    return HttpResponseRedirect("/myapp")
