# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q1HwJc2WF3jAjAPp7Yh6lNrk27rIdc6B

Statements in Python
1. Conditional Statements : if,elif,else
2. Looping Statements : for, while
"""

a = 15
b = 20

if a > b:
  print("a is greater")
  print("a is greater than b")

# if(a > b)
# {
#     printf("a is greater");
# }
# else if(x > y && x > z)
# {
#     printf("x is greater");
# }

# if condition:
#   statements1
#   statements2

x = int(input("Enter first Number : "))
y = int(input("Enter second Number : "))
z = int(input("Enter third Number : "))

if x > y and x > z:
  print("x is greater",x)
elif y > x and y > z:
  print("y is greater",y)
else:
  print("z is greater",z)

# 2016 % 4 == 0 - leap year
# 2000 % 100 == 0 2000 % 400 - leap year

# 1300 = not leap
# 1200 = leap 2013

year = int(input("Enter Year : "))

if year % 100 == 0:
  if year % 400 == 0:
    print("Leap year")
  else:
    print("Not Leap Year")
else:
  if year % 4 == 0:
    print("leap Year")
  else:
    print("Not Leap Year")

"""for loop"""

# for (i = 0; i < 10; i++)
# {
#     printf(i)
# }

"""range(n)"""

list(range(10))

list(range(5,15))

list(range(2,20,2))

for i in range(1,101):
  print(i)
print("hello")

for var in range(1,101):
  if var%2 != 0:
    print(var)

# while(i < 10)
# {
#     print(i)
# }

"""While in Python"""

i = 1
while i < 101:
  print(i)
  i += 1

while False:
  print("hello")

for i in range(10):
  for j in range(10):
    print(i,j)

i = 1

while i < 10:
  j = 1
  while j < 10:
    print(i,j)
    j += 1
  i += 1

