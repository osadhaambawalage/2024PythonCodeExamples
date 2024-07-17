# primitive data types integer , string , boolan 

integerVariable = 10;
print('Type = ',type(integerVariable)); # int
print('value = ',integerVariable); #10

integerVariable = 'Sri lanka';
print('Type = ',type(integerVariable)); # string
print('value = ',integerVariable); # Sri lanka

total01 = integerVariable + '20'; # 
print('total01 = ', total01) # Sri lanka20

integerVariable = True;
print('Type = ',type(integerVariable));
print('value = ',integerVariable);

total02 = integerVariable + 20; # true --> 1 +20
print(total02) # 21


variableInt: int = 18;
print(type(variableInt))


def IntegerReturnFunc(x:int , y: int):
    return x+y;

print (IntegerReturnFunc(2,9))

