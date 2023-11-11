from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span', class_="comments")
count = len(tags)
sumx = 0
for tag in tags:
	num = tag.contents[0]
	#print('keke',num)
	sumx += int(num)

print('Count', count)
print('Sum', sumx)
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

#http://py4e-data.dr-chuck.net/comments_42.html
#http://py4e-data.dr-chuck.net/comments_1921401.html
