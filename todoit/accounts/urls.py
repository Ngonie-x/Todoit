from django.urls import path
from .views import user_login, register, home
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    # Temporary home
    path('', home, name='home' ),


    path("login/", user_login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path("register/", register, name="register")
]
