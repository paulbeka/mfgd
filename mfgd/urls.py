"""mfgd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from mfgd_app import views

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import handler404


urlpatterns = [
    path("", views.index, name="index"),
    re_path(
        r"(?P<repo_name>\w+)/view/(?P<oid>\w+)/(?P<path>\S*)", views.view, name="view"
    ),
    re_path(r"(?P<repo_name>\w+)/info/(?P<oid>\w+)/?", views.info, name="info"),
    re_path(r"(?P<repo_name>\w+)/chain/(?P<oid>\w+)/?", views.chain, name="chain"),
    re_path(r"(?P<repo_name>\w+)/manage/?", views.manage_repo, name="manage_repo"),
    path("admin/", admin.site.urls),
    path("logout/", views.user_logout, name="logout"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("manage/", views.manage, name="manage"),
    path("manage/delete_repo/<str:repo_name>/", views.delete_repo, name="delete_repo"),
]

handler404 = views.error_404
handler500 = views.error_500
