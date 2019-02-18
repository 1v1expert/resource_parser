from django.core.management.base import BaseCommand
#from ...models import Points, Gallery, Coordinates, Structured_address
#from django.core.files.storage import default_storage
from django.conf import settings
from core.client import make_api_request
from json.decoder import JSONDecodeError
from core.models import Cars

import unicodedata

class Command(BaseCommand):
	help = 'Generates Fake data'
	
	def handle(self, *args, **options):
		get_request = make_api_request()
		if get_request.status_code in (200, 201):
			try:
				message = get_request.json()
			except JSONDecodeError:
				return get_request.text
		if 'message' in locals():
			items = message.get('items')
			for item in items:
				car = Cars()
				car.idd = item.get('id')
				car.url = item.get('url')[:250]
				car.category = item.get('category')
				car.hasDamage = item.get('hasDamage')
				car.price = unicodedata.normalize("NFKD", item.get('price').get('grs').get('localized'))
				car.title = item.get('title')
				car.created = item.get('created')
				car.modified = item.get('modified')
				car.renewed = item.get('renewed')
				car.features = ';'.join([unicodedata.normalize("NFKD", word) for word in item.get('features')])[:750]
				car.details = ';'.join([unicodedata.normalize("NFKD", word) for word in item.get('details')])[:750]
				car.attr = str(item.get('attr'))[:750]
				car.save()
		
