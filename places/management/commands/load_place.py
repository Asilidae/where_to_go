import requests
from django.core.management.base import BaseCommand
from io import BytesIO
import uuid

from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('github_api_file_url', type=str)

    def handle(self, *args, **kwargs):
        github_api_file_url = kwargs['github_api_file_url']
        file_response = requests.get(github_api_file_url).json()
        obj, created = Place.objects.get_or_create(
            title=file_response['title'],
            title_short=file_response['title'],
            place_id=file_response['title'],
            description_short=file_response['description_short'],
            description_long=file_response['description_long'],
            lng=file_response['coordinates']['lng'],
            lon=file_response['coordinates']['lat']
        )

        number = 0
        for img_url in file_response['imgs']:
            img = BytesIO(requests.get(img_url).content)
            number += 1
            img_obj, c = Image.objects.get_or_create(
                place=obj,
                number=number
            )
            img_obj.image.save(uuid.uuid4().hex + '.jpg', img, save=True)
