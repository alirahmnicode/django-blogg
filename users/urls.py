from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView
from .views import UserLoginView, UserLogoutView , UserRegisterView , SearchUsernameView 


app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("signup/", UserRegisterView.as_view(), name="signup"),
    path("search/<str:username>/", SearchUsernameView.as_view(), name="search"),
]
  