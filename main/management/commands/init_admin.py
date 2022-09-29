from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            admin = User.objects.create_superuser('admin@school.org.br', password='adminschool')
            admin.save()
        except IntegrityError:
            print('Admin já existe')
