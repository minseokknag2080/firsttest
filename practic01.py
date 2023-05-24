



a = input("첫 번째 비트를 입력하시오 : ")
b = input("두 번째 비트를 입력하시오(첫 번째 비트와 자리 수를 맞춰서 입력) : ")

#AND
for i in range(len(a)):                             #len 문자열의 크기 반환   // range()숫자 한개 0~그 숫자 까지, 숫자 두개 수~그 수
    andbit = str(int(a[i])&int(b[i]))             #str 문자열로 변환 // 
    if i==0 :
        andvalue = andbit
    else:
        andvalue = andvalue + andbit


print("AND 연산 : "+andvalue)   

#OR
for i in range(len(a)):
    orbit = str(int(a[i])|int(b[i]))
    if i==0 :
        orvalue = orbit
    else:
        orvalue = orvalue + orbit


print("OR 연산 : "+orvalue)   

#XOR
for i in range(len(a)):
    xorbit = str(int(a[i])^int(b[i]))
    if i==0 :
        xorvalue = xorbit
    else:
        xorvalue = xorvalue + xorbit


print("XOR 연산 : "+xorvalue)   