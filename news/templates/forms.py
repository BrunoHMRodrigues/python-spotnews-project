from django import forms
from news.models import News, Categories, Users

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)

class NewsForm(forms.ModelForm):
    created_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    categories = forms.ModelMultipleChoiceField(
        queryset=Categories.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    author = forms.ModelChoiceField(
        queryset=Users.objects.all(),
        empty_label="---------",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = News
        fields = ['title', 'content', 'author', 'created_at', 'image', 'categories']
