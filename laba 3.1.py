import re

st = input()
smile = ';<{/'

countsmile = len(re.findall(smile, st))

print(countsmile)

