from django.contrib import admin

from core.models import Student


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','student_name','student_email')
    search_fields = ('student_name',)
