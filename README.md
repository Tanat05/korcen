<div align="center">
  <h1>korcen(코르센)</h1>
  
  [![PyPI version](https://img.shields.io/pypi/v/korcen.svg)](https://python.org/pypi/korcen)
  [![downloads](https://img.shields.io/pypi/dm/korcen.svg)](https://pypi.org/project/korcen/)
  
  [![NPM version](http://img.shields.io/npm/v/korcen.svg?style=flat-square)](https://www.npmjs.org/package/npm-expansions)
  [![downloads](http://img.shields.io/npm/dm/korcen.svg?style=flat-square)](https://www.npmjs.org/package/npm-expansions)
</div>

korean(한국어) censorship(검열)의 줄임말로 

누구나 쉽게 텍스트에 비속어가 있는지 확인이 가능합니다.

## Licenses

GNU General Public License v3.0

![image](https://user-images.githubusercontent.com/85154556/171647408-fb2d26c8-509b-4c7d-be93-9290b309e65d.png)

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

>PyPI  0.1.6
```py
from korcen import korcen

korcen = korcen.korcen()

text = input()
print(korcen.check(text))
```

>NPM 0.1.4
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
NPM 0.1.0 이후 버전 업데이트 제공

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



Copyright© All rights reserved.
