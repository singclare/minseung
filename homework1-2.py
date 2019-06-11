##기본 연산 수행하기##
#Program 2-13#
#salary 변수에 급여를 할당합니다.
salary = 2500.0
#bonus변수에 보너스를 할당합니다.
bonus = 1200.0
#급여와 보너스를 더하여 총 급여
pay = salary + bonus
#총 급여 출력
print('총 급여: ', pay)

#program 2-14#
#본 예제에서는 원가에 할인율 적용 > 할인가격 계산
#original price 변수에 원가를 입력
original_price = float(input("제품의 원가를 입력해주세요: "))
#원가에 할인율 20%를 적용 > 할인가 계산 > discount변수에 할당
discount = original_price * 0.2
#원가에 할인가가 적용된 제품 가격을 계산 > sale_price변수에 할당
sale_price = origianl_price - discount
#할인가가 적용된 제품 가격을 출력
print('할인가격: ', sale_price)

#Program 2-15#
#세 과목의 평가 점수를 입력받고
#test1, test2, test3 변수에 각각 할당
test1 = float(input('첫 번째 과목 점수를 입력해주세요: '))
test2 = float(input('두 번째 과목 점수를 입력해주세요: '))
test3 = float(input('세 번째 과목 점수를 입력해주세요: '))
#각 과목 평균 점수 계산
#그 결과 값을 average 변수에 할당
average = (test1 + test2 + test3) / 3.0
#점수 평균 출력
print('3 과목의 평균 점수: ', average)

#Program 2-16#
#본 예제는 초를 입력받아 시, 분, 초로 변환하는 프로그램
#초 값을 입력받아 total_seconds 변수에 할당
total_seconds = float(input('시간 값을 초 단위로 입력해주세요: '))
#시간을 계산하여 hours 변수에 할당
hours = total_seconds // 3600 #나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
#분을 계산하여 minutes 변수에 할당
minutes = (total_seconds) // 60) % 60 #나누기 연산 후 몫이 아닌 나머지를 구함
#초의 나머지 값을 seconds 변수에 할당
seconds = total_seconds % 60
#시, 분, 초 값을 출력
print('시 분 초는 다음과 같습니다.')
print('시: ', hours)
print('분: ', minutes)
print('초: ', seconds)

#Program 2-17#
#본 예제는 목표액을 특정 이율을 얻고자 할 경우 매년 적립해야할 금액을 계산
#목표액을 입력받고 future_value 변수에 할당
future_value = float(input('목표 금액을 입력해주세요: '))
#연간 이율을 입력받고 rate변수에 할당
rate = float(input('연간 이율을 입력해주세요: '))
#적립 기간을 입력ㅂ다고 rate변수에 할당한다.
years = int(input("저축 기간을 연 단위로 입력해주세요: "))
#특정 기간 동안 적립해야할 금액 계산 > present_value변수에 할당
present_value = future_value / (1.0 + rate)**years #**: 거듭제곱
#적립 금액을 출력
print('적립 금액: ', present_value)
