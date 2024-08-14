from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def find_app_user(user):
    return AppUser.objects.get(user=user)

class Comment(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

def default_user():
    try:
        return AppUser.objects.get(name="DefaultUser")
    except:
        base_user = User.objects.create_user("default", "default@default.com", "defaultpassword")
        default_user = AppUser(name="DefaultUser", user=base_user)
        default_user.save()
        return default_user

