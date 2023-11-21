from django.urls import path
from .views import (
                    main_page,
                    RequestsView,
                    AddMessageView,
                    get_message_from_request,
                    request_messages,
                    RequestDataView
)


app_name = 'SomeRequests'

urlpatterns = [
    path('main_page/', main_page, name='main_page'),
    path('requests/', RequestsView.as_view(), name='requests'),
    path('requests/<int:pk>', RequestDataView.as_view(), name='request_data_view'),
    path('add_message/', AddMessageView.as_view(), name='add_message'),
    path('get_messages/', get_message_from_request, name='get_messages'),
    path('request_messages/', request_messages, name='request_message'),

]



