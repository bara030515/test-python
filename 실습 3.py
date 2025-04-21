print("## 택배를 보내기 위한 정보를 입력하세요. ##")
reciever = input("받는 사람 : ")
adress = input("주소 : ")
weight = int(input("무게(g) : "))
price = weight * 5

print("** 받는 사람 ==> ", reciever)
print("** 주소 ==> ", adress)
print("** 배송비 ==> ", price, "원")