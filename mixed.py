import re
r = re.compile("^[A-Za-z0-9 ,-]*[A-Za-z0-9][A-Za-z0-9 ,-]*$")
#r = re.compile("^[A-Za-z ]*[A-Za-z][A-Za-z ]*$")
x = input('fisrt time')
while r.match(x) is None:
    print('fff')
    x = input('again')



