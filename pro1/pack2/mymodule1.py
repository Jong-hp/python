# 메인으로 사용하지 않고 다른 오듈에 호출될 맴버를 기술하는 용도
price = 12345

def listHap(*ar):
    print(ar)
    
    if __name__ == '__main__':  # False
        print('난 최상위 메인 모듈이야')
    

def kbs():
    print('대한민국 대표방송')
    
    
def mbc():
    print('만나면 좋은 친구')
