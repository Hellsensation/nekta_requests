from django.urls import path
from .views import (
                    main_page,
                    RequestsView,
                    add_message,
                    get_request_data,
                    request_data,
                    get_message_from_request,
                    request_messages,
                    RequestDataView
)


app_name = 'SomeRequests'

urlpatterns = [
    path('main_page/', main_page, name='main_page'),
    path('requests/', RequestsView.as_view(), name='requests'),
    path('requests/<int:pk>', RequestDataView.as_view(), name='request_data_view'),
    path('add_message/', add_message, name='add_message'),
    path('get_request_data/', get_request_data, name='get_request_data'),
    path('request_data/', request_data, name='request_data'),
    path('get_messages/', get_message_from_request, name='get_messages'),
    path('request_messages/', request_messages, name='request_message'),

]



