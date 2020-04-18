from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Report

def index(request):
    report_list = Report.objects.all()
    context = {'report_list': report_list}
    return render(request, 'article/index.html', context)

def detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'article/detail.html', {'report': report})

