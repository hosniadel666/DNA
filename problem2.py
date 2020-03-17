import random

def problem2_1():
  lis = list(range(20,30))
  print(lis[3])
  print(lis)
  for i in lis :
    print (i,end = " ")


def problem2_2(my_list):
  print(my_list)
  print(my_list[0])
  print(my_list[-1])
  print(my_list[3:5])
  print(my_list[:3])
  print(my_list[3:])
  print(len(my_list))
  my_list.append('z')
  print(my_list)

def problem2_3(ne):
  for i in ne:
    print(i,"has",len(i),"letters.")
    
def problem2_4():
  lis = []
  random.seed(70)
  for i in range(0,10):
    lis.append(random.random()*5+30)
  print(lis)
  
def problem2_5():
  random.seed(171)
  for i in range(0,10):
    print(random.randint(1,6))

def problem2_6():
  random.seed(431)
  for i in range(0,100):
    print(random.randint(1,6)+random.randint(1,6))
    
def problem2_7():
  a = float(input("Enter length of side one: "))
  b = float(input("Enter length of side two: "))
  c = float(input("Enter length of side three: "))
  s = 0.5 * (a + b + c)
  area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
  print("Area of a triangle with sides",a,b,c,"is",area)


def average(lis):
  sum = 0
  for i in lis:
    sum = sum + i
  return sum / len(lis)

def maximum(lis):
  max_ = lis[0]
  for i in lis:
    if i > max_:
      max_ = i
  return max_

def minimum(lis):
  min_ = lis[0]
  for i in lis:
    if i < min_:
      min_ = i
  return min_

def problem2_8(temp_list):
  print("Average: ",average(temp_list))
  print("High: ",maximum(temp_list))
  print("Low: ",minimum(temp_list))

