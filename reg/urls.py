from django.conf.urls import url
from reg import views 

urlpatterns = [
    
    url("register", views.register, name="register"),
    url("login", views.login_request, name="login"),
    url("logout", views.logout_request, name="logout")
]
