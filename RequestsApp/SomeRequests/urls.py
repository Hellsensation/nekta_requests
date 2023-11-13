from django.urls import path
from .views import (main_page,
                    view_requests,
                    create_request,
                    add_message,
                    get_request_data,
                    request_data,
                    get_message_from_request,
                    request_messages)


app_name = 'SomeRequests'

urlpatterns = [
    path('main_page/', main_page, name='main_page'),
    path('requests/', view_requests, name='requests'),
    path('add_message/', add_message, name='add_message'),
    path('create_request/', create_request, name='create_request'),
    path('get_request_data/', get_request_data, name='get_request_data'),
    path('request_data/', request_data, name='request_data'),
    path('get_messages/', get_message_from_request, name='get_messages'),
    path('request_messages/', request_messages, name='request_message'),
]



