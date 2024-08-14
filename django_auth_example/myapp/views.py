from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from .models import Comment, AppUser, find_app_user, default_user
from .forms import LoginForm, RegistrationForm, CommentForm


def index(request):
    comments = Comment.objects.order_by("-id")
    user = None
    if request.user.is_authenticated:
        user = find_app_user(request.user).name

    context = {
        "comments": comments,
        "form": CommentForm(),
        "logged_in_user": user
    }
    return render(request, "myapp/index.html", context)

def post_comment(request):
    if request.method != "POST":
        return HttpResponseRedirect("/myapp")

    form = CommentForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = default_user()
        if request.user.is_authenticated:
            user = find_app_user(request.user)
        c = Comment(user=user, comment=data["body"])
        c.save()
    return HttpResponseRedirect("/myapp")

def log_in(request):
    if request.method == "POST":
        usernm = request.POST["username"]
        passwd = request.POST["password"]
        user = authenticate(request, username=usernm, password=passwd)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/myapp")
        else:
            return HttpResponseRedirect("/myapp/login?state=loginfail")
    else:
        return render(request, "myapp/login.html", { "form": LoginForm()})

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/myapp")

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        usernm = request.POST["username"]
        passwd = request.POST["password"]
        email = request.POST["email"]

        # Create base user
        user = User.objects.create_user(usernm, email, passwd)
        app_user = AppUser(name=name, user=user)
        app_user.save()

        # Redirect to login form
        return HttpResponseRedirect("/myapp/login")
    else:
        return render(request, "myapp/register.html", { "form": RegistrationForm() })
