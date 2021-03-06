"""streetjammin URL Configuration

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
from django.conf.urls import include, url
from qr_code import urls as qr_code_urls
from jammin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('upload/', views.uploadSongs, name="upload"),
    path('logout/', views.logout_view, name="logout"),
    path('list/', views.mySongs, name="list"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/login/', views.login, name="login"),
    path('accounts/signup/', views.signup, name="signup"),
    path('qrcode_generator/song<int:sid>', views.qrcode, name="qrcode_generator"),
    path('download/<int:did>/', views.download, name='download'),
    url(r'^qr_code/', include(qr_code_urls, namespace="qr_code")),
]
