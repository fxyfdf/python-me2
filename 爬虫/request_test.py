import requests
import json
from PIL import Image
from io import BytesIO

url = 'http://www.baidu.com'
r = requests.get(url)
# print (r.status_code)
# print (r.text)
# print (r.encoding)
# print (dir(r))

# 传参数http://aaa.com?pageId=content
params = {'k1': 'v1', 'k2': 'v2'}
# r = requests.get('http://httpbin.org/get', params)
# print(r.url)

# 二进制数据
r = requests.get('https://goss1.veer.com/creative/vcg/veer/612/veer-142468260.jpg')
# r.content  二进制数据
# image = Image.open(BytesIO(r.content))
# image.save('meinv1.jpg')

# json 处理
#
# r = requests.get('https://github.com/timeline.json')
# print(type(r.json))
# print(r.json)
# print(r.text)

# 原始数据处理
# 把数据保存在 meinv3.jpg  中
# r = requests.get('http://b.hiphotos.baidu.com/image/h%3D300/sign=5e56cb4c4fa7d933a0a8e2739d4ad194/6f061d950a7b02082a11ceb96fd9f2d3562cc88a.jpg', stream = True)
# with open('meinv3.jpg', 'wb+') as f:
#     for chunk in r.iter_content(1024):
#         f.write(chunk)


# 提交表单
# 提交一个字典数据，就认为是一个表单
# form = {'username':'user', 'password':'pass'}
# r = requests.post('http://httpbin.org/post', data = form)
# print(r.text)
# print ('********************json************************')
# r = requests.post('http://httpbin.org/post', data = json.dumps(form))
# print(r.text)

# cookie
url = 'http://www.baidu.com'
r = requests.get(url)
print(r)
print(type(r))
cookies = r.cookies
print(cookies)
print(type(cookies))
print(cookies.get_dict())
for k, v in cookies.get_dict().items():
    print(k, v)

cookies = {'c1': 'v1', 'c2': 'v2'}
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.text)
