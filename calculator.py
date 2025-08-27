a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=input('Enter function to perform(+,-*,%,**):')
d=0

if c=='+':
  d=a+b
  print(d)
elif c=='-':
  d=a-b
  print(d)
elif c=='*':
  d=a*b
  print(d)
elif c=='%':
  d=a%b
  print(d)
elif c=='**':
  d=a**b
  print(d)
else:
  print('invalid operation')          
  