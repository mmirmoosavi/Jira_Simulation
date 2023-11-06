from django.db import models
from django.db.models import TextChoices


class Task(models.Model):

    # static fields that user cannot add or remove these fields from Platform
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)

    # Add other static fields here that you need

    def __str__(self):
        return f'task_name:{self.name}; task_status:{self.status}'


# create Custom Field as a separate table that can use for any custom-fields that user want to define in a task
class CustomField(models.Model):
    # add types for custom field
    class FieldType(TextChoices):
        TEXT = ('text', 'TEXT')
        INTEGER = ('int', 'INTEGER')
        DATE = ('date', 'DATE')
        USER = ('user', 'USER')

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=10, choices=FieldType.choices)
    field_value_text = models.TextField(blank=True, null=True)
    field_value_int = models.IntegerField(blank=True, null=True)
    field_value_date = models.DateField(blank=True, null=True)
    field_value_user = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.field_name} for Task: {self.task.name}"
