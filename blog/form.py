from django import forms

from .models import Post, MojeModele, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)

class SecondForm(forms.ModelForm):

    class Meta:
        model = MojeModele
        fields = ('tytul_postu','tresc_postu',)

class EmailPostForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(required=False, widget=forms.Textarea)
    #name = forms.CharField(max_length=25)
    #email = forms.EmailField()
    to = forms.EmailField()
    #comments = forms.CharField(required = False,widget=forms.Textarea)

class FormDoMaila(forms.Form):
    imie = forms.CharField(max_length=100)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', )
