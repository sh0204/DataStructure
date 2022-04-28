#카톡 친구 자동 삽입하기


#삽입 위치 찾기
def find_insert(name, num):
    findPos = -1 #새 친구 위치 -1로 설정
    for i in range(len(katok)):
        pair = katok[i]
        if num >= pair[1]:
            findPos = i
            break
    if findPos == -1: #새친구의 위치를 찾지 못함 -> 가장 횟수 적으니까 맨 뒤로 위치 설정
        findPos = len(katok)
        
    insert_data(findPos,(name, num))
    
#삽입
def  insert_data(position, name):
    if position < 0 or position > len(katok):
        print("데이터 삽입 범위 벗어남")
        return
    
    katok.append(None) #빈칸 추가
    Now_len = len(katok) #현재 배열 크기

    for i in range(Now_len-1, position, -1):
        katok[i]=katok[i-1]
        katok[i-1]=None
        
    katok[position]=name
    
#전역변수
katok = [('다현',200),('정연',150),('쯔위',90),('사나',30),('지효',15)]

#main
if __name__ =="__main__":
    
    while True:
        data = input("추가할 친구 : ")
        cnt = int(input("카톡 횟수 : "))
        find_insert(data,cnt)
        print(katok)