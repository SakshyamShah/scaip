from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
import datetime
from django.utils import timezone

# Create your views here.

def get_report(request):
	return render(request, 'report/get_report.html', {})
def thankyou(request):
	return render(request, 'report/thankyou.html', {})

def report_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			Report_Data = form.save(commit=False)
			Report_Data.received_date = timezone.now()
			Report_Data.save()
			return redirect(thankyou)
	else:
		form = PostForm()
	return render(request, 'report/report_new.html', {'form': form})

