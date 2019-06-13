##출력 옵션 활용하기##
#program 2-18#
#print() 함수에서 쉼표로 데이터를 구분하여 출력할 때
#자동적으로 분리되는 빈 칸을 sep 옵션으로 제어할 수 있다.
print('a','b','c')
print('a','b','c',sep='')
print('a','b','c',sep='***')

#program 2-19#
#print() 함수를 여러 변 사용할 경우, 각 print() 함수가 수행된 후에는
#자동적으로 줄바꿈이 일어난다. 이는 커서가 자동적으로 내려가기 때문
#커서를 줄바꿈시키지 않고 바로 옆에 놓고 같은 줄에 여러 print()함수의 내용을
#나타내고자 할 때 end 옵션을 사용할 수 있다.
print('a')
print('b')
print('c', end ='')
print('d', end ='')
print('e', end ='***')
print('f')

#program 2-20#
#본 예제는 부동 소수점이 출력되는 연산을 수행해 봄
#소수점 길이를 제어하지 않고 결과 값을 출력
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print("월급여: ", monthly_payment)

#program 2-21#
#본 예제에서는 소수점 자리를 제어하여 결과를 출력해봄
amount_due = 5000.0
monthly_payment = amount_due / 12
print('월급여: ', format(monthly_payment, '.2f'))

#program 2-22#
#본 예제도 소수점 자리를 제어하여 결과를 출력
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $', format(annual_pay, '.2f'), sep='')

#program 2-23#
#본 예제는 부동 소수점을 특정 너비에 맞추어 출력하는 방법
#아래와 같이 각 변수에 부동 소수점이 포함된 값을 할당
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999
#7칸에 맞추어 부동 소수점이 포함된 변수 값을 출력
print(format(num1, '7.2f'))
print(format(num2, '7.2f'))
print(format(num3, '7.2f'))
print(format(num4, '7.2f'))
print(format(num5, '7.2f'))
print(format(num6, '7.2f'))
