from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path(r'accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
