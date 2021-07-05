# 복습코드

#으로 시작하는 곳 부터 줄 끝까지 주석
''' 이것은 구간 주석 '''
""" 이것도 구간 주석 """

variable = 100              # int로 취급됨
variable = "문자 가능"      # str로 취급됨
variable = '문자 가능'      # "dhk '은 같다

print(variable)             # 문자 출력 방법1
print("%s" %variable)       # 문자 출력 방법2
print(type(variable))       # 변수의 type을 알아내기
a = type(variable)          
print(a)

print("Variable 의 Type : %s"  % type(variable))

a, b, c, d = 100, "apple" , 3.14, 'melon'
print("a 의 Value : %d"  % a)
print("a 의 Type : %s"  % type(a))
print("b 의 Value : %s"  % b)
print("b 의 Type : %s"  % type(b))
print("c 의 Value : %f"  % c)
print("c 의 Type : %s"  % type(c))
print("d 의 Value : %s"  % d)
print("d 의 Type : %s"  % type(d))

alist = [100, 200, 300, 400]   # C#의 경우 int[4]
print('alist : %d, %d, %d, %d' %(alist[0],alist[1],alist[2],alist[3]))
