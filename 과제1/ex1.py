import random

# 전역변수 생성
totallLotto =[]
lotto =[]
pickNum = 0
cnt =0

# 메인
print("로또 번호 생성")
cnt = int(input("몇 번 뽑을까요? : "))

for _ in range(cnt):
    lotto = []
    while True:
        pickNum = random.randint(1,45) #1~45까지 랜덤으로 번호 생성
        if pickNum not in lotto :
            lotto.append(pickNum)
        if len(lotto) >=6 :
            break
    totallLotto.append(lotto)
        
for lotto in totallLotto :
    lotto.sort()
    print("자동번호 --> ", end=' ')
    for i in range(0,6):
        print("%2d " %lotto[i], end=' ')
        
    print()