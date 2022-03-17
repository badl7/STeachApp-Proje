from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User,Student,Teacher,StudentsInClass

# Register your models here.
admin.site.register(StudentsInClass)

@admin.register(User)
class UsersAdmin(UserAdmin):
    list_display = ["username","is_student","is_teacher"]
    """
    fieldsets = UserAdmin.fieldsets + (
        (('Avatar Değiştirme Alanı'), {
            'fields': ['avatar'],
        }),
    )
    """

@admin.register(Student)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ["user","name","olus_tarih","email"]
    list_display_links = ["user","name"]
    search_fields = ["user"]

@admin.register(Teacher)
class TeacherUserAdmin(admin.ModelAdmin):
    list_display = ["user","name","subject_name","email"]
    list_display_links = ["user","name"]
    search_fields = ["user","subject_name"]
