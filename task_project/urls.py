"""task_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from taskapp import views as taskviews
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^rajagiri/', admin.site.urls),
    url(r'^$', taskviews.home, name='home'),
    url(r'^task_edit/(?P<pk>\d+)$', taskviews.task_edit, name='task_edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# media settings path.....
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'TASK MANAGEMENT SYSTEM'

admin.site.site_title = "PROJECT"
admin.site.index_title = "PROJECT"
