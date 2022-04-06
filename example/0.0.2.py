#0.0.1 ~0.0.2 버전
from korcen import check

while True:
    text = input()
    a = check.check(text)
    print(a)
    #비속어가 없다면 0 출력
    #비속어 종류에 따라 1~9 출력
    
#모듈 사용 표기하기
