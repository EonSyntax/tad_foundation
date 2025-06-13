from django.shortcuts import render, get_object_or_404
from .models import TeamMember, Volunteer, Sponsor, Testimonial, Project, ProjectImage







# Create your views here.
def index(request): 
    team = TeamMember.objects.all()
    testimonial = Testimonial.objects.all()
    upcoming_projects = Project.objects.filter(status='upcoming').order_by('-date')[:3]
    completed_projects = Project.objects.filter(status='completed').order_by('-date')[:3]
    donation_projects = Project.objects.filter(status='upcoming')
    return render(request, 'pages/index.html', {'team': team, 'testimonial': testimonial, 'upcoming_projects': upcoming_projects, 'completed_projects': completed_projects, 'projects': donation_projects,})





def about(request):
    team = TeamMember.objects.all()
    return render(request, 'pages/about.html', {'team': team})






def contact(request):
    return render(request, 'pages/contact.html')





def volunteers(request):
    volunteer = Volunteer.objects.all()
    return render(request, 'pages/volunteers.html', {'volunteer': volunteer})





def sponsors(request):
    sponsor = Sponsor.objects.all()
    return render(request, 'pages/sponsors.html', {'sponsor': sponsor})





def upcomingprojects(request):
    projects = Project.objects.filter(status='upcoming').order_by('-date')
    return render(request, 'pages/upcomingprojects.html', {'project': projects})




def completedprojects(request):
    projects = Project.objects.filter(status='completed').order_by('-date')
    return render(request, 'pages/completedprojects.html', {'projectk': projects})





def upcomingprojectdetail(request, pk):
    project = get_object_or_404(Project, pk=pk, status='upcoming')
    testimonial = Testimonial.objects.all()
    donation_projects = Project.objects.filter(status='upcoming')
    return render(request, 'pages/upcomingprojectdetail.html', {'project': project, 'testimonial': testimonial, 'projects': donation_projects,})




def completedprojectdetail(request, pk):
    project = get_object_or_404(Project, pk=pk, status='completed')
    testimonial = Testimonial.objects.all()
    donation_projects = Project.objects.filter(status='upcoming')
    return render(request, 'pages/completedprojectdetail.html', {'project': project, 'testimonial': testimonial, 'projects': donation_projects,})





def donate(request):
    donation_projects = Project.objects.filter(status='upcoming')
    return render(request, 'pages/donate.html', {'projects': donation_projects,})



def team(request):
    team = TeamMember.objects.all()
    return render(request, 'pages/team.html', {'team': team})




def testimonial(request):
    testimonial = Testimonial.objects.all()
    return render(request, 'pages/testimonial.html', {'testimonial': testimonial})





def _404(request):
    return render(request, 'pages/404.html', status=404)