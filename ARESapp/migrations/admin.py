from django.contrib import admin
from .models import Project, Skill, ResumeEntry

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    search_fields = ('name',)

@admin.register(ResumeEntry)
class ResumeEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company')
    list_filter = ('start_date', 'end_date')
