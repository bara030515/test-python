var1 = "나는 Python을 열공 중입니다."
var2 = "화이팅"

var3 = var1+var2
var4 = var2+var1

print(len(var4))

strLen1 = len(var1)
strLen2 = len(var2)

print("두 문자열 길이의 차이는"+str(strLen1-strLen2)+"입니다.")

var5 = var1.upper()
print(var5)
var6 = var1.lower()
print(var6)

var7 = """
선배, 마라탕 사주세요 (그래, 가자)
선배, 혹시 탕후루도 같이? (뭐? 탕후루도?)
그럼 제가 선배 맘에
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 내 맘이 단짠단짠
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 마라탕탕탕탕, 후루루루루
사실 저는 선배 마음에 들고싶은게 목적인데
내 맘 달콤상콤 탕후루처럼
선배, 맘에 들어갈게요 (무슨뜻이야?)
선배 (어), 마라탕 사주세요 (좋아, 가자)
선배 (어), 탕후루 사주세요 (탕탕탕)
사실 저는 선배 마음에 들고싶은게 목적인데
내 맘 맵당맵당 마라탕처럼
선배, 맘에 들어갈게요 (나 좋아하니?)
선배 (어), 마라탕 사주세요 (좋아, 가자)
선배 (어), 탕후루 사주세요 (탕탕탕)
오늘은 기필코 모쏠인생 때려친다
그럼 제가 선배 맘에
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 내 맘이 단짠단짠
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 마라탕탕탕탕, 후루루루루
사실 저는 선배 마음에 들고싶은게 목적인데
내 맘 달콤상콤 탕후루처럼
선배, 맘에 들어갈게요 (무슨뜻이야?)
선배 (어), 마라탕 사주세요 (좋아, 가자)
선배 (어), 탕후루 사주세요 (탕탕탕)
사실 저는 선배 마음에 들고싶은게 목적인데
내 맘 맵당맵당 마라탕처럼
선배, 맘에 들어갈게요 (나 좋아하니?)
선배 (어), 마라탕 사주세요 (좋아, 가자)
선배 (어), 탕후루 사주세요 (탕탕탕)
오늘은 기필코 모쏠인생 때려친다
그럼 제가 선배 맘에
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 내 맘이 단짠단짠
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 마라탕탕탕탕, 후루루루루
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 내 맘이 단짠단짠
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 마라탕탕탕탕, 후루루루루
"""

while True:
    numTang = var7.find("마라",0)
    numTang = var7.find("마라",numTang+1)
    print(numTang)
    if numTang == -1:
        break

print(numTang)

numHuru = var7.count("선배")
print(numHuru)


