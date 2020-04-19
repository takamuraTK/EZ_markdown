from django.urls import path

# from . import views
from .views import ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView, ReportDeleteView

urlpatterns = [
    path('', ReportListView.as_view(), name='index'),
    path('<int:pk>/', ReportDetailView.as_view(), name='detail'),
    path('create/', ReportCreateView.as_view(), name='create'),
    path('<int:pk>/edit', ReportUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', ReportDeleteView.as_view(), name='delete'),
]