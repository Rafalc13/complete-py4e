import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
lib = urllib.request.urlopen(url, context=ctx)
data = lib.read().decode()


info = json.loads(data)
print('Retrieving', len(info), 'characters')
sumx = 0
count = 0
for item in info['comments']:
    num = item['count']
    sumx += int(num)
    count += 1

print('Count:', count)
print('Sum:', sumx)