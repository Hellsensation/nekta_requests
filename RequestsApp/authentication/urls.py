from django.contrib.auth.views import LoginView
from django.urls import path, include, re_path


app_name = 'authentication'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('login/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
