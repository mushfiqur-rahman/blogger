from django import forms

from blog.models import Post


class PostSearchForm(forms.Form):
    q = forms.CharField()

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].widget.attrs.update({'class': 'form-control'})


class PostForm(forms.Form):
    class Meta:
        model = Post