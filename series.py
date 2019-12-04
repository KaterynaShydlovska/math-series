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

def sum_series(n):
    b, c = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        b, c = c, b + c
    return c
print(sum_series(5))
  
   
  

  
