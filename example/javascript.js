const { check,general,minor,sexual,belittle,race,parent,foreign,special,politics } = require('korcen')
var content = "체크할 문자열"

console.log(check(content))
//모든 비속어

console.log(general(content))
//일반 욕설

console.log(minor(content))
//사소한 욕설

console.log(sexual(content))
//성적발언

console.log(belittle(content))
//비하발언

console.log(race(content))
//인종차별발언

console.log(parent(content))
//패드립

console.log(foreign(content))
//외국 욕설

console.log(special(content))
//특수(이모지)

console.log(politics(content))
//정치발언



//모듈 사용 출처 표기하기
