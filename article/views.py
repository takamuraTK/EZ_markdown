from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReportForm
from .models import Report

def index(request):
    report_list = Report.objects.all()
    context = {'report_list': report_list}
    return render(request, 'article/index.html', context)

def detail(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    return render(request, 'article/detail.html', {'report': report})

def create(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = ReportForm()
    return render(request, 'article/create.html', params)