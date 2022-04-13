# korcen(코르센)
korean(한국어) censorship(검열)의 줄임말로 

누구나 쉽게 텍스트에 비속어가 있는지 확인이 가능합니다.

어떤 종류의 비속어인지까지 구별이 되는 모듈입니다.

[욕설 데이터 파일](https://github.com/2runo/Curse-detection-data/blob/master/dataset.txt)을 이용해 테스트한 결과 77.5%의 정확도를 보입니다.

[TNS봇](https://discord.com/api/oauth2/authorize?client_id=848795383751639080&permissions=8&scope=bot%20applications.command)의 욕설 검열에 들어가는 코드입니다.
## Licenses

모든 프로그램 모듈의 출처 표기

협의후 제거

https://github.com/TANAT96564/korcen

링크 또는 "디스코드 TNS 봇" 표기 

# Maker

#### 총 개발자
>Tanat
```
discord:  Tanat#0206
email:    shrbwjd05@gmail.com
```
#### JS 버전 
>이루
```
discord:  이루#6410
```
## Installation

```sh
$ pip install korcen

# MacOs/Linux
$ python3 -m pip install korcen
# Windows
$ py -m pip install korcen
```

# Example
모든 예시는 가장 최신버전의 모듈을 사용합니다.

>py  0.0.5
```py
from korcen import korcen

korcen = korcen.korcen()

text = input()
print(korcen.check(text))
```

>js 0.0.1
```js
준비중
```

비속어가 있다면 True 없다면 False 출력하는 예제입니다.


#### 자세한 예시들은 [example](https://github.com/Tanat05/korcen/tree/main/example) 파일 참고하세요.



© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
