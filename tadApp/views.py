from django.shortcuts import render
from .models import TeamMember, Volunteer, Sponsor, Testimonial







# Create your views here.
def index(request): 
    team = TeamMember.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request, 'pages/index.html', {'team': team, 'testimonial': testimonial})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def volunteers(request):
    volunteer = Volunteer.objects.all()
    return render(request, 'pages/volunteers.html', {'volunteer': volunteer})

def sponsors(request):
    sponsor = Sponsor.objects.all()
    return render(request, 'pages/sponsors.html', {'sponsor': sponsor})

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
    team = TeamMember.objects.all()
    return render(request, 'pages/team.html', {'team': team})

def testimonial(request):
    testimonial = Testimonial.objects.all()
    return render(request, 'pages/testimonial.html', {'testimonial': testimonial})

def _404(request):
    return render(request, 'pages/404.html')