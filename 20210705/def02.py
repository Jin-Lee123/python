def myde01():
	i = 10
	j = 20
	print(i+j)
myde01()

def myde02(i, j):
	print(i + j)
myde02(10, 20)

#계산할 숫자를 두개 입력하니다.
def myde03(i, j, p):
	if p == '+':
		print(i+j)
	elif p == '-':
		print(i-j)
	elif p == '*':
		print(i*j)
	elif p == '/':
		print(i/j)
n = int(input("첫 번째 숫자를 입력합니다. : "))
m = int(input("두 번째 숫자를 입력합니다. : "))
p = input("연산자를 입력하세요(+, -, *, / ) ")
myde03(n,m,p)
