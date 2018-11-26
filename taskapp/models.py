from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
task_choice = (('1', 'Not submitted'), ('2', 'under process'), ('3', 'completed'))

class Task(models.Model):
    username = models.OneToOneField(User, limit_choices_to={'is_superuser':False})
    rollno = models.CharField(max_length=10, help_text='Student Roll number')
    course_name = models.CharField(max_length=50, help_text='Student ciurse name')
    task_name = models.CharField(max_length=300, help_text='Student task/project name')
    submitted = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    remarks = models.CharField(max_length=100, help_text='Remarks of the task')
    task_status = models.CharField(max_length=1, choices=task_choice)
    last_date = models.DateTimeField(default=datetime.datetime.now())
    file = models.FileField(verbose_name='Project file')

    def __str__(self):
        return '{0}'.format(self.username)

