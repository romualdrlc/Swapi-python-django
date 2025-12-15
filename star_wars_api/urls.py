"""
URL configuration for star_wars_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from peoples.views import people_detail, people_list
from planets.views import planet_list, planet_detail
from .views import home, clear_swapi_cache

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  
    path('peoples/', people_list, name='people_list'),
    path('planets/', planet_list, name='planet_list'),
    path('people/<int:people_id>/', people_detail, name='people_detail'),
    path('planet/<int:planet_id>/', planet_detail, name='planet_detail'),
    path('clear_cache/', clear_swapi_cache, name='clear_swapi_cache'),
]
