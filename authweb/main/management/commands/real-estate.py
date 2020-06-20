from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from authweb.realestate.helpers import do_real_estate_demo_reset
        do_real_estate_demo_reset()


