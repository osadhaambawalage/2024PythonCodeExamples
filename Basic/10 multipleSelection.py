# input number should be categorised as less than 1, 1-20 , 21-40 or above 40 

num = int(input("Enter number : "))

if num < 1 : 
    print("Less than 1")
elif num < 21:
    print("1 - 20")
elif num < 41 :
    print("21 - 40")
else :
    print("above 40")