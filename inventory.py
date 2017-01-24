import requests, json, ConfigParser, os, collections
from colours import *



PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
c = ConfigParser.ConfigParser()
configFilePath = os.path.join(PROJECT_ROOT_DIR + '/adidas_monitor-master', 'config.cfg')
c.read(configFilePath)
 
sku = c.get("Preferences", "Item_Sku")
client_id = c.get("Preferences", "client_Id")

def get_inventory(sku):

	headers = {'user-agent' : 'Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'}
	session = requests.Session()
	session.verify = False
	session.cookies.clear()

	url = ('http://{0}-store-adidasgroup.demandware.net/s/adidas-{1}'
		'/dw/shop/v15_6/products/({2})'
            '?client_id={3}&expand=availability,variations,prices'
        ).format('production', 'GB', sku, client_id,)

	return session.get(url=url, headers=headers)



def get_variant_inventory(sku):

	headers = {'user-agent' : 'Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'}
	session = requests.Session()
	session.verify = False
	session.cookies.clear()

   	url = ('http://www.{0}/on/demandware.store/Sites-adidas-'
    '{1}-Site/MLT/Product-GetVariants?pid={2}').format('adidas.co.uk', 'GB', sku,)

	return session.get(url=url, headers=headers)



def organise_product_data(json_data):
	product_name = ''
	product_colour = ''

	data = json_data['data'][0]


	product_name = data['name']
	product_colour = data['c_defaultColor']
	stock_level = data['inventory']['ats']


	return product_name, product_colour, stock_level



def organise_variant_data(json_data):
	'''
	Sort the data received from requests!
	'''

	## Initialize dictionaries for future use
	product_info = {}
	product_size_stocks = {}
	product_size_ids = {}

 	## Parse JSON for PID
	product_info['Pid'] = json_data['variations']['variants'][0]['articleNo']

	##Parse JSON for Price
	product_info['price'] = json_data['variations']['variants'][0]['pricing']['standard']

	##Parse JSON for amount of sizes sold
	product_info['size_count'] = len(json_data['variations']['variants'])


	##Parse and count how many of sizes are in stock
	size_in_stock = 0
	for item in json_data['variations']['variants']:
		if item['avLevels']['IN_STOCK'] != 0:
			size_in_stock += 1
	product_info['size_count_instock'] = size_in_stock



	##Parse for stock for each size
	for item in json_data['variations']['variants']:
		product_size_stocks[str(item['attributes']['size'])] = int(item['ATS'])

	
	##Parse for Size ID
	for size in product_size_stocks:
		for item in json_data['variations']['variants']:
			if size == item['attributes']['size']:
				product_size_ids[size] = item['id']


	return 	product_info, product_size_stocks, product_size_ids

	# product_info['size_count_instock'] = 



def organise_size_data(json_data):

	item_size_dictionary = {}
	item_Pid_dictionary = {}
	size_list = []

	for item in json_data['variations']['variants']:
		item_size_dictionary[str(item['attributes']['size'])] = int(item['ATS'])
		size_list.append(str(item['attributes']['size']))

	# for key,value in item_size_dictionary.iteritems():
	# 	print key + ' ' +  value

	for key in item_size_dictionary:
		for item in json_data['variations']['variants']:
			if key == item['attributes']['size']:
				item_Pid_dictionary[key] = item['id']

	# for key in item_size_dictionary:
	# 	print 'Size ---' + key
	# 	print 'PID ---' + item_Pid_dictionary[key]
	# 	print 'stock---' + item_size_dictionary[key] 
	# 	print
	return item_size_dictionary, item_Pid_dictionary, size_list


product_response = get_inventory(sku)
product_data = product_response.json()
product_name, product_colour, product_stock = organise_product_data(product_data)


variant_response = get_variant_inventory(sku)
variant_data = variant_response.json()
product_info, product_size_stocks, product_size_ids = organise_variant_data(variant_data)
size_stock_dictionary, size_pid_dictionary, size_list = organise_size_data(variant_data)



organise_size_data(variant_data)
print
print
print
print
print
print
print

print pi_('Name ----- ' + product_name)
print pi_('Product Colour ----- ' + product_colour)
print pi_('Product Stock ----- ' + str(product_stock))
print pi_('Product ID ----- ' + product_info['Pid'])
print pi_()
print pi_('Price ----- ' + product_info['price'])
print pi_('Number of sizes available ----- ' + str(product_info['size_count']))
print pi_('Number of sizes in stock ----- ' + str(product_info['size_count_instock']))
	
print
print
print
print
print
print
print

input = raw_input(pi_('Would you like to view the stock for each size? Y/N'))

print
print
print
print

if input == 'y' or input == 'Y':
	for size in size_list:
		print pi_('Size ----- ' + size)
		print pi_('Stock ----- ' + str(size_stock_dictionary[size]))
		print pi_('Variant Pid -----' + size_pid_dictionary[size])
		print 
		print

	print pi_("Thank you for using Yelax's stock checker")


else:
	print pi_("Thank you for using Yelax's stock checker")





##To do
## Email or sms notifs

