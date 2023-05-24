

#ctrl shift v

#집합 a입렵받기
# 사용자로부터 입력받은 값을 공백을 기준으로 분리하여 딕셔너리로 만들기
data_a = input("딕셔너리를 생성할 값을 입력하세요 (key:value 쌍, 각 쌍은 공백으로 구분): ")
dic_items_a = data_a.split()  # 입력받은 값을 공백을 기준으로 분리하여 리스트로 만듦
fuzzy_dic_a = {}  # 빈 딕셔너리 생성


#print(dic_items)

# 리스트의 각 요소를 ','를 기준으로 분리하여 딕셔너리에 추가
for item in dic_items_a:
    key, value = item.split(",")
   # print(item.split(":"))
   # print(key,"==",value)
    fuzzy_dic_a[key] = float(value)

# 생성된 딕셔너리 출력
#print("생성된 딕셔너리:", fuzzy_dic)




#집합 b입렵받기
# 사용자로부터 입력받은 값을 공백을 기준으로 분리하여 딕셔너리로 만들기
data_b = input("딕셔너리를 생성할 값을 입력하세요 (key:value 쌍, 각 쌍은 공백으로 구분): ")
dic_items_b = data_b.split()  # 입력받은 값을 공백을 기준으로 분리하여 리스트로 만듦
fuzzy_dic_b = {}  # 빈 딕셔너리 생성


# 리스트의 각 요소를 ','를 기준으로 분리하여 딕셔너리에 추가
for item in dic_items_b:
    key, value = item.split(",")
   # print(item.split(":"))
   # print(key,"==",value)
    fuzzy_dic_b[key] = float(value)




#여집합

print("생성된 딕셔너리:", fuzzy_dic_a)

print("퍼지 집합의 여집합")

compl_dic_a = fuzzy_dic_a.copy()

for i in list(fuzzy_dic_a.keys()) :
     compl_dic_a[i] = round(1.0- fuzzy_dic_a[i],1)  #부동 소수점 한계 때문에 1.0-0.9 = 0.09999999999999998이 나온다.


print(compl_dic_a)


#합집합



#print(fuzzy_set_a_k)


#sum_dic = fuzzy_dic_a    #딕셔너리는 복사 해야 한다.

sum_dic = fuzzy_dic_a.copy()


for i in fuzzy_dic_b.keys():
    count = 0
    for q in sum_dic.keys():
        if(i == q):
            count = count +1
            if(sum_dic[q]>=fuzzy_dic_b[i]):
                {}
            else:
                sum_dic[q] = fuzzy_dic_b[i]

    if(count==0):
        sum_dic[i] = fuzzy_dic_b[i]



print(sum_dic)           




#교집합


fuzz_set_a_key = set(fuzzy_dic_a.keys())
fuzz_set_b_key = set(fuzzy_dic_b.keys())


inter_set = fuzz_set_a_key&fuzz_set_b_key
inter_dic = {}

for i in inter_set:
    inter_dic[i] = fuzzy_dic_a[i]

for i in inter_dic.keys():
    for q in fuzzy_dic_b.keys():
        if(i == q):
            if(inter_dic[i]<=fuzzy_dic_b[q]):
                {}
            else:
                inter_dic[i] = fuzzy_dic_b[q]


print(inter_dic)