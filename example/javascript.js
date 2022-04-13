const { check, general, minor, sexual, belittle, race, parent, foreign, special, politics } = require('korcen')

var content = "확인 할 문장"

var result = check(content)//모든 비속어
console.log(result) 

var result = general(content)//일반 욕설
console.log(result)

var result = minor(content)//사소한 욕설
console.log(result)

var result = sexual(content)//성적발언
console.log(result)

var result = belittle(content)//비하발언
console.log(result)

var result = race(content)//인종차별발언
console.log(result)

var result = parent(content)//패드립
console.log(result)

var result = foreign(content)//외국 욕설
console.log(result)

var result = special(content)//특수(이모지)
console.log(result)

var result = politics(content)//정치발언
console.log(result)



//모듈 사용 출처 표기하기
