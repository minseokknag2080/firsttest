

a = int(input("첫 번째 양의 정수를 입력하시오 :"))
b = int(input("두 번째 양의 정수를 입력하시오 :"))





if(a<b):
    tmp = a
    a = b
    b = tmp

x = a
y=b

while(y != 0):
    r = x%y
    x = y
    y = r

print(x , "= gce(",a,",",b,")")

