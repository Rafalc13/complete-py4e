import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter URL: ')
    if len(url) < 1: break
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    sumx = 0
    count = 0
    for c in counts:
        num = c.text
        sumx += int(num)
        count += 1
    print('Count', count)
    print('Sum: ', sumx)

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1921403.xml (Sum ends with 92)