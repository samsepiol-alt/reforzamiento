from django.contrib import admin
from .models import Course, Inscription

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'created_at')
    search_fields = ('title',)
 

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress', 'enrolled_at')
    search_fields = ('user__username', 'course__title')



