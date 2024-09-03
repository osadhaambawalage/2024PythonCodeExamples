studentDic = {'id':'S001', 'name':'Amal', 'Age' :29}

print(studentDic['Age']) # 29

# add new data to dictionary 
studentDic['TelNo'] = '0117878776'
print(studentDic['TelNo']) # 0117878776

# remove data from dictionary 

del studentDic['TelNo']
# print(studentDic['TelNo']) # this will generate an error 
print(studentDic) # {'id': 'S001', 'name': 'Amal', 'Age': 29}

studentDic.clear() # delete only the dictionary data 
print(studentDic) # {}

del studentDic # delete the enteir dictionary
