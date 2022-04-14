export function sexual(text: string|any): boolean {
    if(!text) throw new Error('Korean: 확인할 텍스트를 입력해 주세요');
    if(typeof text !== 'string') throw new Error('Korean: String 타입만 입력 가능합니다');
    const newtext = text.toLowerCase()
    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    text = text.replace(/보지도못/gi, '')
    text = text.replace(/보지도않/gi, '')
    text = text.replace(/켜보지/gi, '')
    text = text.replace(/보지맙/gi, '')
    text = text.replace(/초보지/gi, '')
    text = text.replace(/로보지/gi, '')
    text = text.replace(/홍보지/gi, '')
    text = text.replace(/서보지/gi, '')
    text = text.replace(/보지금/gi, '')
    text = text.replace(/정지금/gi, '')
    text = text.replace(/걸보지/gi, '')
    text = text.replace(/을보지/gi, '')
    text = text.replace(/나보지/gi, '')
    text = text.replace(/면접보지/gi, '')
    text = text.replace(/보지는/gi, '')
    text = text.replace(/보지지/gi, '')
    text = text.replace(/못보지/gi, '')
    text = text.replace(/보지않/gi, '')
    text = text.replace(/보지마/gi, '')
    text = text.replace(/보지말/gi, '')
    text = text.replace(/안보지/gi, '')
    text = text.replace(/오/gi, '')
    const pussy = ["보지"]
    for (const i of pussy) {
        if (text.includes(i)) {
            return true;
        }
    }


    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    const onahole = ["ㅈㅈ빨", "자ㅈ", "ㅈ지빨"]
    for (const i of onahole) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    text = text.replace(/남자지/gi, '')
    text = text.replace(/여자지/gi, '')
    text = text.replace(/감자지/gi, '')
    text = text.replace(/왁자지/gi, '')
    text = text.replace(/자지금/gi, '')
    text = text.replace(/자지러/gi, '')
    text = text.replace(/개발자지/gi, '')
    text = text.replace(/타자지/gi, '')
    text = text.replace(/못보지/gi, '')
    text = text.replace(/자지원/gi, '')
    text = text.replace(/사용자/gi, '')
    text = text.replace(/자지않/gi, '')
    text = text.replace(/자지마/gi, '')
    text = text.replace(/자지말/gi, '')
    text = text.replace(/지원지/gi, '')
    text = text.replace(/안자지/gi, '')
    text = text.replace(/아/gi, '')
    const dicks = ["자지"]
    for (const i of dicks) {
        if (text.includes(i)) {
            return true;
        }
    }


    text = newtext.replace(/\^/gi, 'ㅅ')
    text = text.replace(/sex/gi, '섹스')
    text = text.replace(/엑/gi, '')
    text = text.replace(/[^ㄱ-힣]/gi, '')
    const sex = ["ㅅㅔㄱ스", "섹ㅅ", "ㅅ스", "세ㄱㅅ", "ㅅㅔㄱㅅ"]
    for (const i of sex) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, '')
    text = text.replace(/야스오/gi, '')
    const sex2 = ["섹스", "섻스", "쉑스", "섿스", "섹그", "야스", "색스", "셱스", "섁스", "세엑스", "썩스"]
    for (const i of sex2) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    const fireegg = ["불알", "부랄", "뽕알", "뿅알", "뿌랄", "뿔알", "블알"]
    for (const i of fireegg) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    const onahole2 = ["오나홍", "오나홀", "ㅇㄴ홀"]
    for (const i of onahole2) {
        if (text.includes(i)) {
            return true;
        }
    }
    

    text = newtext.replace(/[^가-힣]/gi, '')
    const onahole3 = ["매춘부"]
    for (const i of onahole3) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    const onahole4 = ["자궁문신"]
    for (const i of onahole) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    const onahole5 = ["모유물","로리물"]
    for (const i of onahole5) {
        if (text.includes(i)) {
            return true;
        }
    }

    return false;
}