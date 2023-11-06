from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, reverse, redirect
from .models import UserRequest
from .forms import RequestForm


def main_page(request: HttpRequest):
    return render(request, 'SomeRequests/main_page.html')


def view_requests(request: HttpRequest):
    context = {
        'requests': UserRequest.objects.all()
    }
    return render(request, 'SomeRequests/view_requests.html', context=context)


def create_request(request: HttpRequest):
    if request.method == 'POST':
        user = User.objects.get(username='admin')
        req = UserRequest()
        req.title = request.POST.get('request_title', '')
        req.description = request.POST.get('request_description', '')
        req.user = user
        req.save()

        url = reverse('SomeRequests:requests')
        return redirect(url)

    return render(request, 'SomeRequests/create_request.html')


def create_request2(request):
    if request.method == 'POST':
        request_data = RequestForm(request.POST)
        if request_data.is_valid():
            request_data.save()
            url = reverse('SomeRequests:requests')
            return redirect(url)

    else:
        request_data = RequestForm()

    user = User.objects.all()
    context = {
        'request_data': request_data,
        'user': user
    }

    return render(request, 'SomeRequests/create_request_2.html', context=context)


def add_message(request: HttpRequest) -> HttpResponse:
    context = {

    }
    return render(request, 'SomeRequests/add_message.html', context=context)
