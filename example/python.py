from korcen import korcen

korcen = korcen.korcen()

text = input()

a = korcen.check(text)
print(a)
#모든 비속어

a = korcen.general(text)
print(a)
#일반 욕설

a = korcen.minor(text)
print(a)
#사소한 욕설

a = korcen.sexual(text)
print(a)
#성적발언

a = korcen.belittle(text)
print(a)
#비하발언

a = korcen.race(text)
print(a)
#인종차별발언

a = korcen.parent(text)
print(a)
#패드립

a = korcen.english(text)
print(a)
#어 욕설

a = korcen.japanese(text)
print(a)
#일본어 욕설

a = korcen.chinese(text)
print(a)
#중국어 욕설

a = korcen.special(text)
print(a)
#특수(이모지)

a = korcen.politics(text)
print(a)
#정치발언


