from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def volunteers(request):
    return render(request, 'pages/volunteers.html')

def upcomingprojects(request):
    return render(request, 'pages/upcomingprojects.html')

def completedprojects(request):
    return render(request, 'pages/completedprojects.html')

def upcomingprojectdetail(request):
    return render(request, 'pages/upcomingprojectdetail.html')

def completedprojectdetail(request):
    return render(request, 'pages/completedprojectdetail.html')

def donate(request):
    return render(request, 'pages/donate.html')

def team(request):
    return render(request, 'pages/team.html')

def testimonial(request):
    return render(request, 'pages/testimonial.html')

def _404(request):
    return render(request, 'pages/404.html')