"""ksxx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from show import views as show_view
import django_cas_ng.views  # 导入模块

urlpatterns = [
    url(r'^accounts/login', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),  # 认证跳转
    url(r'^accounts/logout', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),  # 注销
    url(r'test/', show_view.login_test),
    url(r'^admin/', admin.site.urls),
    url(r'api', show_view.api),
    url(r'^$', show_view.show, name="show_view_show"),

]
