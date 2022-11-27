'''
파일명 : ex07-2-for-range.py
for 문과 range 함수

range()
    연속된 숫자를 만들어주는 함수
'''
dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):
    print('{}x{}={}'.format(dan, n, dan * n, end=''))

'''
# range(10):  # 0~9까지. range(stop)
# print('{}x{}={}'.format(dan, n, dan * n))

# range(1, 10, 2):  #step을 2값으로 넣어줌. 1부터 2씩 증가 < 10
# print('{}x{}={}'.format(dan, n, dan * n))
'''

'''
range(stop)
range(start, stop)
range(start, stop, step)
'''

