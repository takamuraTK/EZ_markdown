from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, ListView, DetailView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy

from .forms import ReportForm
from .models import Report

class ReportListView(ListView):
    model = Report
    template_name = 'article/index.html'

class ReportDetailView(DetailView):
    model = Report
    template_name = 'article/detail.html'

class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'article/create.html'

    # success_urlを静的なページではないときに、get_success_urlを用いる
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'article/update.html'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'article/delete.html'
    success_url = reverse_lazy('index')
