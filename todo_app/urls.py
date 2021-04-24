from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('todo_list.urls')),
    path('admin/', admin.site.urls),
]
