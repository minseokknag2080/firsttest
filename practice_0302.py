







insertarray = list(map(int, input("수를 입력하시오 :").split()))



for i in range(1,len(insertarray),1):
    loc = i-1
    newitem = insertarray[i]
    while(loc>=0 and newitem < insertarray[loc]):
        # print(i,"************")
        insertarray[loc+1] = insertarray[loc]
        loc = loc -1
    insertarray[loc+1] = newitem

print(insertarray)