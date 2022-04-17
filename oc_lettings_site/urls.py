from django.contrib import admin
from django.urls import path

import lettings.views
import profiles.views
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', lettings.views.index, name='lettings'),
    path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
    path('profiles/', profiles.views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('admin/', admin.site.urls)
]
