
from django import forms
from .models import Report_Data

class PostForm(forms.ModelForm):

	class Meta:
		model = Report_Data
		fields = ('catagory', 'location', 'trafficker-info', 'description')