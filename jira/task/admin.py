from django.contrib import admin

from task.models import Task, CustomField


# Register your models here.


# add simple admin for task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


# add simple admin for custom-field
@admin.register(CustomField)
class CustomFieldAdmin(admin.ModelAdmin):
    pass
