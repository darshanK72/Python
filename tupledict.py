# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17wJ5wToP0J9BqOpgSWET0BlACwNy5skJ

str,list,tuple,dict,set
"""

t = (1,2,5,2,5,"hello",24.2,True)

print(t)
print(type(t))

print(t[3])

print(t[1:5:2])

print(t[::-1])

# t[2] = 10 immutable data type

t.count(2)

print(t.index('hello'))

t = list(t)
print(t)
print(type(t))

t.pop()

t

t = tuple(t)
print(t)
print(type(t))

"""Dict"""

d = {'one':1,'two':2,'three':3}
print(d)
print(type(d))

print(d['one'])

print(d['three'])

d1 = {2:12,23.1:23.24,False:True,'str':"hello World",'list':[1,2,3,4],'tup':(1,2,3),'dict':{'one':1,'two':2},'set':{1,1,2,2,3,4,5,4}}

print(d1)
print(type(d1))

print(d1[2])

print(d1[23.1])

print(d1['bool'])

print(d1[False])

d2 = d1.copy()

print(d2)

print(d1.get('str'))

print(d1.keys())

print(d1.values())

print(d1.items())

for ele in d1:
  print(d1[ele])

for k,v in d1.items():
  print(k , v)

d1.pop(23.1)

print(d1)

d1.popitem()

print(d1)

d1['str'] = "This is my home"

print(d1)

d1['set'] = {5,5,62,4,2,2}

print(d1)

d1.update({False:False})

print(d1)

l = ["hello","World","my","name"]
l1 = 56

d3 = dict.fromkeys(l,l1)
print(d3)

l2 = [1,2,3,4]
d4 = dict(zip(l,l2))
print(d4)

