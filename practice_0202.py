





h_a = int(input("A행렬의 행을 입력하시오 : "))
l_a = int(input("A행렬의 열을 입력하시오 : "))
h_b = int(input("B행렬의 행을 입력하시오 : "))
l_b = int(input("B행렬의 열을 입력하시오 : "))

print("a행렬을 입력하시오.")
matrix_a = []
for i in range(h_a):
    row = list(map(int, input().split()))
    matrix_a.append(row)

# print(matrix_a)

# print(matrix_a[0][0])

print("b행렬을 입력하시오.")
matrix_b = []
for i in range(h_b):
    row = list(map(int, input().split()))
    matrix_b.append(row)



a = []    # 빈 리스트 생성
 
for i in range(h_a):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(l_b):
        line.append(0)     # 안쪽 리스트에 0 추가
    a.append(line)         # 전체 리스트에 안쪽 리스트를 추가
 


for i in range(h_a):
    for q in range(l_b):
            a[i][q]=0
            for p in range(l_a):
                a[i][q] = a[i][q] + matrix_a[i][p]*matrix_b[p][q]

print(a)

#///////////////////////////////////////////////////////////////////////////////////////////////
# a = [38, 21, 53, 62, 19]
# for i in range(len(a)):    #i는 0부터 4까지
#     print(i)

# print(len(a))