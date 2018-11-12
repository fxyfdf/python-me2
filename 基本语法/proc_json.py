import json
# json 库的解码与编码
#字典不保证顺序
obj = {'one': '一', 'two': '二'}
print ('obj : %s'% obj)
encoded = json.dumps(obj)
print(type(encoded))
print(encoded)
decoded = json.loads(encoded)
print(type(decoded))
print(decoded)
