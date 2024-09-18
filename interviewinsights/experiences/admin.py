from django.contrib import admin
from .models import InterviewExperience

class InterviewExperienceAdmin(admin.ModelAdmin):
    list_display = ('candidate_name', 'college_name', 'company_name', 'timestamp')
    search_fields = ('candidate_name', 'college_name', 'company_name')
    list_filter = ('company_name', 'college_name')
    ordering = ('-timestamp',)

admin.site.register(InterviewExperience, InterviewExperienceAdmin)
