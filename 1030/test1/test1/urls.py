from django.contrib import admin
from django.urls import path
from django.urls import re_path
from course.views import show

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^course/(?P<SID>.{3})/(?P<CID>.{3})/$', show, name='show')
]