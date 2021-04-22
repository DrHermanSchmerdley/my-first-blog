from django import forms

from .models import Post

class PostForm(forms.ModelForm):
#telling django this form is a modelform
    class Meta:
        model = Post
        #which model creates form
        fields = ('title', 'text',)