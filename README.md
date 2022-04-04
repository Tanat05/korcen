# korcen(코르센)
누구나 쉽게 텍스트에 욕설이 있는지 확인이 가능합니다

어떤 종류의 욕설인지까지 구별이 되는 모듈입니다

## 모듈 사용시

모듈의 출처 표기

https://github.com/TANAT96564/korcen

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

욕설 종류에 따라 1~9 출력

욕설이 아니라면 0

© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
