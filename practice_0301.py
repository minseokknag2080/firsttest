



bubblearray = list(map(int, input("수를 입력하시오 :").split()))


for q in range(len(bubblearray)-1,0,-1):
    for i in range(0,q,1): 
        #print(str(q) + "/" + str(i))
        #print(bubblearray[i])
        if(bubblearray[i]>bubblearray[i+1]):
            tmp = bubblearray[i+1]
            bubblearray[i+1] = bubblearray[i]
            bubblearray[i] = tmp

print(bubblearray)


