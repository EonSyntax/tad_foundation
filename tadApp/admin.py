from django.contrib import admin
from .models import TeamMember, Volunteer, Sponsor, Testimonial, Project, ProjectImage
from django.utils.html import format_html

# Register your models here.
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Photo'





@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Photo'




@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Photo'



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:50%;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Photo'




class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_image_tag', 'status')
    inlines = [ProjectImageInline]

    def main_image_tag(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" width="80" height="50" style="object-fit: cover; border-radius: 4px;" />',
                obj.main_image.url
            )
        return "No Image"

    main_image_tag.short_description = 'Main Image'


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'image', 'uploaded_at')