'''
파일명 : ex02-5-list.py
List
    단일 변수에 여러 항목을 저장하는데 사용된다.
    List 항목은 순서가 지정되고 변경 가능하며 중복값 허용
    List 에는 다양한 데이터 유형이 포함될 수 있다.
'''
thislist = ["피카츄", "라이츄", "꼬부기"]
            # 0         1          2 (인덱스 번호)
print(thislist)
print(thislist[0])
# List 길이
print(len(thislist))  # len함수는 데이터 몇개있는지 알려줌

# List 데이터 유형
list1 = ["피카츄", "라이츄", "꼬부기"]
list2 = [1, 2, 3, 5]
list3 = [True, False, False] # Bool함수는 True, False처럼 대문자로 시작
# List 안에는 다양한 유형 포함 가능
list4 = ["abc", 34, False, 40]

# 항목 (인덱스 번호)
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist[1])

# 변경
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist[1] = "잠만보"
print(thislist)

# 항목 변경 2개
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터블", "야도란"]
thislist[1:3] = ["울먹이", "메타몽" ]
print(thislist)

# 두번째 세번째 값을 하나의 값으로 변경
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터블", "야도란"]
thislist[1:3] = ["울먹이"]
print(thislist)

# 항목추가 - 맨뒤에 추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.append("꼬부기")  # list에 append 함수(?)가 있음
print(thislist)

# 항목추가 - 인덱스번호로 추가
thislist = ["피카츄", "라이츄", "파이리"]
thislist.insert(1, "잠만보")
print(thislist)

# 항목 값으로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.remove("라이츄")
print(thislist)

# 항목을 지정된 인덱스로 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop(2)
print(thislist)

# 마지막 값 제거
thislist = ["피카츄", "라이츄", "파이리"]
thislist.pop()
print(thislist)

# 전체 목록 삭제
thislist = ["피카츄", "라이츄", "파이리"]
thislist.clear()
print(thislist)

thislist = ["피카츄", "라이츄", "파이리"]
thislist.extend(["버터플", "야도란"])
print(thislist)

#객체(object)에 종속된 함수 : 매소드 예시) list.extend

#객체 삭제
# del thislist
# print(thislist)
