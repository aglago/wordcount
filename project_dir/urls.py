"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include # allows to include similar patterns from another module

# come and tell the main project, where to find your apps
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('home_app.urls')) 
    path('', include('home_app.urls')), # makes all the app-specific URL patterns defined in home_app.urls available under the myproject/
    path('wordcount/', include('wordcount.urls')),
]
