from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('welcome/', views.welcome_view, name='welcome'),  
    path('goodbye/', views.goodbye_view, name='goodbye'),  
    path('about/', views.about_view, name='about'),  
    path('greet/<str:name>/', views.greet_view, name='greet'),
]
