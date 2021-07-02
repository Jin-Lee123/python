#list02
aa = [0, 0, 0, 0]
hap = 0
aa[0] = int(input("1번째 숫자 : "))
aa[1] = int(input("2번째 숫자 : "))
aa[2] = int(input("3번째 숫자 : "))
aa[3] = int(input("4번째 숫자 : "))

hap = aa[0] + aa[1] + aa[2] + aa[3]
print("합계2 => %d" %hap)


# list 03
aa = []
aa.append(0)
aa.append(0)
aa.append(0)
aa.append(0)
print(len(aa))
print(aa)
bb = []
for i in range(0, 100):
    bb.append(i)
print(bb)

#list04
aa = [10, 20, 30, 40]
print("aa[-1]은 %d, aa[-2]는 %d" % (aa[-1], aa[-2]))

print(aa[0:2])
print(aa[2:4])
print(aa[0:])

#list03
aa=[]
print(type(aa))
print(len(aa))

aa.append(1)
aa.append(100)
aa.append("apple")
aa.append(3.14)

print(aa)
print(type(aa[0]))
print(type(aa[1]))
print(type(aa[2]))
print(type(aa[3]))

