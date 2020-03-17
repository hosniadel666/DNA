def around(n):
  return int(n+0.5)
  
def average (lis):
  sum = 0
  for i in lis:
    sum = sum + i
  return sum / len(lis)
