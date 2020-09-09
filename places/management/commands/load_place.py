import requests
from django.core.management.base import BaseCommand
from io import BytesIO
import uuid

from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('github_api_file_url', type=str)

    def create_new_place(self, file_response):
        file_response = file_response.json()
        obj, created = Place.objects.get_or_create(
            title=file_response['title'],
            title_short=file_response['title'],
            place_id=file_response['title'],
            description_short=file_response['description_short'],
            description_long=file_response['description_long'],
            lng=file_response['coordinates']['lng'],
            lon=file_response['coordinates']['lat']
        )

        images = file_response['imgs']
        for number, img_url in enumerate(images, 1):
            img = BytesIO(requests.get(img_url).content)
            img_obj, _ = Image.objects.get_or_create(
                place=obj,
                number=number
            )
            img_obj.image.save(uuid.uuid4().hex + '.jpg', img, save=True)

    def handle(self, *args, **kwargs):
        github_api_file_url = kwargs['github_api_file_url']
        file_response = requests.get(github_api_file_url)

        if file_response.status_code == 200:
            self.create_new_place(file_response)
            print('Success!')
        elif file_response.status_code == 404:
            print('Not Found!')
        elif file_response.status_code == 401:
            print('Unauthorized!')
