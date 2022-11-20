'''
파일명 : ex02-7-set.py
Set
    순서가 없다
    변경할 수 없다
    인덱싱되지 않는 컬렉션
    배열성 있는 자료구조의 객체 데이터
    중복값 없다
'''
thisset = {"피카츄", "라이츄", "파이리"}
print(thisset)
# 실행할 때마다 순서가 변경
print(thisset)
# 항목 가져오기
for x in thisset:  #반복실행문. set에 남는게 없을때까지
    print(x)

# 값이 있는지 확인 : True/False bool값으로 알려줌
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset)
print("꼬부기" in thisset)

# 항목 추가하기
thisset.add("꼬부기")
print(thisset)

# 다른 Set 항목 추가
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1)

# 항목제거
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset)
# thisset.remove("피카츄")
# print(thisset)

thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset)
thisset.discard("피카츄")
print(thisset)

# 항목제거
thisset.pop()

# 비우기
thisset.clear()
