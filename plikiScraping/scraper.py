from bs4 import BeautifulSoup
import requests
import random
import csv

def scrap(pageLink, shoeCategory):
	global index		

	urlHeaders = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, 			like Gecko) Chrome/74.0.3729.169 Safari/537.36'
	}	

	baseUrl = requests.get(pageLink)
	soup = BeautifulSoup(baseUrl.content, 'lxml')

	productList = soup.find_all('article', class_ = 
	'col-xl-3 col-lg-3 col-md-4 col-sm-4 col-xs-6 infinite_article product-article')

	productLinks = []

	for item in productList:
		for link in item.find_all('a',class_ = 'send-search', href=True):
			productLinks.append(link['href'])

	print(len(productLinks))
		
	for link in productLinks:
		r = requests.get(link, headers = urlHeaders)

		soup = BeautifulSoup(r.content, 'lxml')
		
		shoeBrandAndName = soup.find_all('span', itemprop = 'name')
		shoeBrand = shoeBrandAndName[0].text
		shoeName = shoeBrandAndName[1].text
		shoeSubcategory = soup.find('span', class_ = 'sr-only').text
		shoeCategoryAndSubcategory = shoeCategory + '/' + shoeSubcategory
		shoePrice = soup.find('span', property = 'price').text

		shoeSizeZone = soup.find('ul', class_ = 'sizes')
		shoeSizeList = shoeSizeZone.find_all('li')			
			
		shoeInfoZone = soup.find('div', class_ ="panel-body")
		shoeInfoList = shoeInfoZone.find_all('li')
		shoeInfoString = ''
		for item in shoeInfoList:
			shoeInfoString+= item.text + ' '			
		
		shoeInfoString = shoeInfoString[:-1] #pozbywam się ostatniej spacji
		
		shoeMainPhotoBox = soup.find('div', class_ = 'aniimated-thumbnials')
		shoeMainPhotoLink = shoeMainPhotoBox.find('a')['href']
			
		writerProducts.writerow([index, shoeName, shoeBrand, shoeCategoryAndSubcategory, 						shoePrice, shoeMainPhotoLink, shoeInfoString])
		for size in shoeSizeList:
			shoeQuantity = random.randint(0,50)
			writerSizes.writerow([index, 'Rozmiar:rozmiar:0', size.text, shoeQuantity])

		index+=1
		print(f'{index} saved')

index = 0

fileWithProducts = open('productsList.csv', 'w')
writerProducts = csv.writer(fileWithProducts)
fileWithSizes = open('sizeList.csv', 'w')
writerSizes = csv.writer(fileWithSizes)

writerProducts.writerow(['Index', 'Name', 'BrandName', 'Category/Subcategory', 'Price', 'Info', 			'PhotoAdress'])
writerSizes.writerow(['Product ID', 'Attribute (Name:Type:Position)', 'Value', 'Quantity'])

pageMen = 'https://www.officeshoes.pl/obuwie-buty-meskie/4/48/order_asc?page=1'
pageWomen = 'https://www.officeshoes.pl/obuwie-buty-damskie/1/48/order_asc?page=1'
pageKids = 'https://www.officeshoes.pl/obuwie-buty-dzieciece/10/48/order_asc?page=1'

scrap(pageMen, 'Męskie')
scrap(pageWomen, 'Damskie')
scrap(pageKids, 'Dziecięce')

fileWithProducts.close()
fileWithSizes.close()
