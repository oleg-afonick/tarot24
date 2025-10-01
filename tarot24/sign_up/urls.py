from django.contrib.auth.views import LoginView, LogoutView,TemplateView
from django.urls import path

from .views import SignupView


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='sign_up/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirm/logout/', TemplateView.as_view(template_name='sign_up/logout.html'), name='confirm_logout'),
]
