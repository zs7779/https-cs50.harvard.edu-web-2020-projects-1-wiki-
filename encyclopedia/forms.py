from django import forms


class ArticleForm(forms.Form):
    article_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': "Title"
        }
    ))
    article_content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': "form-control",
            'rows': 20
        }
    ))


class SearchForm(forms.Form):
    search_query = forms.CharField()
