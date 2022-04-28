# 전역 변수
poet = '''
나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다.
영변에 약산 진달래꽃, 아름 따다 가실 길에 뿌리오리다.
가시는 걸음걸음 놓인 그 꽃을 사뿐히 즈려 밟고 가시옵소서.
나 보기가 역겨워 가실 때에는 죽어도 아니 눈물 흘리오리다.
'''

cntDic ={}

#메인
if __name__ == "__main__" :
    for ch in poet:
        if ch.isalpha():
            if ch in cntDic:
                cntDic[ch] += 1
            else:
                cntDic[ch] = 1
                
    
    print('원문', poet)
    print('----------------------------------------------------')
    print('문자 빈도수(4회 이상)')
    print('----------------------------------------------------')
    for key in cntDic:
        if cntDic[key] >= 4:
            print(key, '-->', cntDic[key])