https://pypi.org/project/korcen/

# korcen(코르센)
korean(한국어) censorship(검열)의 줄임말로 

누구나 쉽게 텍스트에 비속어가 있는지 확인이 가능합니다

어떤 종류의 비속어인지까지 구별이 되는 모듈입니다

한국어와 일부 영어욕설를 지원합니다

TNS봇의 욕설 검열에 들어가는 코드입니다

https://discord.com/api/oauth2/authorize?client_id=848795383751639080&permissions=8&scope=bot%20applications.commands
## Licenses

모든 프로그램 모듈의 출처 표기

협의후 제거

https://github.com/TANAT96564/korcen

링크 또는 "디스코드 TNS 봇" 표기 

# Maker

>Tanat

discord:  Tanat#0206

email:    shrbwjd05@gmail.com

## Installation

```sh
$ pip install korcen

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

### 디스코드 봇 응용
```py
@bot.event
async def on_message(message):
    a = check.check(message.content)
    if a != 0:
        await message.delete()
```
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
