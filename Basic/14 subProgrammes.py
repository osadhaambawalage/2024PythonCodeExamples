#01  in build functions, system defined function 

print('hello'); 


#02  user defined functions 

def sample_function ():  # non retruned function/ void function 
    print("This is a sample function");
    print("For testing purpose");


def calculate_twoNumers(num1, num2): # returned function with parameters 
    sum = num1 + num2;
    return sum;

def calculate_twoNumers_v2(num1, num2): # returned function with parameters 
    return num1 + num2;

# call functions 
sample_function(); 

result = calculate_twoNumers(20,5);
print('result = ', result);
