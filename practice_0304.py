



bubblearray = list(map(int, input("수를 입력하시오 :").split()))
insertarray = list(bubblearray)      #리스트 복사는 그냥 포인터로 같은 곳 보는 것과 같다.

bc=0
ic=0

bcount = 0
for q in range(len(bubblearray)-1,0,-1):
    for i in range(0,q,1): 
        #print(str(q) + "/" + str(i))
        #print(bubblearray[i])
        bc+=1
        if(bubblearray[i]>bubblearray[i+1]):
            tmp = bubblearray[i+1]
            bubblearray[i+1] = bubblearray[i]
            bubblearray[i] = tmp

print(bubblearray)





# insertarray = list(map(int, input("수를 입력하시오 :").split()))



for i in range(1,len(insertarray),1):
    loc = i-1
    newitem = insertarray[i]
    
    while(loc>=0 and newitem < insertarray[loc]):
        ic+=1
        insertarray[loc+1] = insertarray[loc]
        loc = loc -1
    else:
        ic+=1
    insertarray[loc+1] = newitem

print(insertarray)







print("버블정렬 비교 횟수 : ",bc,"삽입정렬 비교 횟수 :" ,ic)

