from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(label="Comment")
