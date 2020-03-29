"""diagnospymes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viesw
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
        path('', include('mm_evaluation.urls')),
        path('admin/', admin.site.urls),
        path('login/', auth_views.LoginView.as_view(), name="login"),
        path('logout/', auth_views.logout_then_login, name="logout"),
        path('cambiar_contraseña/', auth_views.PasswordChangeView.as_view(), name="change_password"),
        path('contraseña_cambiada/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
        ]
