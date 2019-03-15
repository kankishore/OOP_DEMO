from datetime import datetime


x=5
print(type(x))
y=str(x)    # Type Casting
print(type(y))


active=True
print(type(active))
print(int(active))
print(type(int(active)))

i=0
b=bool(i)# convert int to boolean
print(type(b))
print('value of b is',b)

doj='2018-02-28'
print(type(doj))
doj=datetime.strptime(doj, '%Y-%m-%d')
print(doj)
print(type(doj))