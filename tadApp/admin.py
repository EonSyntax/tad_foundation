from django.contrib import admin
from .models import TeamMember, Volunteer, Sponsor, Testimonial
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