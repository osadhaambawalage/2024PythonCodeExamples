# 01 syntax error example 

# prin() --> syntax error . can be identified before running the code 

# 02 Logical error --> can be identified when the code is running 

# example for logical error / runtime 
# assume we have an array with 3 elements. in the next step we will going to delete all 3 elements. 
# after that we need to call the value of 1 st element. 


# with out error handaling  
a1 = int (input ('enter value for a1 : ')) 
b1 = int (input('Enter value for b1 : '))


# with error handaling
try : # put critical stuff 
    a = int (input ('enter value for a : ')) 
    b = int (input('Enter value for b : '))

except: # call after fired a error 
    print("Error was found")