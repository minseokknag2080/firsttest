
while True:

    p = float(input("0~1사이의 명제 p의 진리값을 입력하시오 : "))  #input 모든 것을 문자열로 출력한다.

    if (p<0 or p>1):
        print("잘 못 입력하셨습니다.")
        continue
    else:
        break


while True:

    q = float(input("0~1사이의 명제 q의 진리값을 입력하시오 : "))  

    if (q<0 or q>1):
        print("잘 못 입력하셨습니다.")
        continue
    else:
        break


#AND (논리곱)

if(q>p):
    andva = p
    print("논리곱은 p이다 : %.1f"%p)
else:
    andva = q
    print("논리곱은 q이다 : %.1f"%q)




#OR (논리합)

if(q<p):
    andva = p
    print("논리곱은 p이다 : %.1f"%p)
else:
    andva = q
    print("논리곱은 q이다 : %.1f"%q)
