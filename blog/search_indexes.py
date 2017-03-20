#import datetime
from django.utils import timezone
from haystack import indexes
from blog.models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title_t = indexes.CharField(model_attr='title')
	author = indexes.CharField(model_attr='author')
	created_date = indexes.DateTimeField(model_attr='created_date')
	published_date = indexes.DateTimeField(model_attr='published_date', null=True)

	def get_model(self):
		return Post

	def index_queryset(self, using=None):
		#return self.get_model().objects.filter(created_date__lte=timezone.now())
		print(self.get_model().objects.all())
		return self.get_model().objects.all()

