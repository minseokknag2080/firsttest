import random
import matplotlib.pyplot as plt

n = int(input("정수 n을 입력하세요 : "))
p = int(input("앞면이 나올 확률을 입력하세요(%) : "))

count_f =0
count_b = 0

i = n

while(i>0):

    coin = random.randrange(1,101)

    if (0<coin and coin < p+1):
        count_f = count_f+1
    else:
        count_b = count_b+1
    i = i-1



#print(count_b , count_f)

ratio =[count_b , count_f]

plt.pie(ratio,labels=['count_b','count_f'],autopct='%1.2f%%')
plt.show()
