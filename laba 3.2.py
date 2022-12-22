import re

st = input()

allword = re.split(' ', st)

pattern = allword[0]

i=1
while i < len(allword):
    match = re.fullmatch (pattern, allword[i])
    if match:
        pattern = allword[i]
        allword.pop(i)

    else:
        pattern = allword[i]
        i+=1


str = ""
for i in range(len(allword)):
    str += allword[i]
    str += " "

print(str)