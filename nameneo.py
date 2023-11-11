import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter starting URL: ')

# Get user input for count and position
position = int(input('Enter position: '))
count = int(input('Enter repetitions: '))


for _ in range(count):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	link = tags[position - 1].get('href', None)
	url = link
	last_name = url.split('/')[-1].split('.')[0].split('_')[2]

print('Last name in sequence:', last_name)
