


#from_pos 출발점 기둥
#to_pos 도착점 기둥
#aux_pos 중간 기둥




def hanoi(n,from_pos, to_pos, aux_pos):
    if n==1:    #원반이 1개이면 그냥 옮기면 된다.
        print(from_pos, "->",to_pos)
        return 
    
    #원반 n-1개를 aux_pos로 이동 (to_pos를 보조 기둥으로)
    hanoi(n-1, from_pos, aux_pos, to_pos)

    print(from_pos, "->", to_pos)
    hanoi(n-1,aux_pos,to_pos,from_pos)



n = int(input("정수 n을 입력하세요 : "))

hanoi(n,1,3,2)



