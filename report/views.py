from django.shortcuts import render
from .forms import PostForm

# Create your views here.

def get_report(request):
	return render(request, 'report/get_report.html', {})

def report_new(request):
	form = PostForm()
	return render(request, 'report/report_new.html', {'form': form})

