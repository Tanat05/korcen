const { check, general, minor, sexual, belittle, race, parent, foreign, special, politics } = require('korcen')

var content = "확인 할 문장"

var content = check(content)//모든 비속어
console.log(content) 

var content = general(content)//일반 욕설
console.log(content)

var content = minor(content)//사소한 욕설
console.log(content)

var content = sexual(content)//성적발언
console.log(content)

var content = belittle(content)//비하발언
console.log(content)

var content = race(content)//인종차별발언
console.log(content)

var content = parent(content)//패드립
console.log(content)

var content = foreign(content)//외국 욕설
console.log(content)

var content = special(content)//특수(이모지)
console.log(content)

var content = politics(content)//정치발언
console.log(content)



//모듈 사용 출처 표기하기
