from django.shortcuts import render

def get_report(request):
	return render(request, 'report/get_report.html', {})


# Create your views here.
