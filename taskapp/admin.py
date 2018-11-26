from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.
from .models import Task
import datetime
admin.site.disable_action('delete_selected') # removed all delete actions

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['username', 'course_name', 'task_name','file', 'submitted', 'last_date']
    fields = ['username','course_name' , 'remarks', 'task_status']
    list_editable = ['task_name','file']

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    def save_model(self, request, obj, form, change):

        auser = User.objects.get(pk=obj.username.pk)
        auser.is_staff = True
        auser.save()

        group_student = Group.objects.get(name='student')
        auser.groups.add(group_student)

        if not request.user.is_superuser:
            obj.submitted = datetime.datetime.now()
            obj.save()

        super(TaskAdmin, self).save_model(request, obj, form, change)



    def get_queryset(self, request):
        qs = super(TaskAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(username = request.user)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return 'username','course_name' , 'remarks', 'task_status'
        else:
            return  'task_name', 'remarks',

    def get_list_display_links(self, request, list_display):
        if request.user.is_superuser:
            return 'username'
        else:
            return None

