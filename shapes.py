
 def drawing_triangle(n):
   for i in range(1,n):
      print("#" * i)
 def drawing_pyramid(n):
   for i in range(0,n):
      j = n - i
      print(" "*j,end = "")
      print("#"*(2*i+1))

 def drawing_diamond(n):
    for i in range(0,n):
    j = n - i
    print(" "*j,end = "")
    print("#"*(2*i+1))
  for i in range(n,-1,-1):
    j = n - i
    print(" "*j,end = "")
    print("#"*(2*i+1))
