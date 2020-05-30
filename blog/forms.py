from django.forms import ModelForm, Textarea
from .models import Post, Comment
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

class PostForm(ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title':Textarea(attrs={'class':'textinputclass', 'cols':40, 'rows':1}),
            'text':CKEditorWidget(attrs={'class':'textinputclass', 'cols':40, 'rows':1}),
        }




class CommentForm(ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':Textarea(attrs={'class':'textinputclass','cols':40, 'rows':1}),
            'text':CKEditorWidget(attrs={'class':'textinputclass', 'cols':40, 'rows':1}),
        }
