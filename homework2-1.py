##While반복문: 조건 기반 반복문##
#Program 2-1#
#본 예제는 while문을 이용하여 판매 수수료를
#반복적으로 수행하는 프로그램을 만들어보자.
def main() :
    keep_going = 'y' #반복 제어 변수 'y'값 할당
    #판매 수수료율 반복적 계산
    while keep_going == 'y' :
        #판매량, 수수료율 입력 > 변수에 할당
        sales = float(input('Enter the amount of sales: '))
        comm_rate = float(input('Enter the commission rate: '))
        # 수수료 계산
        commission  = sales * comm_rate
        #수수로 출력
        print('The commission is $', format(commission, ',.2f'), sep = '')
        keep_going = input('Do you want to calculate another commission? (y/n)')

main()

#Program 2-2#
#본 예제에서는 while문을 이용하여 온도 상태를 반복적으로 점검하는 프로그램을 만들어보자.
#전역 상수 MAX_TEMP에 최고 온도 할당
MAX_TEMP = 102.5

def main() :
    #현재 온도 입력 및 할당
    temperature = float(input("Enter the substance's Celsius temperature: "))
    #온도가 조건에 맞을 때까지 반복적으로 입력받고 상태를 점검
    while temperature > MAX_TEMP :
        print('The temperature is too high')
        print('Turn the thermostat down and wait')
        print('5 minutes. The take the temperature')
        print('again and enter it.')
        temperature = float(input('Enter the new Celsius temperature: '))
    #while문을 벗어나면 온도가 적절히 내려갔다는 의미이므로 해당 메시지를 출력
    print('The temperature is acceptable.')
    print('Check it again in 15 minutes.')

main()
