from django.contrib.auth.views import LoginView
from django.urls import path
#from .views import login_view

app_name = 'authentication'


urlpatterns = [
    #path('login/', login_view, name='login'),
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login')

]
