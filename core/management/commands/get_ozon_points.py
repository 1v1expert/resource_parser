from django.core.management.base import BaseCommand
#from ...models import Points, Gallery, Coordinates, Structured_address
#from django.core.files.storage import default_storage
from django.conf import settings
from core.client import make_api_request
from json.decoder import JSONDecodeError
from core.models import Cars, OzonPoints
import requests
import json

import unicodedata

# Московская обалсть:

area_list = [{"areaId":45,"name":"Жуковский","city":"Жуковский","countryId":1,"countryCode":"RUS","country":"Россия","fias":"fd91f393-4820-437f-a50c-907e9856c374","geoCoordinate":{"latitude":55.599803,"longitude":38.1224298},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Жуковский, Московская область","region":"Московская область"},{"areaId":69920,"name":"Климовск","city":"Климовск","countryId":1,"countryCode":"RUS","country":"Россия","fias":"5a11404e-3a4f-4943-b60c-51480729dcfb","geoCoordinate":{"latitude":55.3749442,"longitude":37.5389975},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Климовск, Московская область","region":"Московская область"},{"areaId":120,"name":"Озеры","city":"Озеры","countryId":1,"countryCode":"RUS","country":"Россия","fias":"e778b800-b432-4150-82fd-d415911fb700","geoCoordinate":{"latitude":54.8541006,"longitude":38.5599196},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Озеры, Московская область","region":"Московская область"},{"areaId":170,"name":"Мытищи","city":"Мытищи","countryId":1,"countryCode":"RUS","country":"Россия","fias":"5f290be7-14ff-4ccd-8bc8-2871a9ca9d5f","geoCoordinate":{"latitude":55.9105782,"longitude":37.7363579},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Мытищи, Московская область","region":"Московская область"},{"areaId":708,"name":"Опалиха","city":"Опалиха","countryId":1,"countryCode":"RUS","country":"Россия","fias":"63fcf18a-365e-451f-baee-8d09ac50b773","geoCoordinate":{"latitude":55.8317203,"longitude":37.3295266},"areaType":11,"timeZoneUtc":"UTC+3","fullName":"Опалиха, Красногорск, Московская область","district":"Красногорск","region":"Красногорск, Московская область"},{"areaId":60,"name":"Егорьевск","city":"Егорьевск","countryId":1,"countryCode":"RUS","country":"Россия","fias":"17a3426e-add6-4b2e-b4b1-6f36da02b6ab","geoCoordinate":{"latitude":55.3830113,"longitude":39.0358317},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Егорьевск, Московская область","region":"Московская область"},{"areaId":188,"name":"Королев","city":"Королев","countryId":1,"countryCode":"RUS","country":"Россия","fias":"819d6910-b4d1-474f-ad10-c1fa944dfca4","geoCoordinate":{"latitude":55.9161773,"longitude":37.8545415},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Королев, Московская область","region":"Московская область"},{"areaId":617,"name":"Руза","city":"Руза","countryId":1,"countryCode":"RUS","country":"Россия","fias":"9e6c2327-d7ee-49b1-b36c-0bfc0eb5f145","geoCoordinate":{"latitude":55.7014744,"longitude":36.1959206},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Руза, Московская область","region":"Московская область"},{"areaId":543,"name":"Кашира","city":"Кашира","countryId":1,"countryCode":"RUS","country":"Россия","fias":"45b3f9ac-43cd-4bd0-90af-74cf64ea67f7","geoCoordinate":{"latitude":54.853337,"longitude":38.1904392},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Кашира, Московская область","region":"Московская область"},{"areaId":463,"name":"Павловский Посад","city":"Павловский Посад","countryId":1,"countryCode":"RUS","country":"Россия","fias":"bb464d94-30bf-4cf8-a320-905733fa67e2","geoCoordinate":{"latitude":55.779393,"longitude":38.651318},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Павловский Посад, Московская область","region":"Московская область"},{"areaId":642,"name":"Звенигород","city":"Звенигород","countryId":1,"countryCode":"RUS","country":"Россия","fias":"4bae8c68-e107-4352-9d4b-f937f90469ac","geoCoordinate":{"latitude":55.7297089,"longitude":36.8554029},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Звенигород, Московская область","region":"Московская область"},{"areaId":147,"name":"Шатура","city":"Шатура","countryId":1,"countryCode":"RUS","country":"Россия","fias":"cd6486b7-fd7a-4da8-b7f3-420d6e16b07b","geoCoordinate":{"latitude":55.577739,"longitude":39.544477},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Шатура, Московская область","region":"Московская область"},{"areaId":44,"name":"Бронницы","city":"Бронницы","countryId":1,"countryCode":"RUS","country":"Россия","fias":"582fae29-5955-4dba-9f77-ebf9a8e60827","geoCoordinate":{"latitude":55.4255379,"longitude":38.264145},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Бронницы, Московская область","region":"Московская область"},{"areaId":427,"name":"Протвино","city":"Протвино","countryId":1,"countryCode":"RUS","country":"Россия","fias":"9990bc45-c7c1-407e-bdd2-5526e4f742d2","geoCoordinate":{"latitude":54.870621,"longitude":37.218316},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Протвино, Московская область","region":"Московская область"},{"areaId":615,"name":"Краснознаменск","city":"Краснознаменск","countryId":1,"countryCode":"RUS","country":"Россия","fias":"6e8a99b2-e6bd-4169-acb3-f7e6cd53be3b","geoCoordinate":{"latitude":55.5978959,"longitude":37.0393709},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Краснознаменск, Московская область","region":"Московская область"},{"areaId":517,"name":"Ступино","city":"Ступино","countryId":1,"countryCode":"RUS","country":"Россия","fias":"f516f0a9-3882-42fb-ae68-87a433e83e06","geoCoordinate":{"latitude":54.9238928,"longitude":38.1186623},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Ступино, Московская область","region":"Московская область"},{"areaId":449,"name":"Черноголовка","city":"Черноголовка","countryId":1,"countryCode":"RUS","country":"Россия","fias":"70c5b1c8-43ec-471f-b3df-fd6f60557332","geoCoordinate":{"latitude":56.0100707,"longitude":38.3792047},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Черноголовка, Московская область","region":"Московская область"},{"areaId":698,"name":"Красногорск","city":"Красногорск","countryId":1,"countryCode":"RUS","country":"Россия","fias":"63fcf18a-365e-451f-baee-8d09ac50b773","geoCoordinate":{"latitude":55.8317203,"longitude":37.3295266},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Красногорск, Московская область","region":"Московская область"},{"areaId":79,"name":"Коломна","city":"Коломна","countryId":1,"countryCode":"RUS","country":"Россия","fias":"b367fb03-29f9-4dac-8d85-01595cfb6ad9","geoCoordinate":{"latitude":55.102814,"longitude":38.7531002},"areaType":4,"timeZoneUtc":"UTC+3","fullName":"Коломна, Московская область","region":"Московская область"}]



def save_data(data):
	#OzonPoints.objects.all().delete()
	for i in data:
		print(data)
		
		point, create = OzonPoints.objects.get_or_create(idd=i.get('id'),
		                                 defaults={
			                                 "name": i.get('name')[:250],
			                                 "address": i.get('address')[:250],
			                                 #"deliveryType": i.get('deliveryType').get('name')[:250]
		                                 })
		#print(point, create)
		if create:
			try:
				point.metro = i.get('metro')[:250]
				point.save()
			except:
				print('Error create metro')
				


def get_data(areaId=2, token='cWwN7QB86Ei9ExsJD8cx'):
	url = 'https://api.ozon.ru/checkout/v7/checkout'
	url2 = 'https://www.ozon.ru/json/pvzservice.asmx/getbyareaid'
	requests_method = getattr(requests, 'post')
	headers = {'authorization': 'Bearer {}'.format(token),  # 'Origin': 'https://www.ozon.ru',
		'Content-Type': 'application/json',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
		              'Chrome/39.0.2171.95 Safari/537.36'}
	# 'x-o3-app-handler':'Checkout/Checkout',
	# 'x-o3-app-name': 'ozon_new',
	# 'X-OZON-ABGROUP': '44'}
	request2 = {"areaId": areaId}
	request = {'areaId': areaId, 'balanceAmount': 0, 'deliveryTypeId': 2, 'filters': {
		'itemFields': ['info', 'quantity', 'seller', 'price', 'availability', 'merchant', 'feedback',
		               'isDeliveryUnavailableItem'],
		'deliveryFields': ['id', 'name', 'coordinates', 'address', 'deliveryType', 'metro', 'provider', 'deliveryPrice',
		                   'deliveryDiscountedPrice', 'useInLastOrders', 'hasLoyalty', 'restrictionAccessField',
		                   'storagePeriod', 'properties', 'classInstanceDescription', 'foreignCustomFeesMessage',
		                   'splits', 'timeSlotsAvailable']}, 'items': [{'id': 148296533, 'quantity': 1}],
	           'options': {'legalUser': False, 'rewriteStorage': False, 'useStorage': True}, 'pointsAmount': 0,
	           'scope': ['delivery', 'deliveryMethods', 'deliveryInfo', 'payment'],
	           'splitGroups': [{'key': 'FBO', 'splits': [{'key': 'FBO-1-W3'}]}]}
	get_request = requests_method(url2, headers=headers, json=request2)
	if get_request.status_code in (200, 201):
		message = get_request.json()
		flag = True
		try:
			data = json.loads(message.get('d', None).get('data'))
			print(data)#, message)
			#data = message.get('data')['delivery']['deliveryTypes'][0]
		except:
			flag = False
			print('no data')
			
		if flag:
			save_data(data)
		# try:
		# 	message = get_request.json()
		# 	#print(message.get('data')['delivery']['deliveryTypes'][0]['deliveryMethods'])
		# 	save_data(message.get('data')['delivery']['deliveryTypes'][0]['deliveryMethods'])
		# except JSONDecodeError:
		# 	print(get_request.text)
		# 	return get_request.text
		# except:
		# 	print(message.get('data')['delivery']['deliveryTypes'])
		# 	return get_request.text  # return get_request.text
	else:
		return get_request.text
	
	#session = requests.Session()
	#headers[
	#	'cookie'] = 'incap_ses_379_1101384=vFcsclCzMGKRbKeXiXpCBYTkc1wAAAAA1+mPaDvE2Kj0GTHKm51zyQ==; visid_incap_1101384=TymqMYLcRIu019kVCbOcPYTkc1wAAAAAQUIPAAAAAAA9yQgs02stgP4xQH+R1CCl'
	
	#response = session.get(url='https://www.ozon.ru/checkout', headers=headers)
	#print(response.cookies.get_dict())


# response = response.get(url='https://www.ozon.ru/checkout')
# print(response.cookies.get_dict())

class Command(BaseCommand):
	help = 'Generates Fake data'
	
	def handle(self, *args, **options):
		OzonPoints.objects.all().delete()
		token = input('Entered token: ')
		for area in area_list:
			get_data(area.get('areaId', None), token)
		get_data(2, token)

			#print(area.get('areaId', None))
		
		