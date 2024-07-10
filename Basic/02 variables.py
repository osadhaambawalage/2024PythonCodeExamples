studentName = "amal"; #global variable 
print("student name in line no 02 ", studentName);


def testFunc(): #function declaration
    localStudentAge = 10; #local variable
    print("Now i am in test function");
    print("student name in line no 08 ", studentName);
    print("local student age = ",localStudentAge);

testFunc();  #function call 

#print(localStudentAge) # we can not use it here