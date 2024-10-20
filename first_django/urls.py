from django.contrib import admin
from django.urls import path,include
from first_django import views

handler404='first_django.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls')),
    path('api/',include('polls.api_urls')),
    path('accounts/',include('accounts.urls')),
]
