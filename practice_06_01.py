


# su = [3,6,2,5,4,1]


# list_length=len(su)-2


# while su[list_length]>=su[list_length+1]:
#     list_length = list_length-1

# #print(su[list_length])


# while su[list_length]<su[list_length+1]
    


def hamsu(lst):
    n = len(lst)
    
    i = n - 2
    while i >= 0 and lst[i] >= lst[i+1]:
        i -= 1
    
    if i == -1:
        return None
    

    j = n - 1

    while lst[i] >= lst[j]:
         j -= 1
    

    lst[i], lst[j] = lst[j], lst[i]
    
  
    lst[i+1:] = reversed(lst[i+1:])
    
    return lst




lst = [3, 6, 2, 5, 4, 1]
nextlst = hamsu(lst)
if nextlst is None:
    print("주어진 순열이 마지막 순열입니다.")
else:
    print(nextlst)  