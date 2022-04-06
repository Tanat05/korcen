#0.0.1 ~0.0.2 버전
from korcen import check

text = input()
a = check.check(text)
print(a)
#비속어가 없다면 0 출력
#비속어 종류에 따라 1~9 출력

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
#0.0.3 ~0.0.4
from korcen import korcen

korcen = korcen.korcen()

text = input()
a = korcen.check(text)
print(a)
#비속어가 있는지 없는지 확인
#0.0.3 0 ~ 9 출력
#0.0.4 True 또는 False 출력

a = korcen.general(text)
print(a)
#일반 욕설
#True 또는 False 출력

a = korcen.minor(text)
print(a)
#일반 욕설
#True 또는 False 출력

a = korcen.sexual(text)
print(a)
#일반 욕설
#True 또는 False 출력

a = korcen.belittle(text)
print(a)
#일반 욕설
#True 또는 False 출력

a = korcen.race(text)
print(a)
#일반 욕설
#True 또는 False 출력

a = korcen.parent(text)
print(a)
#일반 욕설
#True 또는 False 출력

a = korcen.foreign(text)
print(a)
#일반 욕설
#True 또는 False 출력

a = korcen.special(text)
print(a)
#일반 욕설
#True 또는 False 출력

a = korcen.politics(text)
print(a)
#일반 욕설
#True 또는 False 출력

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#모듈 사용 출처 표기하기
