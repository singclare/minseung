##무한 반복문##
#Program 2-3#
#본 예제에서는 while문을 keep_going 변수로 조절하지 못할 경우
#반복문을 빠져나오지 못하는 무한 반복 상황

def main() :
    #반복을 제어하는 변수에 'y' 값 할당
    keep_going = 'y'
    #반복문 안에서 반복을 제어하는 변수에 대한 조절 기능이 없어서 무한 반복 진행
    while keep_going =='y' :
        #판매량과 수수료율을 입력 > 각 변수 할당
        sales = float(input('Enter the amount of sales: '))
        comm_rate = float(input('Enter the commission rate: '))
        #수수료 계산
        commission = sales * comm_rate
        #수수료 출력
        print('The commission is $', format(commission, ',.2f'), sep ='')
