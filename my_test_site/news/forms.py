from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label='Название статьи',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    content = forms.CharField(
        label='Текст статьи',
        required=False,
        widget=forms.Textarea({
            'class': 'form-control',
            'rows': '3',
        })
    )
    is_published = forms.BooleanField(
        label='опубликованно?',
        initial=True,
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Выберите категорию',
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
