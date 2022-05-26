# My First Simple Calculator.
# It performs addition(+), subtraction(-), multiplication(*) and division(/).

a = float (input ('Enter first number= '))
b = input ('Enter operator (+,-,*,/)= ')
c= float (input ('Enter second number= '))
if b == '+':
    print (a + c)
elif b == '-':
    print (a - c)
elif b == '*':
    print (a * c)
elif b == '/':
    print (a / c)
else:
    print ('Invalid')
    
#You can try this out!
