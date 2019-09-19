"""Lesson4prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from less4App import views

from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('create', views.create),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('send',views.email,name='send'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register,name='register'),

    path('listdept',views.listdept,name='listdept'),
    path('createdept',views.createdept,name='create'),
    path('editDept/<int:id>', views.editDept),
    path('updateDept/<int:id>', views.updateDept),
    path('deleteDept/<int:id>', views.destroyDept),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
