aa = [30, 10, 20]
print("현재의 리스트 : %s" % aa)
	
aa.append(40)										# 리스트에 요소 하나 추가
print("append 후의 리스트 : %s" % aa)
zz=aa.pop()											# 리스트에 제일 마지막 요소 제거
print("pop 후의 리스트   : %s" % aa)
print("리스트에서 꺼낸값 : %s" % zz)
aa.sort()											# 리스트를 오름차순 정렬
print("sort 후의 리스트 : %s" % aa)			
aa.reverse()										# 리스트를 역순 정렬
print("reverse 후의 리스트 : %s" % aa)
aa.insert(2, 222)									# 리스트의 3번째 위치에 222값을 추가
print("insert 후의 리스트 : %s" % aa)
aa.remove(222)										# 리스트의 222값 제거
print("remove 후의 리스트 : %s" % aa)
aa.extend([77,88,77])								# 다른 리스트를 확장 
print("extend([77,88,77]) 후의 리스트 : %s" % aa)   
print("77값의 개수 : %d" % aa.count(77))            # aa리스트에 77 요소 값이 몇개 있는지 출력
