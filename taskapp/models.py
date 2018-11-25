from django.db import models
import datetime
# Create your models here.

class Task(models.Model):
    rollno = models.CharField(max_length=10, help_text='Student Roll number')
    course_name = models.CharField(max_length=50, help_text='Student ciurse name')
    task_name = models.CharField(max_length=300, help_text='Student task/project name')
    submitted = models.DateTimeField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)

    def __str__(self):
        return '{0}'.format(self.rollno)

