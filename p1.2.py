# 파이썬 기초 순서
'''
1. 단일 데이터 관련
        수치형
            정수, 부동소수, 8~10~16 진수 등
'''
print('='*70)
# 수치형 값 변수에 담기
# 문자의 끝에 아무것도 쓰지 않는다(타 언어는 :)
# 여러 문장을 한줄에 표현할때 사용 할 수 있다.
# a 라는 변수에 10을 담아라 -> 10은 객체다
# -> a라는 변수에 10이라는 객체의 주소를 가르키고 있다(가르키고 있다가 중요 포인트)

a = 10
print(a)
# a는 11이라는 값을 카르킨다
a = 11
print(a, type(a))
a = 1.1
print(a, type(a))
a = '점심'
print(a, type(a))

# 파이썬의 변수는 : 변수명 = 값(실제는 주소값)
# 변수의 타입은 : 값이 세팅 될 때(=주소가 세팅 될 때) 결정된다 
# 타입 추론으로 타입을 결정한다
# 자바의 경우 : int a = 10:
# 타입을 줄 필요 없이 바로(단순하게) 쓸 수 있다
# 변수에는 키워드(예약어는 이용하지 않는다 : 파랑색)
# 변수명 : 알파벳, _, [숫자로 시작할 경우(x), 특수문자(x)]
#           관습적
#           단어를 이어서 사용 할 겨우 이어지는 글자 대문자, 첫글자 소문자
#           <상수>-> 대문자 사용
# 값은 오른쪽에서 왼쪽으로 
userName = 'kim'
user_name = 'lee' 
_userName = 'park'
_UserName = 'han'
P = 3.122482728
########################################################################################################

# 수치형 : 숫자로 정의된 자료형

#   정수 : 1, -1, 0
#   실수 : 1.1, -1.1

########################################################################################################
#   8진수  : 0o12 => 0o
#   10진수 : 255, 
#   16진수 : 0XFF, (0~9, A(10) ~ F(15)) => 0x

########################################################################################################
print('='*70)
# 정수값
a = 128
print(a)
a = -128
print(a)
a = 0
print(a)

########################################################################################################
print('='*70)
# 실수값
a = 1.1
print(a)
a = -1.1
print(a)

########################################################################################################
print('='*70)
# 16진수
a = 0xFF
print(a)

########################################################################################################
print('='*70)
# 기본 연산 확인(더하기 곱하기 빼기 나누기)
a = 10
b = 5
c = a + b
print(c)

print( a - b )
print( a * b )
print( a / b )


# 나머지 획득
print(a % b)
print( 11 % b)

# x의 y 제곱
print( 2** 3)
print( 2 ** 3)
print( 2**3)
print( 2  **3)
print( 2**          3)


# 나누고 소수점 아래 버림
print( 7//4)

# 우선순위
# 연산자 운선순위를 모르겠으면 ()를 이용항려 우선 연산할 내용을 감싸서 처리
print('='*100)
print(1 + 2 + 3 + 4 * 2)
print((1 + 2 + 3 + 4) * 2)

########################################################################################################

# 실습
print('='*100)
# a:90 b:86 c:100 => 평균을 출력하시오

a = 90
b=86
c=100
print((a+b+c)/3)