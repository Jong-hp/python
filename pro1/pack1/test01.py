'''
여러 줄
주석
'''
from astroid.node_classes import Keyword
"""
여러 줄
주석
"""
# 한 줄 주석

var1 = '안녕' #전역 변수
var1 = 5
print(var1)
# 변수 선언시 type을 선언하지 않음

print()
a = 10
b = 12.5
c = b
print(a, ' ', b, ' ', c)
print('주소출력: ', id(a), ' ', id(b), ' ', id(c))
print(a is b, a == b) # 주소 비교, 값 비교
print(c is b, c == b)

aa = [1000]
bb = [1000]
print(aa == bb, aa is bb)
print(id(aa), ' ',id(bb))

print('-----------')
A = 1; a = 2;
print('A+a', A + a, id(A), id(a))

print()
import keyword
print('키워드(예약어) 목록: ', keyword.kwlist)
# &1for = 3

print()
print(10, oct(10), hex(10), bin(10))
print(10, 0o12, 0xa, 0b1010 )

print('자료형')
print(3, type(3))
print(3.4, type(3.4))
print(3 + 4j, type(3 + 4j))
print(True, type(True))
print('good', type('good'))

# 집합형 자료형 타입
print((1,), type((1,)))
print([1], type([1]))
print({1}, type({1}))
print({'k':1}, type({'k':1}))

print(isinstance(1.2, int))
print(isinstance(1.2, float))

