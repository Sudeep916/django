from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,World My name is Sudeep")

def welcome_view(request):  
    return HttpResponse("Welcome to the Polls App!")  

def goodbye_view(request):  
    return HttpResponse("Thank you for visiting the Polls App!")  

def about_view(request):  
    return HttpResponse("This app allows you to create and manage polls.")

def greet_view(request, name):  
    return HttpResponse(f"Hello, {name}!")
