function check(text) {
    newtext = text.toLowerCase()
    text = newtext.replace(/ /gi, '')
    text = text.replace(/[^ㄱ-힣]/gi, '')
    text = text.replace(/ㅗ먹어/gi, 'ㅗ')
    text = text.replace(/오ㅗㅗ/gi, 'ㅗ')
    text = text.replace(/오ㅗ/gi, 'ㅗ')
    text = text.replace(/로ㅗㅗ/gi, 'ㅗ')
    text = text.replace(/로ㅗ/gi, 'ㅗ')
    text = text.replace(/호ㅗㅗ/gi, 'ㅗ')
    text = text.replace(/호ㅗ/gi, 'ㅗ')
    text = text.replace(/옹ㅗㅗ/gi, 'ㅗ')
    text = text.replace(/옹ㅗ/gi, 'ㅗ')
    text = text.replace(/롤ㅗㅗ/gi, 'ㅗ')
    text = text.replace(/롤ㅗ/gi, 'ㅗ')
    text = text.replace(/요ㅗ/gi, 'ㅗ')
    text = text.replace(/하ㅗ/gi, 'ㅗ')
    text = text.replace(/우ㅗ/gi, 'ㅗ')
    text = text.replace(/ㅇㅗ/gi, 'ㅗ')
    text = text.replace(/ㅗㅜ/gi, 'ㅗ')
    let fuckyou = ['ㅗ', '┻', '┴', '┹', '_ㅣ_', '_l_', '_/_', '⊥', '_ |\_', '_|\_', '_ㅣ\_', '_I_']
    for (const i of fuckyou) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/\^/gi, 'ㅅ')
    text = text.replace(/人/gi, 'ㅅ')
    text = text.replace(/丨/gi, 'ㅣ')
    text = text.replace(/甘/gi, 'ㅂ')
    text = text.replace(/卜/gi, 'ㅏ')
    text = text.replace(/1/gi, 'ㅣ')
    text = text.replace(/l/gi, 'ㅣ')
    text = text.replace(/bal/gi, '발')
    text = text.replace(/bar/gi, '발')
    text = text.replace(/r/gi, 'ㅏ')
    text = text.replace(/ᐲ/gi, 'ㅅ')
    text = text.replace(/ᗨ/gi, 'ㅂ')
    text = text.replace(/si/gi, '시')
    text = text.replace(/tl/gi, '시')
    text = text.replace(/qkf/gi, '발')
    text = text.replace(/qk/gi, '바')
    text = text.replace(/ㅣ/gi, '')
    text = text.replace(/[^ㄱ-힣]/gi, '')
    let fuck = ["시ㅂ", "시ㅏㄹ", "씨ㅂ", "씨ㅏㄹ", "ㅣ발", "ㅆ발", "ㅅ발", "ㅅㅂ", "ㅆㅂ", "ㅆ바", "ㅅ바", "시ㅂㅏ", "ㅅㅂㅏ", "시ㅏㄹ", "씨ㅏㄹ", "ㅅ불", "ㅆ불","ㅅ쁠", "ㅆ뿔"]
    for (const i of fuck) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = text.replace(/시발택시/gi, '')
    text = text.replace(/시발자동차/gi, '')
    text = text.replace(/정치발/gi, '')
    text = text.replace(/시발점/gi, '')
    text = text.replace(/시발유/gi, '')
    text = text.replace(/시발역/gi, '')
    text = text.replace(/시발수뢰/gi, '')
    text = text.replace(/아저씨바/gi, '')
    text = text.replace(/시바견/gi, '')
    text = text.replace(/시바/gi, '')
    text = text.replace(/이/gi, '')
    text = text.replace(/ㅣ/gi, '')
    fuck = ["시발", "씨발", "시봘", "씨봘", "씨바", "시바", "샤발", "씌발", "씹발", "시벌", "시팔", "싯팔", "씨빨", "씨랼", "씨파", "띠발", "띡발", "띸발","싸발", "십발", "슈발","야발", "씨불", "씨랄", "쉬발", "쓰발", "쓔발", "쌰발", "쉬발", "쒸발", "씨팔", "씨밝", "씨밯", "쑤발", "치발", "샤발", "발씨", "리발", "씨볼","찌발", "씨비바라랄", "시바랄", "씨바라"]
    for (const i of fuck) {
        if (text.includes(i)) {
            return true;
        }
    }
  
    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    text = text.replace(/근/gi, 'ㄹ')
    bullshit1 = ["ㅈㄹ", "지ㄹ", "ㅈ랄", "ㅈ라"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, 'ㄹ')
    text = text.replace(/지랄탄/gi, '')
    text = text.replace(/지랄버릇/gi, '')
    text = text.replace(/이/gi, '')
    bullshit2 = ["지랄", "찌랄", "지럴", "지롤", "랄지"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    text = text.replace(/빙/gi, '병')
    text = text.replace(/븅/gi, '병')
    text = text.replace(/등/gi, '병')
    text = text.replace(/붱/gi, '병')
    text = text.replace(/뵈/gi, '병')
    text = text.replace(/뼝/gi, '병')
    text = text.replace(/싄/gi, '신')
    text = text.replace(/씬/gi, '신')
    asshole = ["ㅄ", "ㅂㅅ", "병ㅅ", "ㅂ신", "ㅕㅇ신"]
    for (const i of asshole) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, '')
    text = text.replace(/영/gi, '')
    text = text.replace(/엉/gi, '')
    asshole = ["병신", "병딱", "벼신"]
    for (const i of asshole) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    text = text.replace(/전염병/gi, '')
    text = text.replace(/감염병/gi, '')
    motherfucker = ["염병", "엠병", "옘병", "염병", "얨병"]
    for (const i of motherfucker) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    text = text.replace(/왜꺼져/gi, '')
    text = text.replace(/꺼져요/gi, '')
    text = text.replace(/이꺼져/gi, '')
    text = text.replace(/꺼져서/gi, '')
    text = text.replace(/내꺼져/gi, '')
    text = text.replace(/제꺼져/gi, '')
    text = text.replace(/꺼져있/gi, '')
    if (text.includes("꺼져")){
        return true;
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    shit = ["엿같", "엿가튼", "엿먹어"]
    for (const i of shit) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/\^/gi, 'ㅅ')
    text = text.replace(/H/gi, 'ㅐ')
    text = text.replace(/[^가-힣]/gi, '')
    sonofbitch = ["ㅅㄲ", "ㅅ끼", "ㅆ끼", "쎆", "쌖","쌔꺄","새꺄"]
    for (const i of sonofbitch) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/의새끼/gi, '')
    text = text.replace(/애/gi, '')
    text = text.replace(/에/gi, '')
    text = text.replace(/루세끼/gi, '')
    text = text.replace(/시세끼/gi, '')
    text = text.replace(/세끼먹/gi, '')
    sonofbitch = ["새끼", "쉐리", "쌔끼", "썌끼", "쎼끼", "쌬끼", "샠끼","애쌔끼","세끼","이시키"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    dick = ["ㅈ같", "ㅈ망", "ㅈ까", "ㅈ경"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, '')
    dick = ["좆", "촟", "조까", "좈", "쫒", "졷", "좃"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    damn = ["썅", "씨앙", "씨양"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    whatthefuck = ["뻑유", "뻐킹", "뻐큐"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
        sonofagun = ["개같", "개가튼", "개쉑", "개스키", "개세끼", "개색히", "개가뇬", "개새기", "개쌔기", "개쌔끼", "쌖", "쎆", "새긔", "개소리", "개년", "개소리",
                    "개드립"]
        for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    damnit = ["ㅁㅊ", "ㅁ친", "ㅁ쳤"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, '')
    text = text.replace(/이미친/gi, '')
    text = text.replace(/미친증/gi, '')
    damnit = ["미친", "미쳤"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    picking = ["꼽냐", "꼽니", "꼽나"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

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
    pussy = ["보지"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }


    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    onahole = ["ㅈㅈ빨", "자ㅈ", "ㅈ지빨"]
    for (const i of bullshit1) {
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
    dicks = ["자지"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }


    text = newtext.replace(/\^/gi, 'ㅅ')
    text = text.replace(/sex/gi, '섹스')
    text = text.replace(/엑/gi, '')
    text = text.replace(/[^ㄱ-힣]/gi, '')
    sex = ["ㅅㅔㄱ스", "섹ㅅ", "ㅅ스", "세ㄱㅅ", "ㅅㅔㄱㅅ"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, '')
    text = text.replace(/야스오/gi, '')
    sex = ["섹스", "섻스", "쉑스", "섿스", "섹그", "야스", "색스", "셱스", "섁스", "세엑스", "썩스"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    fireegg = ["불알", "부랄", "뽕알", "뿅알", "뿌랄", "뿔알", "블알"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    onahole = ["오나홍", "오나홀", "ㅇㄴ홀"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }
    

    text = newtext.replace(/[^가-힣]/gi, '')
    onahole = ["매춘부"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    onahole = ["자궁문신"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    onahole = ["모유물","로리물"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/련/gi, '년')
    text = text.replace(/뇬/gi, '년')
    text = text.replace(/놈/gi, '년')
    text = text.replace(/러운지/gi, '')
    text = text.replace(/려운지/gi, '년')
    text = text.replace(/[^가-힣]/gi, '')
    belittling = ["따까리", "장애년", "찐따년", "싸가지", "창년", "썅년", "버러지", "고아년", "고아년", "개간년", "종간나", "도구년", "걸래년", "썅년", "씹년",
                "창녀", "머저리", "씹쓰래기", "씹쓰레기", "씹장생", "씹자식", "운지", "급식충", "틀딱충", "조센징", "매국노", "똥꼬충", "진지충", "듣보잡",
                "한남충","정신병자","중생아","돌팔이","김치녀","폰팔이","틀딱년"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    nigger = ["깜둥이", "흑형","조센진","짱개","짱깨","짱께","짱게","쪽바리","쪽파리","빨갱이",]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    your = ["ㄴㄱㅁ", "ㄴ금마", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, '')
    your = ["느금마", "느그엄마", "늑엄마", "늑금마", "느그애미", "넉엄마", "느그부모", "느그애비", "느금빠", "느그메", "느그빠"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    text = text.replace(/도/gi, '')
    motherfuck = ["니애미", "노애미", "노앰", "앰뒤련",
                "아버지도없는게", "애미도없는게", "애비도없는게", "어머니도없는게", "니애비", "노애비","애미없","애비없","애미뒤","애비뒤"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^a-z]/gi, '')
    if (text.includes(("fuck"))) {
        return true;
    }

    text = newtext.replace(/[^a-z]/gi, '')
    if (text.includes("commin")) {
        return true;
    }

    text = newtext.replace(/[^a-z]/gi, '')
    if (text.includes("knod")) {
        return true;
    }

    text = newtext.replace(/[^a-z]/gi, '')
    if (text.includes("cunt")) {
        return true;
    }

    text = newtext.replace(/[^a-z]/gi, '')
    if (text.includes("dotard")) {
        return true;
    }

    text = newtext.replace(/[^a-z]/gi, '')
    if (text.includes("dyke")) {
        return true;
    }

    emoji = ["🖕🏻", "👌🏻👈🏻", "👉🏻👌🏻", "🤏🏻", "🖕", "🖕🏼", "🖕🏽", "🖕🏾", "🖕🏿"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    mh = ["노시개", "노알라", "뇌사모", "뇌물현"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    ji = ["귀걸이아빠", "달창", "대깨문", "문재앙", "문죄앙", "문죄인", "문크예거", "훠훠훠", "문빠"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    gh = ["근혜어", "길라임", "나대블츠", "닭근혜", "댓통령", "레이디가카", "바쁜벌꿀", "수첩공주", "유신공주", "유체이탈화법", "칠푼이", "쿼터갓"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    jh = ["반인반신", "데미갓", "박정희"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    cs = ["간철수"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    mb = ["가카", "이명박근혜", "다스는누구겁니까?"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }
    }


    return false;
}
