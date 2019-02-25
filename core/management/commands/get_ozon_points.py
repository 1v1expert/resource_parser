from django.core.management.base import BaseCommand
#from ...models import Points, Gallery, Coordinates, Structured_address
#from django.core.files.storage import default_storage
from django.conf import settings
from core.client import make_api_request
from json.decoder import JSONDecodeError
from core.models import Cars, OzonPoints
import requests

import unicodedata

def save_data(data):
	OzonPoints.objects.all().delete()
	for i in data:
		#print()
		point = OzonPoints(name='Test')
		try:
			point.name = i.get('name')[:250]
		except:
			print('Erros create name')
		try:
			point.address = i.get('address')[:250]
		except:
			print('Erros create address')
		try:
			point.deliveryType = i.get('deliveryType').get('name')[:250]
		except:
			print('Error create type deliveryType')
		try:
			point.metro = i.get('metro')[0].get('name')[:250]
		except:
			print('Error create metro')
		point.save()
		#except:
			#print('Do not to save')
		

class Command(BaseCommand):
	help = 'Generates Fake data'
	
	def handle(self, *args, **options):
		url = 'https://api.ozon.ru/checkout/v7/checkout'
		requests_method = getattr(requests, 'post')
		headers = {
			'authorization': 'Bearer rLJxHzXfIkqxtlt8Gui3',
			#'Origin': 'https://www.ozon.ru',
			'Content-Type': 'application/json',
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
			              'Chrome/39.0.2171.95 Safari/537.36'}
			#'x-o3-app-handler':'Checkout/Checkout',
#'x-o3-app-name': 'ozon_new',
#'X-OZON-ABGROUP': '44'}
		request = {'areaId':2,'balanceAmount':0,'deliveryTypeId':2,'filters':{'itemFields':['info','quantity','seller','price','availability','merchant','feedback','isDeliveryUnavailableItem'],'deliveryFields':['id','name','coordinates','address','deliveryType','metro','provider','deliveryPrice','deliveryDiscountedPrice','useInLastOrders','hasLoyalty','restrictionAccessField','storagePeriod','properties','classInstanceDescription','foreignCustomFeesMessage','splits','timeSlotsAvailable']},'items':[{'id':148296533,'quantity':1}],'options':{'legalUser':False,'rewriteStorage':False,'useStorage':True},'pointsAmount':0,'scope':['delivery','deliveryMethods','deliveryInfo','payment'],'splitGroups':[{'key':'FBO','splits':[{'key':'FBO-1-W3'}]}]}
		get_request = requests_method(url,  headers=headers, json=request)
		if get_request.status_code in (200, 201):
			try:
				message = get_request.json()
				print(message.get('data')['delivery']['deliveryTypes'][0]['deliveryMethods'])
				save_data(message.get('data')['delivery']['deliveryTypes'][0]['deliveryMethods'])
			except JSONDecodeError:
				print(get_request.text)
			except:
				print(get_request.text)
				#return get_request.text
		else:
			print(get_request.text)
		
		session = requests.Session()
		headers['cookie'] = 'incap_ses_379_1101384=vFcsclCzMGKRbKeXiXpCBYTkc1wAAAAA1+mPaDvE2Kj0GTHKm51zyQ==; visid_incap_1101384=TymqMYLcRIu019kVCbOcPYTkc1wAAAAAQUIPAAAAAAA9yQgs02stgP4xQH+R1CCl'

		response = session.get(url='https://www.ozon.ru/checkout', headers=headers)
		print(response.cookies.get_dict())
		#response = response.get(url='https://www.ozon.ru/checkout')
		#print(response.cookies.get_dict())