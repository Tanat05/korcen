# korcen(코르센)
누구나 쉽게 텍스트에 비속어가 있는지 확인이 가능합니다

어떤 종류의 비속어인지까지 구별이 되는 모듈입니다

## 라이선스

모듈의 출처 표기

https://github.com/TANAT96564/korcen

링크 또는 "TNS 봇" 표기 

# 제작

>Tanat

discord:Tanat#0206
email:shrbwjd05@gmail.com

## Installation

```sh
# MacOs/Linux
$ python3 -m pip install korcen
# Windows
$ py -m pip install korcen
```

## Example

```py
from korcen import check

text = input()
a = check.check(text)
print(a)
```

비속어이 아니라면 0

비속어 종류에 따라 1~9 출력

© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
