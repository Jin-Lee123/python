sum , i = 0, 0
for i in range(1, 20, 1):
	sum+=i
	if sum>100:
		break;
sum-=i
print("%d" %sum)
print("-----------------")

sum , i = 0, 0
j = int(input("숫자를 입력합니다. " ))
while True:
	if i<j:
		i = i + 1
		sum += i;
	elif i==j:
		break
print("1에서 %d 까지의 합은 %d 입니다." % (j, sum))
