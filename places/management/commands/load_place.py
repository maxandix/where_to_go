from pathlib import Path
from urllib.parse import unquote

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, *args, **options):
        for url in options['urls']:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            place, created = Place.objects.get_or_create(
                title=data['title'],
                description_short=data['description_short'],
                description_long=data['description_long'],
                lat=data['coordinates']['lat'],
                lon=data['coordinates']['lng'],
            )

            for index, img_url in enumerate(data['imgs']):
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                content_file = ContentFile(img_response.content)
                new_image = Image()
                new_image.img.save(parse_img_name(img_url), content_file, save=False)
                new_image.place = place
                new_image.position = index
                new_image.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully loaded url "{url}"'))


def parse_img_name(url):
    return Path(unquote(url)).name
