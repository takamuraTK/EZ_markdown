from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('article/', include('article.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
