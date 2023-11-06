from django.contrib.auth.models import User
from django.core.management import BaseCommand
from SomeRequests.models import UserRequest


class Command(BaseCommand):
    """
    Creating new request
    """
    def handle(self, *args, **options):
        self.stdout.write('Creating request')
        user = User.objects.get(username='admin')
        user_request = UserRequest.objects.get_or_create(
            title='request_1',
            description='This request created through b_command',
            user=user,
        )
        self.stdout.write(self.style.SUCCESS('Request created'))
