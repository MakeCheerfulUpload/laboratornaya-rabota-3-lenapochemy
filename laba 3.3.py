import re

st = input()
st = ' ' + st + " "

pattern = '\sl\w{3}p\w{3}e\w*\s'

print(re.findall(pattern,st))

