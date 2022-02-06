import csv

from django.core.management import BaseCommand

from adjust.serializers import AdjustSerializer


class Command(BaseCommand):
    help = "Imports sample data from CSV."

    def add_arguments(self, parser):
        parser.add_argument("csv", type=str)

    def handle(self, *args, **options):
        csv_path = options["csv"]
        with open(csv_path) as import_data:
            for row in csv.DictReader(import_data):
                serialized = AdjustSerializer(data=row)
                serialized.is_valid(raise_exception=True)
                serialized.save()
