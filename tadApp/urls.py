"""tadDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from tadApp.views import healthz

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('upcomingprojects', views.upcomingprojects, name='upcomingprojects'),
    path('completedprojects', views.completedprojects, name='completedprojects'),
    path('upcomingprojectdetail/<int:pk>/', views.upcomingprojectdetail, name='upcomingprojectdetail'),
    path('completedprojectdetail/<int:pk>/', views.completedprojectdetail, name='completedprojectdetail'),
    path('donate', views.donate, name='donate'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('volunteers', views.volunteers, name='volunteers'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('contact', views.contact, name='contact'),
    path('404', views._404, name='404'),
    path("healthz/", healthz, name="healthz"),
]