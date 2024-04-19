# branch sample1

print('branch sample1')
print('Hello World!!')
print('제발 성공하길')

# branch sample2

print('branch sample2')
print('sample2 수정 완료')
print('이제 잘 좀 업로드 하자!!')


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
