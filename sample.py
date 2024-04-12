

x = int(input("첫번째 정수를 입력하시오: "))
ch = input("연산자를 입력하시오: ")
y = int(input("두번째 정수를 입력하시오: "))


if ch == '+':
    print(f'{x} + {y} = {x+y}')
    
elif ch == '-':
    print(f'{x} - {y} = {x-y}')
    
elif ch == '*':
    print(f'{x} * {y} = {x*y}')
    
elif ch == '/':
    print(f'{x} / {y} = {x/y}')
    
else:
    print(f'입력하신 {ch} 연산자는 지원하지 않거나 연산자가 아닙니다.')
