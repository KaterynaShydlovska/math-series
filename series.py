#fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, ...
def fibonacci(n):
  if n<0: 
        print("Fail") 
  elif n==1: 
    return 0
  elif n==2: 
    return 1
  else: 
    return fibonacci(n - 1) + fibonacci(n - 2)



# lucas = 2, 1, 3, 4, 7, 11, 18, 29, ...       
def lucas(n) :  
  if (n == 0) : 
    return 2
  if (n == 1) : 
    return 1 
  return lucas(n - 1) + lucas(n - 2) 


def sum_series(n, first=0, second=1):
  if first == 0:
    n -= 1
  while n - 2 >= 0:
    temp = first + second
    first = second
    second = temp
    n -= 1
  return second
  
   
  

  
