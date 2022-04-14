export function politics(text: string|any): boolean {
    if(!text) throw new Error('Korean: 확인할 텍스트를 입력해 주세요');
    if(typeof text !== 'string') throw new Error('Korean: String 타입만 입력 가능합니다');
    const newtext = text.toLowerCase()
    text = newtext.replace(/[^가-힣]/gi, '')
    const mh = ["노시개", "노알라", "뇌사모", "뇌물현"]
    for (const i of mh) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    const ji = ["귀걸이아빠", "달창", "대깨문", "문재앙", "문죄앙", "문죄인", "문크예거", "훠훠훠", "문빠"]
    for (const i of ji) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    const gh = ["근혜어", "길라임", "나대블츠", "닭근혜", "댓통령", "레이디가카", "바쁜벌꿀", "수첩공주", "유신공주", "유체이탈화법", "칠푼이", "쿼터갓"]
    for (const i of gh) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    const jh = ["반인반신", "데미갓", "박정희"]
    for (const i of jh) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    const cs = ["간철수"]
    for (const i of cs) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    const mb = ["가카", "이명박근혜", "다스는누구겁니까?"]
    for (const i of mb) {
        if (text.includes(i)) {
            return true;
        }
    }

    return false;
}