from django.urls import path

from apps.views import TestTemplateView, EmailView, VerifyView, RegisterFormView, LoginFormView, LogoutView

urlpatterns = [
    path('', TestTemplateView.as_view(), name='home'),
    path('login', LoginFormView.as_view(), name='login'),
    path('email', EmailView.as_view(), name='email'),
    path('verify', VerifyView.as_view(), name='verify'),
    path('register', RegisterFormView.as_view(), name='register'),
    path('loguyr', LogoutView.as_view(), name='logout'),
]