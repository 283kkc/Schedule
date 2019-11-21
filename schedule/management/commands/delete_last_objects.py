from django.core.management.base import BaseCommand, CommandError

from schedule.models import *

# for cypress test
class Command(BaseCommand):
    help = "Type model names to delete last object.(Like: User CmsUser, \
    Their last objects will be deleted)"

    def add_arguments(self, parser):
        parser.add_argument('model_name',
                            nargs='+',
                            type=str,
                            help='type model names')

    def handle(self, *args, **options):
        success = ""
        error = ""
        for model_name in options['model_name']:
            try:
                object = getattr(models, model_name).objects.last()
                success += (f'{model_name}: {object}\n')
                object.delete()
            except Exception as e:
                error += (f'{model_name}: {e}\n')

        self.stdout.write(
            self.style.SUCCESS(f'Deleted[\n{success}]'))
        if error != "":
            self.stdout.write(
                self.style.WARNING(f'Error[\n{error}]'))
