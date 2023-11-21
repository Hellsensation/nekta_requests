from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View

from .models import UserRequest, RequestMessage
from .forms import RequestForm, MessageForm


def main_page(request: HttpRequest) -> HttpResponse:
    """Представление главной страницы"""
    return render(request, 'SomeRequests/main_page.html')


class RequestsView(View):
    """Представление списка заявок"""
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': RequestForm(),
            'requests': UserRequest.objects.all()
        }
        return render(request, 'SomeRequests/view_requests.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        req_data = RequestForm(request.POST)
        if req_data.is_valid():
            req_data.save()
            url = reverse('SomeRequests:requests')
            return redirect(url)


class RequestDataView(View):
    """Представление информации о заявке"""
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        request_id = get_object_or_404(UserRequest, pk=pk)
        context = {
            'request_id': request_id,
        }
        return render(request, 'SomeRequests/request-details.html', context=context)


class AddMessageView(View):
    """Добавление сообщения в заявку"""
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'form': MessageForm
        }
        return render(request, 'SomeRequests/add_message.html', context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        req_data = MessageForm(request.POST)
        if req_data.is_valid():
            req_data.save()
            url = reverse('SomeRequests:requests')
            return redirect(url)


def get_message_from_request(request: HttpRequest) -> HttpResponse:
    """Запрос на получение сообщений из заявки по ее ID """
    return render(request, 'SomeRequests/get_message_from_request.html')


def request_messages(request: HttpRequest) -> HttpResponse:
    """Выдача сообщений из заявки"""
    request_id = request.GET.get('message-id')
    print(request_id)
    messages = RequestMessage.objects.filter(user_request_id=request_id)

    context = {
        'messages': messages
    }
    return render(request, 'SomeRequests/request_messages.html', context=context)

# def create_request(request: HttpRequest) -> HttpResponse:
#     """Создание заявки"""
#     if request.method == 'POST':
#         request_data = RequestForm(request.POST)
#         if request_data.is_valid():
#             request_data.save()
#             url = reverse('SomeRequests:requests')
#             return redirect(url)
#
#     else:
#         request_data = RequestForm()
#
#     user = User.objects.all()
#     context = {
#         'request_data': request_data,
#         'user': user
#     }
#
#     return render(request, 'SomeRequests/create_request.html', context=context)

# def add_message(request: HttpRequest) -> HttpResponse:
#     """Добавление сообщения в заявку"""
#     if request.method == 'POST':
#         message_data = MessageForm(request.POST)
#         if message_data.is_valid():
#             message_data.save()
#             url = reverse('SomeRequests:requests')
#             return redirect(url)
#     else:
#         message_data = MessageForm()
#
#     requests = UserRequest.objects.all()
#     context = {
#         'message_data': message_data,
#         'requests': requests,
#         }
#     return render(request, 'SomeRequests/add_message.html', context=context)

# def get_request_data(request: HttpRequest) -> HttpResponse:
#     """Запрос на получение данных о заявке по ее ID"""
#     return render(request, 'SomeRequests/get_request_data.html')
#
#
# def request_data(request: HttpRequest) -> HttpResponse:
#     """Выдача информации о заявке"""
#     request_id = request.GET.get('id')
#     if request_id:
#         request_data = get_object_or_404(UserRequest, pk=request_id)
#         messages = RequestMessage.objects.filter(user_request=request_id)
#         message_count = len(messages)
#         context = {
#             'request_data': request_data,
#             'request_messages': message_count
#         }
#         return render(request, 'SomeRequests/request_data.html', context=context)
#     return HttpResponse("Nothing in input")