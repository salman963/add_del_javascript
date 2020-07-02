"""facebook URL Configuration

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
from django.urls import path
from mainapp.views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',library.pages,name='pages'),
    path('BookAdd',library.BookAdd,name='BookAdd'),
    path('showBooks',library.showBooks,name='showBooks'),
    path('deleteBook',library.deleteBook,name='deleteBook'),
    path('signUp',library.signUp,name='signUp'),
    path('signup_request',library.signup_req,name='signup_request'),
    path('validMail',library.valid_mail,name='validMail'),

    path('api/',test_api.as_view(),name='api'),
    path('crudApi',crudApi.as_view(),name='crudApi'),
    path('updateApi/<int:pk>',updateApi.as_view(),name='updateApi')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
