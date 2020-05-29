import imgkit
from PIL import Image
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        text = '<meta charset="UTF-8"><font size=5>Сергей'
        options = {'format': 'bmp'}
        imgkit.from_string(text, 'out.bmp', options=options)

        img = Image.open('out.bmp')
        img_width, img_height = img.size
        for x in range(0, img_width):
            for y in range(0, img_height):
                r, g, b = img.getpixel((x, y))
                if r < 250 or g < 250 or b < 250:
                    r, g, b = 0, 0, 0
                img.putpixel((x, y), (r, g, b))

        img.save('out.bmp')
