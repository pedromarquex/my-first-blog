from django import forms
from .models import Post

class PostForm(forms.modelForm):

	class Meta:
		model = Post
		fields = ('title', 'text', )