'''
파일명 : ex10-2-method-string2.py
'''
# join() 메소드  : 문자열 중간 중간에 뭔가를 끼워넣어줌
s = '-'.join('python')
print(s)  # p-y-t-h-o-n

s = '+'.join(['a', 'b', 'c', 'd', 'e'])   # alt+ctrl+l
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'e'])   # alt+ctrl+l
print(s)

# split() 메소드  : 리스트 값으로 반환
s = 'Life is too short'
result = s.split()
print(result)   # ['Life', 'is', 'too', 'short']

s = '010-1234-5678'
result = s.split('-')
print(result)   # ['010', '1234', '5678']

data = '김태호|39|프로그래머'
result=data.split('|')
print(result)



# replace()
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)    # Life is too long

# strip(), lstrip(), rstrip() 공백제거
s = '                apple'
print(s)    #                 apple 이때, 공백도 컴퓨터는 문자로 인식
result = s.lstrip()    # 왼쪽 공백 제거
print(result)   # apple

s = '      apple        '
print(s)
result = s.strip()   # 양쪽 공백 제거
print(result)

# 전체 공백 제거
s = '  a  p p l e '
print(s)
result = s.replace(' ', '')
print(result)