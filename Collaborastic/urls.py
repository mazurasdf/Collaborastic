"""Collaborastic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from backend import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^api/test/$', views.test),
    # re_path(r'^api/users/$', views.all_users)
    path('api/test/', views.test),
    path('api/users/', views.all_users),
    path('api/users/create/', views.create_user),
    path('api/users/<int:user_id>/delete/', views.delete_user),
    path('api/users/<int:user_id>/edit/', views.edit_user),
    path('api/users/<int:user_id>/', views.show_single_user),
    path('api/event_jobs/', views.all_event_jobs),
    path('api/event_jobs/create/', views.create_event_job)
]
