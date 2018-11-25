from django.db import models
import datetime
# Create your models here.
task_choice = (('1', 'Not submitted'), ('2', 'under process'), ('3', 'completed'))

class Task(models.Model):
    rollno = models.CharField(max_length=10, help_text='Student Roll number')
    course_name = models.CharField(max_length=50, help_text='Student ciurse name')
    task_name = models.CharField(max_length=300, help_text='Student task/project name')
    submitted = models.DateTimeField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)
    remarks = models.CharField(max_length=100, help_text='Remarks of the task')
    task_status = models.CharField(max_length=1, choices=task_choice)

    def __str__(self):
        return '{0}'.format(self.rollno)

