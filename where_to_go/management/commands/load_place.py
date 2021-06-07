from django.core.management.base import BaseCommand
from where_to_go.models import Place, Image
import requests
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Загружает данные из JSON-файлов, на которые вы укажете ссылки'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str)

    def handle(self, *args, **options):
        urls = options['urls']
        for url in urls:
            response = requests.get(url)
            response.raise_for_status()
            place_data = response.json()
            coordinates = place_data["coordinates"]
            image_urls = place_data["imgs"]

            Place.objects.get_or_create(
                title = place_data['title'],
                description_short = place_data['description_short'],
                description_long = place_data['description_long'],
                longtitude = coordinates["lng"],
                latitude = coordinates['lat'],
            )
            
            place = Place.objects.get(title = place_data['title'])

            for image_id, image_url in enumerate (image_urls):
                image_id += 1
                response = requests.get(image_url)
                response.raise_for_status()
                image_binary = response.content
                #image_file = ContentFile(Img.open(BytesIO(image_binary)))
                image_file = ContentFile(image_binary)

                Image.objects.get_or_create(
                    title = f"{str(image_id)} {place.title}",
                    place = place,
                    my_order = image_id,
                )

                image_note = Image.objects.get(title = f"{str(image_id)} {place.title}")
                image_note.image.save(f"{str(image_id)} {place.title}", content=image_file, save=True)
                