# thread를 사용한 디지털 시간 출력
import time

now = time.localtime()
print(now)
print('{}년 {}월 {}일 {}시 {}분 {}초'.format(
    now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

print('-------')
import threading

def cal_show():
    now = time.localtime()
    print('{}년 {}월 {}일 {}시 {}분 {}초'.format(   # \ 쓰면서 가독성을 높일 수 있다
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

def my_run():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 3: break  # 3분으로 맞추고 break 넣고 출력을 멈출 수 있다.
        cal_show()
        time.sleep(1)
        
th = threading.Thread(target=my_run)    # threading.Thread(target=수행함수명)
th.start()

th.join()
print('프로그램 종료')