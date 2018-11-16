
import requests

for i in range (1,26):
    print (i)
    url = "http://www.ivsky.com/tupian/ziranfengguang/index_%d.html" % (i)
    r = requests.get(url)

r = requests.get('http://i-2.shouji56.com/2015/2/11/23dab5c5-336d-4686-9713-ec44d21958e3.jpg', stream = True)

with open('meinv2.jpg', 'wb+') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)

