<div align="center">
  <h1>korcen(코르센)</h1>
  
  [![image](https://img.shields.io/pypi/v/korcen.svg)](https://python.org/pypi/korcen)
  [![image](https://img.shields.io/pypi/l/korcen.svg)](https://python.org/pypi/korcen)
  [![image](https://img.shields.io/pypi/pyversions/korcen.svg)](https://python.org/pypi/korcen)
  [![downloads](https://img.shields.io/pypi/dm/korcen.svg)](https://pypi.org/project/korcen/)
</div>

korean(한국어) censorship(검열)의 줄임말로 

누구나 쉽게 텍스트에 비속어가 있는지 확인이 가능합니다.

## Licenses

모든 프로그램 모듈의 출처 표기

https://github.com/TANAT96564/korcen

링크 또는 "디스코드 TNS 봇" 표기 

## Installation
>PyPI
```sh
$ pip install korcen
```

>NPM
```sh
$ npm i korcen
```
# Example
모든 예시는 가장 최신버전의 모듈을 사용합니다.

비속어가 있다면 True 없다면 False 출력하는 예시입니다.

>PyPI  0.1.2
```py
from korcen import korcen

korcen = korcen.korcen()

text = input()
print(korcen.check(text))
```

>NPM 0.1.2
```js
const { check } = require('korcen')
var content = check("문자열")
console.log(content)
```

#### 자세한 예시들은 [example](https://github.com/Tanat05/korcen/tree/main/example) 파일 참고하세요.

# Maker


>Tanat
```
메인 개발자

github:   Tanat05
discord:  Tanat#0206
email:    shrbwjd05@gmail.com
```
>이루
```
PY→JS 작업 도움
NPM버전 업데이트 제공

github:   erukim
discord:  이루#6410
```
>kiss
```
JS→TS 변환과 깃허브 설정
https://github.com/Tanat05/korcen.ts

github:   kiss8981
discord:  kisss#4755
```



© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
