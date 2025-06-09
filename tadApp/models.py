from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    image = models.ImageField(
    upload_to='team_images/',
    blank=True,
    null=True,
    default='team_images/default.png'  # or any valid path inside your media folder
    )

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    project_Volunteered_For = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='volunteer_images/',
        blank=True,
        null=True,
        default='team_images/default.png'  # or any valid path inside your media folder
    )

    def __str__(self):
        return self.name
    

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    project_Sponsored = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='volunteer_images/',
        blank=True,
        null=True,
        default='team_images/default.png'  # or any valid path inside your media folder
    )

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    image = models.ImageField(
        upload_to='volunteer_images/',
        blank=True,
        null=True,
        default='team_images/default.png'  # or any valid path inside your media folder
    )

    def __str__(self):
        return self.name







"""
        Team
image
name
designation
whatsapp number
facebook link
instagram link



        for upcoming&completed project
category
project name
description
project start date
project end date
project status (ongoing, completed, upcoming)
image
goal price
raised price


"""


