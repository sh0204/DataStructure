import random
import math

##클래스와 함수 선언 부분
class Node():
    def __init__(self):
        self.data = None
        self.link = None
        
def printStores(start):
    current = start 
    if current.link == None:
        return
    
    while current.link != start: #head
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], '편의점, 거리:', math.sqrt(x*x + y*y))
    print()
    
def makeStoreList(store):
    global memory, head, current, pre
    
    node = Node()
    node.data = store
    memory.append(node)
    
    if head == Node: #첫번째 편의점
    
        head = node
        node.link = head
        memory.append(node)
        return

    #새 편의점이 첫 번째 편의점보다 가까우면 첫 편의점으로 만듦
    
    nodeX, nodeY = node.data[1:]
    nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
    headX, headY = head.data[1:]
    headDist= math.sqrt(headX*headX + headY*headY)
    
    if headDist > nodeDist :
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currDist = math.sqrt(currX*currX + currY*currY)
        if currDist > nodeDist:
            pre.link = node
            node.link  = current
            return
     
#전역변수 선언부분
memory = []
head, current, pre = None, None, None

#메인 코드부분
if __name__ == "__main__":
    
    storeArray =[]
    storeName = 'A'
    for _ in range(10):
        store = (storeName, random.randint(1,100), random.randint(1,100))
        storeArray.append(store)
        storeName = chr(ord(storeName)+1) #편의점 이름 순서를 A->B->C...
        
    for store in storeArray:
        makeStoreList(store)
        
    printStores(head)
    
    