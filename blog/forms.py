from haystack.forms import SearchForm
from django import forms
from .models import Post

class PostsSearchForm(SearchForm):
	def no_query_found(self):
		return self.searchqueryset.all()
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
