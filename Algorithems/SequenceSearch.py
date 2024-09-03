marksList = [45, 30, 80, 55, 43, 85]
searchKeyword = 30;
indexNum = 0;
searchLocation = -1;

while(indexNum < len(marksList)):
    if(marksList[indexNum] == searchKeyword):
        searchLocation = indexNum;
        break;
    else :
        indexNum = indexNum + 1;


if searchLocation == -1 :
    print("Search result not found")
else :
    print("Result was found. Location -  ", searchLocation) 

    