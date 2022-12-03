'''
파일명 : ex11-1-function.py

함수(function)
    하나의 특별한 목적의 작업을 수행하기 위해
    독립적으로 설계된 프로그램 코드의 집합.     # 매소드와의 차이점 : 매소드는 종속적으로 설계되었음. 그러나 중요한 것은 프로그램 코드의 집합이라는 점.

def 함수이름(매개변수#매개변수는 없을수있음)
    코드 실행문
    return 반환값  # return 이하는 없을 수있음
'''

# 매개변수 없고, 리턴 없는 경우의 함수 예시
def welcome():                      # 함수 정의하기
    print('Hello Python')
    print('Nice to meet you')

welcome()  # 함수 명령어를 실행하는 것을 호출(Call)이라고 함. 함수 호출하기(실행)

# 매개변수 있고, 리턴 없는 경우의 함수 예시
def introduce(name, age):           # 함수 정의하기
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))   # 매개변수란 다른(?) 함수에서 값을 받아서 변수로 쓸수있다

introduce('james', 25)

# 가변 매개변수 함수
def show(*args):
    print(type(args))
    for item in args:
        print(item)

show('python')
show('python', 'happy', 'birthday')


# 반환(return)값이 있는 함수의 예시
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()
print(result)


# 매개변수가 있고, 리턴값도 있는 함수의 예시
def plus(num1, num2):
    return num1 + num2

print(plus(1, 3))



area = 0
def move():
    global area    # 전역변수 선언해주기
    area += 1
    return area