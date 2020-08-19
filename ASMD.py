def add(a,b):
   return(a+b)
def sub(a,b):
   return(a-b)
def mul(a,b):
   return(a*b)
def div(a,b):
   return(a/b)
a,b=map(int,input('enter any two numbers:').split())
print('addition of given number:',add(a,b))
print('subtraction of given number:',sub(a,b))
print('multiplication of given number:',mul(a,b))
print('divison of given number:',div(a,b))
