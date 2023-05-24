# A = 0b101010    #이진수 접두어 0b

# B = 0b100000

# C = bin(10)      #내장함수 bin을 이용하면 변수에 이진수 자체를 저장할 수 있다.

# print(A)       #10진수로 출력된다.

# print(C)         #내장함수를 이용한 변수는 이진수로 출력된다.


######################################################################


# print("첫번째 비트열을 입력하시오")


# a =  int(input(),2)   #input은 사용자가 키보드로 입력한 모든 것을 문자열로 저장한다. ## 그렇기 때문에 정수형으로 변환해야 한다.
#                                      #모든 비트열은 문자열로 표현된다. 
# print("두번째 비트열을 입력하시오")

# b = int(input(),2)

# #AND

# print(bin(a&b))       #비트연산 후 반환되는 값이 정수이므로 bin()함수를 이용해 이진수로 바꾼다.

# #OR

# print(bin(a|b))        #or

# #XOR

# print(bin(a^b))        #xor


#################################################################


# a = input("비트를 입력하시오 : ")
# b = input("비트를 입력하시오 : ")

# andva = ""
# orva = ""
# xorva = ""

# for i in range(len(a)):                  #len()함수 문자열 길이    #range()함수 숫자 한개 - 0~ 그수 // 숫자 두개 수 ~ 수
#     # 비트별 AND 연산 수행
#     andbit = str(int(a[i]) & int(b[i]))
#     andva += andbit

#     # 비트별 OR 연산 수행
#     orbit = str(int(a[i]) | int(b[i]))
#     orva += orbit

#     # 비트별 XOR 연산 수행
#     xorbit = str(int(a[i]) ^ int(b[i]))
#     xorva += xorbit 

# print("AND 결과:", and_result)
# print("OR 결과:", or_result)
# print("XOR 결과:", xor_result)







# a = input("첫 번째 비트를 입력하시오 : ")
# b = input("두 번째 비트를 입력하시오(첫 번째 비트와 자리 수를 맞춰서 입력) : ")

# #AND
# for i in range(len(a)):
#     andbit = str(int(a[i])&int(b[i]))        #정수나 실수를 문자열로 바꿔주는 함수
#     if i==0 :
#         andvalue = andbit
#     else:
#         andvalue = andvalue + andbit


# print("AND 연산 : "+andvalue)   

# #OR
# for i in range(len(a)):
#     orbit = str(int(a[i])|int(b[i]))
#     if i==0 :
#         orvalue = orbit
#     else:
#         orvalue = orvalue + orbit


# print("OR 연산 : "+orvalue)   

# #XOR
# for i in range(len(a)):
#     xorbit = str(int(a[i])^int(b[i]))
#     if i==0 :
#         xorvalue = xorbit
#     else:
#         xorvalue = xorvalue + xorbit


# print("XOR 연산 : "xorvalue)   



##########################################################################################

# while True:

#     p = float(input("0~1사이의 명제 p의 진리값을 입력하시오 : "))  #input 모든 것을 문자열로 출력한다.

#     if (p<0 or p>1):
#         print("잘 못 입력하셨습니다.")
#         continue
#     else:
#         break


# while True:

#     q = float(input("0~1사이의 명제 q의 진리값을 입력하시오 : "))  

#     if (q<0 or q>1):
#         print("잘 못 입력하셨습니다.")
#         continue
#     else:
#         break


# #AND (논리곱)

# if(q>p):
#     andva = p
#     print("논리곱은 p이다 : %.1f"%p)
# else:
#     andva = q
#     print("논리곱은 q이다 : %.1f"%q)




# #OR (논리합)

# if(q<p):
#     andva = p
#     print("논리곱은 p이다 : %.1f"%p)
# else:
#     andva = q
#     print("논리곱은 q이다 : %.1f"%q)








a = input("입력d : ")

b=""                            
for i in range(len(a)):
    b = b+a[i]                                  #b변수가 선언되기 전에 b변수를 사용하는 식이다. 그러므로 b를 위에서 선언해줘야 한다.

print(b)






