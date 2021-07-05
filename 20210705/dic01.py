dict = {'번호':10, '성명':'장동건', '나이':23, '사는곳':'서울'}

print(dict)
print(type(dict))			  #dic 변수 타입
print(dict['나이'])		      #나이 key 값으로 value 값 출력
dict['나이'] = 24             #나이 키 값 항목 변경
print(dict['나이'])
dict['직업'] = '배우'         #작업 항목 추가
print(dict)
print(dict.keys())            # 키 값 전체 반환
print(dict.values())          # 값 전체 반환
print('사는곳' in dict)       # 키 값 존재여부 : True
del dict['사는곳']			  # 키 값 삭제
print('사는곳' in dict)       # 키 값 존재여부 : False
print(dict)
