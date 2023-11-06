from django.contrib import admin

from .models import UserRequest, RequestMessage


admin.site.register(UserRequest)
admin.site.register(RequestMessage)
