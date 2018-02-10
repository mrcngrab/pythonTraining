# import libraries
from bs4 import BeautifulSoup
import urllib3

# specify the url
quote_page = 'https://www.mathem.se/varor/frukt-o-gront'

http = urllib3.PoolManager()

# query the website and return the html to the variable ‘page’
page = http.request('GET', quote_page)

print(page.status)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.data,"html.parser")

# Take out the <div> of name and get its value

produtct_container = soup.find_all('div',class_="priceTest")
print(type(produtct_container))
print(len(produtct_container))
for product in produtct_container:
	product_details = product.find_all('div',recursive=False)
	product_name = product_details[1]
	print(product_name.text)
	
#first_product = produtct_container[0]
#first_product_elements = first_product.find_all('div',recursive=False)
#print(len(first_product_elements))
#details = first_product_elements[1]
#print(details.text)

