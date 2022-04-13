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
        }else{
            return false;
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
        }else{
            return false;
        }
    }
    text = newtext.replace(/시발택시/gi, '')
    text = newtext.replace(/시발자동차/gi, '')
    text = newtext.replace(/정치발/gi, '')
    text = newtext.replace(/시발점/gi, '')
    text = newtext.replace(/시발유/gi, '')
    text = newtext.replace(/시발역/gi, '')
    text = newtext.replace(/시발수뢰/gi, '')
    text = newtext.replace(/아저씨바/gi, '')
    text = newtext.replace(/시바견/gi, '')
    text = newtext.replace(/시바/gi, '')
    text = newtext.replace(/이/gi, '')
    text = newtext.replace(/ㅣ/gi, '')
    fuck = ["시발", "씨발", "시봘", "씨봘", "씨바", "시바", "샤발", "씌발", "씹발", "시벌", "시팔", "싯팔", "씨빨", "씨랼", "씨파", "띠발", "띡발", "띸발","싸발", "십발", "슈발","야발", "씨불", "씨랄", "쉬발", "쓰발", "쓔발", "쌰발", "쉬발", "쒸발", "씨팔", "씨밝", "씨밯", "쑤발", "치발", "샤발", "발씨", "리발", "씨볼","찌발", "씨비바라랄", "시바랄", "씨바라"]
    for (const i of fuck) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
  
    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    text = newtext.replace(/근/gi, 'ㄹ')
    bullshit1 = ["ㅈㄹ", "지ㄹ", "ㅈ랄", "ㅈ라"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, 'ㄹ')
    text = newtext.replace(/지랄탄/gi, '')
    text = newtext.replace(/지랄버릇/gi, '')
    text = newtext.replace(/이/gi, '')
    bullshit2 = ["지랄", "찌랄", "지럴", "지롤", "랄지"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    text = newtext.replace(/빙/gi, '병')
    text = newtext.replace(/븅/gi, '병')
    text = newtext.replace(/등/gi, '병')
    text = newtext.replace(/붱/gi, '병')
    text = newtext.replace(/뵈/gi, '병')
    text = newtext.replace(/뼝/gi, '병')
    text = newtext.replace(/싄/gi, '신')
    text = newtext.replace(/씬/gi, '신')
    asshole = ["ㅄ", "ㅂㅅ", "병ㅅ", "ㅂ신", "ㅕㅇ신"]
    for (const i of asshole) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, '')
    text = newtext.replace(/영/gi, '')
    text = newtext.replace(/엉/gi, '')
    asshole = ["병신", "병딱", "벼신"]
    for (const i of asshole) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    text = newtext.replace(/전염병/gi, '')
    text = newtext.replace(/감염병/gi, '')
    motherfucker = ["염병", "엠병", "옘병", "염병", "얨병"]
    for (const i of motherfucker) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    text = newtext.replace(/왜꺼져/gi, '')
    text = newtext.replace(/꺼져요/gi, '')
    text = newtext.replace(/이꺼져/gi, '')
    text = newtext.replace(/꺼져서/gi, '')
    text = newtext.replace(/내꺼져/gi, '')
    text = newtext.replace(/제꺼져/gi, '')
    text = newtext.replace(/꺼져있/gi, '')
    if (text.includes("꺼져")){
        return true;
    }else{
        return false;
    }

    text = re.sub("[^가-힣]", "", newtext)
    shit = ["엿같", "엿가튼", "엿먹어"]
    for (const i of shit) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub(r,'\^', 'ㅅ', newtext)
    text = re.sub('H', 'ㅐ', text)
    text = re.sub("[^가-힣]", "", text)
    sonofbitch = ["ㅅㄲ", "ㅅ끼", "ㅆ끼", "쎆", "쌖","쌔꺄","새꺄"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub('의새끼', '', text)
    text = re.sub('애', '', text)
    text = re.sub('에', '', text)
    text = re.sub('루세끼', '', text)
    text = re.sub('시세끼', '', text)
    text = re.sub('세끼먹', '', text)
    sonofbitch = ["새끼", "쉐리", "쌔끼", "썌끼", "쎼끼", "쌬끼", "샠끼","애쌔끼","세끼","이시키"]
    animal = ["고양이","사바나캣", "너구리", "붉은여우", "사막여우", "북극여우", "코요테", "딩고", "서벌", "오셀롯", "페럿", "스컹크", "라쿤", "수달", "몽구스",
    "미어캣", "사향고양이", "햄스터", "양", "알파카", "라마", "사슴", "토끼", "다람쥐", "앵무새", "부엉이", "올빼미", "거북이", "개구리"]
    for (i in animal)
        if (i in text)
            text = re.sub('새끼', '', text)
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^ㄱ-힣]", "", newtext)
    dick = ["ㅈ같", "ㅈ망", "ㅈ까", "ㅈ경"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
    text = re.sub("[^가-힣]", "", text)
    dick = ["좆", "촟", "조까", "좈", "쫒", "졷", "좃"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^가-힣]", "", text)
    damn = ["썅", "씨앙", "씨양"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    swear = ["tq", "qt"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^ㄱ-힣]", "", newtext)
    whatthefuck = ["뻑유", "뻐킹", "뻐큐"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^가-힣]", "", newtext)
        sonofagun = ["개같", "개가튼", "개쉑", "개스키", "개세끼", "개색히", "개가뇬", "개새기", "개쌔기", "개쌔끼", "쌖", "쎆", "새긔", "개소리", "개년", "개소리",
                    "개드립"]
        for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^ㄱ-힣]", "", newtext)
    damnit = ["ㅁㅊ", "ㅁ친", "ㅁ쳤"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
    text = re.sub("[^가-힣]", "", text)
    text = re.sub('이미친', '', text)
    text = re.sub('미친증', '', text)
    damnit = ["미친", "미쳤"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^가-힣]", "", text)
    picking = ["꼽냐", "꼽니", "꼽나"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^ㄱ-힣]", "", newtext)
    text = re.sub('보지도못', '', text)
    text = re.sub('보지도않', '', text)
    text = re.sub('켜보지', '', text)
    text = re.sub('보지맙', '', text)
    text = re.sub('초보지', '', text)
    text = re.sub('로보지', '', text)
    text = re.sub('홍보지', '', text)
    text = re.sub('서보지', '', text)
    text = re.sub('보지금', '', text)
    text = re.sub('정지금', '', text)
    text = re.sub('걸보지', '', text)
    text = re.sub('을보지', '', text)
    text = re.sub('나보지', '', text)
    text = re.sub('면접보지', '', text)
    text = re.sub('보지는', '', text)
    text = re.sub('보지지', '', text)
    text = re.sub('못보지', '', text)
    text = re.sub('보지않', '', text)
    text = re.sub('보지마', '', text)
    text = re.sub('보지말', '', text)
    text = re.sub('안보지', '', text)
    text = re.sub('오', '', text)
    pussy = ["보지"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }


    text = re.sub("[^ㄱ-힣]", "", newtext)
    onahole = ["ㅈㅈ빨", "자ㅈ", "ㅈ지빨"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
    text = re.sub("[^ㄱ-힣]", "", newtext)
    text = re.sub('남자지', '', text)
    text = re.sub('여자지', '', text)
    text = re.sub('감자지', '', text)
    text = re.sub('왁자지', '', text)
    text = re.sub('자지금', '', text)
    text = re.sub('자지러', '', text)
    text = re.sub('개발자지', '', text)
    text = re.sub('타자지', '', text)
    text = re.sub('못자지', '', text)
    text = re.sub('자지원', '', text)
    text = re.sub('사용자', '', text)
    text = re.sub('자지않', '', text)
    text = re.sub('자지마', '', text)
    text = re.sub('자지말', '', text)
    text = re.sub('지원자', '', text)
    text = re.sub('안자지', '', text)
    text = re.sub('아', '', text)
    dicks = ["자지"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }


    text = re.sub(r,'\^', 'ㅅ', newtext)
    text = re.sub('sex', '섹스', text)
    text = re.sub('s', 'ㅅ', text)
    text = re.sub('x', 'ㅅ', text)
    text = re.sub('엑', '', text)
    text = re.sub("[^ㄱ-힣]", "", text)
    sex = ["ㅅㅔㄱ스", "섹ㅅ", "ㅅ스", "세ㄱㅅ", "ㅅㅔㄱㅅ"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
    text = re.sub("[^가-힣]", "", newtext)
    text = re.sub("야스오", "", text)
    sex = ["섹스", "섻스", "쉑스", "섿스", "섹그", "야스", "색스", "셱스", "섁스", "세엑스", "썩스"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^가-힣]", "", newtext)
    fireegg = ["불알", "부랄", "뽕알", "뿅알", "뿌랄", "뿔알", "블알"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^ㄱ-힣]", "", newtext)
    onahole = ["오나홍", "오나홀", "ㅇㄴ홀"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
    

    text = re.sub("[^가-힣]", "", newtext)
    onahole = ["매춘부"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^가-힣]", "", newtext)
    onahole = ["자궁문신"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^가-힣]", "", newtext)
    onahole = ["모유물","로리물"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub('련', '년', newtext)
    text = re.sub('뇬', '년', text)
    text = re.sub('놈', '년', text)
    text = re.sub('러운지', '', text)
    text = re.sub('려운지', '', text)
    text = re.sub("[^가-힣]", "", text)
    belittling = ["따까리", "장애년", "찐따년", "싸가지", "창년", "썅년", "버러지", "고아년", "고아년", "개간년", "종간나", "도구년", "걸래년", "썅년", "씹년",
                "창녀", "머저리", "씹쓰래기", "씹쓰레기", "씹장생", "씹자식", "운지", "급식충", "틀딱충", "조센징", "매국노", "똥꼬충", "진지충", "듣보잡",
                "한남충","정신병자","중생아","돌팔이","김치녀","폰팔이","틀딱년"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^가-힣]", "", newtext)
    nigger = ["깜둥이", "흑형","조센진","짱개","짱깨","짱께","짱게","쪽바리","쪽파리","빨갱이",]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^ㄱ-힣]", "", newtext)
    your = ["ㄴㄱㅁ", "ㄴ금마", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
    text = re.sub("[^가-힣]", "", newtext)
    your = ["느금마", "느그엄마", "늑엄마", "늑금마", "느그애미", "넉엄마", "느그부모", "느그애비", "느금빠", "느그메", "느그빠"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub("[^가-힣]", "", newtext)
    text = re.sub("도", "", text)
    motherfuck = ["니애미", "노애미", "노앰", "앰뒤련",
                "아버지도없는게", "애미도없는게", "애비도없는게", "어머니도없는게", "니애비", "노애비","애미없","애비없","애미뒤","애비뒤"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    text = re.sub('[^a-z]', '', newtext)
    if (text.includes(("fuck")) {
        return true;
    }else{
        return false;
    }

    text = re.sub('[^a-z]', '', newtext)
    if (text.includes("commin")) {
        return true;
    }else{
        return false;
    }

    text = re.sub('[^a-z]', '', newtext)
    if (text.includes("knod")) {
        return true;
    }else{
        return false;
    }

    if (text.includes("cunt")) {
        return true;
    }else{
        return false;
    }

    text = re.sub('[^a-z]', '', newtext)
    if (text.includes("dotard")) {
        return true;
    }else{
        return false;
    }

    text = re.sub('[^a-z]', '', newtext)
    if (text.includes("dyke")) {
        return true;
    }else{
        return false;
    }

    emoji = ["🖕🏻", "👌🏻👈🏻", "👉🏻👌🏻", "🤏🏻", "🖕", "🖕🏼", "🖕🏽", "🖕🏾", "🖕🏿"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    mh = ["노시개", "노알라", "뇌사모", "뇌물현"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    ji = ["귀걸이아빠", "달창", "대깨문", "문재앙", "문죄앙", "문죄인", "문크예거", "훠훠훠", "문빠"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    gh = ["근혜어", "길라임", "나대블츠", "닭근혜", "댓통령", "레이디가카", "바쁜벌꿀", "수첩공주", "유신공주", "유체이탈화법", "칠푼이", "쿼터갓"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    jh = ["반인반신", "데미갓", "박정희"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    cs = ["간철수"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }

    mb = ["가카", "이명박근혜", "다스는누구겁니까?"]
    for (const i of bullshit1) {
        if (text.includes(i)) {
            return true;
        }else{
            return false;
        }
    }
}
