marksList = [20, 30, 40, 55, 43.56, 85]
marksList2 = [80,56,69,78]

print(marksList) # [20, 30, 40, 55, 43.56, 85]

print(marksList[2]) # 40

print(marksList[0:3]) # [20,30,40] 

print(marksList[2:5]) # [40, 55, 43.56] 

mergedMarksList = marksList + marksList2

print(mergedMarksList) # [20, 30, 40, 55, 43.56, 85, 80, 56, 69, 78]

# to get the min value of the list 
print(min(marksList)) # 20

# to get the max value of the list 
print(max(marksList)) # 85

print(marksList.count(20)) # to get the given element count of the list

print(len(marksList))  # to get the length of the list --> 6

marksList.append(99) # add new element to the list 
print(marksList)

del(marksList[-1])  # to remove element from the list -1 means the last element of the list 
print(marksList)

marksList.reverse() # to reverse elements of te list  
print(marksList)

marksList.sort() # sort in acending order 
print(marksList)




