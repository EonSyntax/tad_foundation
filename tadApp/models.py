from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

# Models for TeamMember
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default'
    )

    def __str__(self):
        return self.name

# Models for Volunteer
class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    project_Volunteered_For = models.CharField(max_length=100)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default'
    )

    def __str__(self):
        return self.name
    
# Models for Sponsor
class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    project_Sponsored = models.CharField(max_length=100)
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default'
    )

    def __str__(self):
        return self.name


# Models for Testimonial
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    image = CloudinaryField(
        'image',
        blank=True,
        null=True,
        default='default'
    )

    def __str__(self):
        return self.name

# Models for Project
class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]

    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    main_image = CloudinaryField('image', default='default')

    goal_price = models.DecimalField(max_digits=12, decimal_places=2)
    raised_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.status})"

    @property
    def progress_percentage(self):
        if self.goal_price > 0:
            return min(100, round((self.raised_price / self.goal_price) * 100))
        return 0


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='other_images')
    image = CloudinaryField('image', default='default')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} for {self.project.name}"
    



