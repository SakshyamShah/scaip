
from django import forms
from .models import Report_Data



class PostForm(forms.ModelForm):

	class Meta:
		model = Report_Data
		fields = ('about_issue', 'report_location', 'trafficker_name', 'description')