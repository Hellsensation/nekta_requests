from django.urls import path
from .views import main_page, view_requests, create_request, add_message, create_request2

app_name = 'SomeRequests'

urlpatterns = [
    path('main_page/', main_page, name='main_page'),
    path('requests/', view_requests, name='requests'),
    path('create_request/', create_request, name='create_request'),
    path('add_message/', add_message, name='add_message'),
    path('create_request2/', create_request2, name='create_request2')
]


