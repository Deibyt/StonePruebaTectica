from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class Command(BaseCommand):
    help = 'Generate JWT tokens for different roles'

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            token = RefreshToken.for_user(user)
            roles = ','.join(group.name for group in user.groups.all())
            self.stdout.write(self.style.SUCCESS(f"Token for {user.username} (Roles: {roles}):"))
            self.stdout.write(str(token.access_token))
