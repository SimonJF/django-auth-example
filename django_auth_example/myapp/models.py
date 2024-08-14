from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

def default_user():
    try:
        return User.objects.get(name="DefaultUser")
    except:
        default_user = User(name = "DefaultUser")
        default_user.save()
        return default_user

