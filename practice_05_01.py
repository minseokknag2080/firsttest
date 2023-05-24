def pow(a, n):
    if n == 0:
        return 1
    else:
        return a*pow(a, n-1)

a = float(input("실수 a를 입력하세요: "))
n = int(input("음이 아닌 정수 n을 입력하세요: "))

result1 = pow(2, n)
result2 = pow(a,result1)
print(result1)
print("{0}의 2^2^n승 = {1}".format(a, result2))