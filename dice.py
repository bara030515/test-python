import random

count = 0

dice1 = 0
dice2 = 0
dice3 = 0

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    count = count + 1
    print(dice1,dice2,dice3)
    if ((dice1 == dice2) and ( dice1== dice3)):
        break

print(count, '회:', dice1,dice2,dice3)

print("3개의 주사위는 모두", dice1, "입니다.")
print("같은 숫자가 나오기까지 ", count, "번입니다.")