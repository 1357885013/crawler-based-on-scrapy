import json
import codecs


big = {'1': {'1': 1, '2': 2}, '2': {'1': 1, '2': 2}}
string = json.dumps(big, indent=4, separators=(',', ': '))
string = string.encode()
string = string.decode('unicode-escape')
f = codecs.open('json.txt', 'w+', 'UTF-8')
f.write(string)
f.close()
print(string)

f = codecs.open('json.txt', 'r', 'UTF-8')
string = f.read()
print(string)
big = json.loads(string)
print(big['1']['1'])
f.close()
