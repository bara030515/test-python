'''
#실습1
#팩토리얼 계산기 : 1 ~ n까지의 곱

n = 6
res = 1

for i in range(1,n+1,1):
    res = res * i
# print(res)

# 연습 1
# 1000 - 2000사이 홀수의 합

hap = 0
for i in range(1001,2000,2):
     hap = hap + i
print(hap)

# for 중첩문
for i in range(0,3,1):
     for k in range(0,2,1):
          print("i:", i, "k:", k)'
          

# 실습 2
# 2단부터 9단까지 구구단을 출력하는 구구단 계산기
for num1 in range(2,10,1):
    print ('구구단', num1, '단')
    for num2 in range(1,10,1):
        print (num1, "X", num2, "=\t", num1*num2)
    print ('')
    

# while문
i = 0
while (i < 3):
    print('ㅎ', end='')''
    '''
    

# #무한루프 계산기
# while (True):
#     num1 = int(input("숫자1==> "))
#     if num1 == 0:
#         break
#     num2 = int(input("숫자2==> "))
#     res = num1 + num2
#     print(num1,'+',num2, '=', res)
    
#연습 2
# 1부터 100까지를 더하되 4의 배수는 제외

res = 0
for i in range(1,101,1):
    if (i % 4 == 0) or (i % 3 == 0):
        continue
    res = res + i
print (res)
