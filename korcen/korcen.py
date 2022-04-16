import re

class korcen:
    def check(self, text):
        ae = 0
        be = 0
        ce = 0
        de = 0
        ee = 0
        fe = 0
        ge = 0
        he = 0
        le = 0
        qe = 0

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        text = re.sub('𝗌', 's', text)
        text = re.sub('𝘴', 's', text)
        text = re.sub('𝙨', 's', text)
        text = re.sub('𝚜', 's', text)
        text = re.sub('𝐬', 's', text)
        text = re.sub('𝑠', 's', text)
        text = re.sub('𝒔', 's', text)
        text = re.sub('𝓈', 's', text)
        text = re.sub('𝓼', 's', text)
        text = re.sub('𝔰', 's', text)
        text = re.sub('𝖘', 's', text)
        text = re.sub('𝕤', 's', text)
        text = re.sub('ｓ', 's', text)
        text = re.sub('ⓢ', 's', text)
        text = re.sub('⒮', 's', text)
        text = re.sub('🅢', 's', text)
        text = re.sub('🆂', 's', text)
        text = re.sub('🅂', 's', text)
        text = re.sub('𝖾', 'e', text)
        text = re.sub('𝘦', 'e', text)
        text = re.sub('𝙚', 'e', text)
        text = re.sub('𝚎', 'e', text)
        text = re.sub('𝐞', 'e', text)
        text = re.sub('𝑒', 'e', text)
        text = re.sub('𝒆', 'e', text)
        text = re.sub('ℯ', 'e', text)
        text = re.sub('𝓮', 'e', text)
        text = re.sub('𝔢', 'e', text)
        text = re.sub('𝖊', 'e', text)
        text = re.sub('𝕖', 'e', text)
        text = re.sub('ｅ', 'e', text)
        text = re.sub('ⓔ', 'e', text)
        text = re.sub('⒠', 'e', text)
        text = re.sub('🅔', 'e', text)
        text = re.sub('🅴', 'e', text)
        text = re.sub('🄴', 'e', text)
        text = re.sub('𝗑', 'x', text)
        text = re.sub('𝘹', 'x', text)
        text = re.sub('𝙭', 'x', text)
        text = re.sub('𝚡', 'x', text)
        text = re.sub('𝐱', 'x', text)
        text = re.sub('𝑥', 'x', text)
        text = re.sub('𝒙', 'x', text)
        text = re.sub('𝓍', 'x', text)
        text = re.sub('𝔁', 'x', text)
        text = re.sub('𝔵', 'x', text)
        text = re.sub('𝖝', 'x', text)
        text = re.sub('𝕩', 'x', text)
        text = re.sub('ｘ', 'x', text)
        text = re.sub('ⓧ', 'x', text)
        text = re.sub('⒳', 'x', text)
        text = re.sub('🅧', 'x', text)
        text = re.sub('🆇', 'x', text)
        text = re.sub('🅇', 'x', text)
        newtext = re.sub(' ', '', text)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub('ㅗ먹어', 'ㅗ', newtext)
        text = re.sub('오ㅗㅗ', '', text)
        text = re.sub('오ㅗ', '', text)
        text = re.sub('호ㅗㅗ', '', text)
        text = re.sub('호ㅗ', '', text)
        text = re.sub('로ㅗㅗ', '', text)
        text = re.sub('로ㅗ', '', text)
        text = re.sub('옹ㅗㅗ', '', text)
        text = re.sub('옹ㅗ', '', text)
        text = re.sub('롤ㅗㅗ', '', text)
        text = re.sub('롤ㅗ', '', text)
        text = re.sub('요ㅗ', '', text)
        text = re.sub('우ㅗ', '', text)
        text = re.sub('하ㅗ', '', text)
        text = re.sub('ㅇㅗ', '', text)
        text = re.sub('ㅗㅜ', '', text)
        fuckyou = ["ㅗ", "┻", "┴", "┹", "_ㅣ_", "_l_", "_/_", "⊥", "_ |\_", "_|\_", "_ㅣ\_", "_I_"]
        for i in fuckyou:
            if i in text:
                ae = 1

        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('人', 'ㅅ', text)
        text = re.sub('丨', 'ㅣ', text)
        text = re.sub('甘', 'ㅂ', text)
        text = re.sub('卜', 'ㅏ', text)
        text = re.sub('1', 'ㅣ', text)
        text = re.sub('l', 'ㅣ', text)
        text = re.sub('bal', '발', text)
        text = re.sub('bar', '발', text)
        text = re.sub('bak', '발', text)
        text = re.sub('r', 'ㅏ', text)
        text = re.sub('ᐲ', 'ㅅ', text)
        text = re.sub('ᗨ', 'ㅂ', text)
        text = re.sub('si', 'ㅅ', text)
        text = re.sub('tl', 'ㅅ', text)
        text = re.sub('qkf', '발', text)
        text = re.sub('qk', '바', text)
        text = re.sub('tl', '시', text)
        text = re.sub('시ㅣ', '시', text)
        text = re.sub('씨ㅣ', '씨', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        fuck = ["시ㅂ", "시ㅏㄹ", "씨ㅂ", "씨ㅏㄹ", "ㅣ발", "ㅆ발", "ㅅ발", "ㅅㅂ", "ㅆㅂ", "ㅆ바", "ㅅ바",
                "시ㅂㅏ", "ㅅㅂㅏ", "시ㅏㄹ", "씨ㅏㄹ", "ㅅ불", "ㅆ불","ㅅ쁠", "ㅆ뿔"]
        for i in fuck:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", text)
        text = re.sub('시발택시', '', text)
        text = re.sub('시발자동차', '', text)
        text = re.sub('정치발', '', text)
        text = re.sub('시발점', '', text)
        text = re.sub('시발유', '', text)
        text = re.sub('시발역', '', text)
        text = re.sub('시발수뢰', '', text)
        text = re.sub('아저씨바', '', text)
        text = re.sub('아저씨발', '', text)
        text = re.sub('시바견', '', text)
        text = re.sub('시바', '', text)
        text = re.sub('이', '', text)
        text = re.sub('일', '', text)
        fuck = ["시발", "씨발", "시봘", "씨봘", "씨바", "시바", "샤발", "씌발", "씹발", "시벌", "시팔", "싯팔",
                "씨빨", "씨랼", "씨파", "띠발", "띡발", "띸발","싸발", "십발", "슈발","야발", "씨불", "씨랄",
                "쉬발", "쓰발", "쓔발", "쌰발", "쉬발", "쒸발", "씨팔", "씨밝", "씨밯", "쑤발", "치발", "샤발",
                "발씨", "리발", "씨볼","찌발", "씨비바라랄", "시바랄", "씨바라"]
        for i in fuck:
            if i in text:
                ae = 1

        text = re.sub('련', '놈', newtext)
        text = re.sub('뇬', '놈', text)
        text = re.sub('놈', '놈', text)
        text = re.sub('넘', '놈', text)
        fuck = ["10련아", "18것", "18넘", "18놈", "18럼", "18롬", "18새끼", "18세끼", "18세리", "18섹", "18쉑"]
        for i in fuck:
            if i in text:
                ae = 1

        text = re.sub("g랄", "지랄", text)
        text = re.sub("[^ㄱ-힣]", "", newtext)
        text = re.sub("근", "ㄹ", text)
        bullshit1 = ["ㅈㄹ", "지ㄹ", "ㅈ랄", "ㅈ라"]
        for i in bullshit1:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", text)
        text = re.sub('지랄탄', '', text)
        text = re.sub('지랄버릇', '', text)
        text = re.sub('이', '', text)
        bullshit2 = ["지랄", "찌랄", "지럴", "지롤", "랄지"]
        for i in bullshit2:
            if i in text:
                ae = 1

        text = re.sub("[^ㄱ-힣]", "", newtext)
        text = re.sub('빙', '병', text)
        text = re.sub('븅', '병', text)
        text = re.sub('등', '병', text)
        text = re.sub('붱', '병', text)
        text = re.sub('뵝', '병', text)
        text = re.sub('뼝', '병', text)
        text = re.sub('싄', '신', text)
        text = re.sub('씬', '신', text)
        asshole = ["ㅄ", "ㅂㅅ", "병ㅅ", "ㅂ신", "ㅕㅇ신"]
        for i in asshole:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", text)
        text = re.sub('영', '', text)
        text = re.sub('엉', '', text)
        asshole = ["병신", "병딱", "벼신"]
        for i in asshole:
            if i in text:
                ae = 1

        text = re.sub(r'[0-9]+', '', newtext)
        text = re.sub("[ㅂㅁㅋㅈㄴㅌㄷㅇㅊㄱㄹㅍㅅㅎㅃㅉㄸㄲㅆㅠㅛㅗㅜㅕㅓㅡㅑㅏㅐㅣㅔㄺㄼㄽㅃㅉㄸㄲㅆㅀㄿㄾㅘㅚㅟㅝㅞㅢㅙ]", "", text)
        text = re.sub("[\--z]", "", text)
        text = re.sub('전염병', '', text)
        motherfucker = ["염병", "엠병", "옘병", "염병", "얨병"]
        for i in motherfucker:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub('왜꺼져', '', text)
        text = re.sub('꺼져요', '', text)
        text = re.sub('이꺼져', '', text)
        text = re.sub('꺼져서', '', text)
        text = re.sub('내꺼져', '', text)
        text = re.sub('제꺼져', '', text)
        text = re.sub('꺼져있', '', text)
        if "꺼져" in text:
            ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        shit = ["엿같", "엿가튼", "엿먹어"]
        for i in shit:
            if i in text:
                ae = 1

        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('H', 'ㅐ', text)
        text = re.sub('10새', '새끼', text)
        text = re.sub('10섹', '새끼', text)
        text = re.sub('10쌔', '새끼', text)
        text = re.sub('10쎄', '새끼', text)
        text = re.sub('10새', '새끼', text)
        text = re.sub('10쉑', '새끼', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        sonofbitch = ["ㅅㄲ", "ㅅ끼", "ㅆ끼"]
        for i in sonofbitch:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", text)
        text = re.sub('의새끼', '', text)
        text = re.sub('애', '', text)
        text = re.sub('에', '', text)
        text = re.sub('루세끼', '', text)
        text = re.sub('시세끼', '', text)
        text = re.sub('세끼먹', '', text)
        sonofbitch = ["새끼", "쉐리", "쌔끼", "썌끼", "쎼끼", "쌬끼", "샠끼","세끼"]
        for i in sonofbitch:
            if i in text:
                ae = 1

        text = re.sub("[^ㄱ-힣]", "", newtext)
        dick = ["ㅈ같", "ㅈ망", "ㅈ까", "ㅈ경"]
        for i in dick:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", text)
        dick = ["좆", "촟", "조까", "좈", "쫒", "졷", "좃","좋같","좃같","좃물","좃밥"]
        for i in dick:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", text)
        damn = ["썅", "씨앙", "씨양"]
        for i in damn:
            if i in text:
                ae = 1

        swear = ["tq", "qt"]
        for i in swear:
            if text == i:
                ae = 1

        text = re.sub("[^ㄱ-힣]", "", newtext)
        whatthefuck = ["뻑유", "뻐킹", "뻐큐"]
        for i in whatthefuck:
            if i in text:
                ae = 1

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub("[^가-힣]", "", newtext)
        sonofagun = ["개같", "개가튼", "개쉑", "개스키", "개세끼", "개색히", "개가뇬", "개새기", "개쌔기", "개쌔끼", "쌖", "쎆", "새긔", "개소리", "개년", "개소리",
                    "개드립","개돼지","개씹창","개간나","개스끼","개섹기","개자식"]
        for i in sonofagun:
            if i in text:
                be = 2

        text = re.sub("[^ㄱ-힣]", "", newtext)
        damnit = ["ㅁㅊ", "ㅁ친", "ㅁ쳤"]
        for i in damnit:
            if i in text:
                be = 2
        text = re.sub("[^가-힣]", "", text)
        text = re.sub('이미친', '', text)
        text = re.sub('미친증', '', text)
        damnit = ["미친", "미쳤"]
        for i in damnit:
            if i in text:
                be = 2

        text = re.sub("[^가-힣]", "", text)
        picking = ["꼽냐", "꼽니", "꼽나"]
        for i in picking:
            if i in text:
                be = 2

        text = re.sub("[^ㄱ-힣]", "", text)
        picking = ["ㅈㄴ","ㅈ나","존ㄴ"]
        for i in picking:
            if i in text:
                be = 2
        text = re.sub("[^가-힣]", "", text)
        picking = ["존나","존내"]
        for i in picking:
            if i in text:
                be = 2

        text = re.sub("[^가-힣]", "", text)
        picking = ["뒤져","뒈져","뒈진","뒈질","디져라","디진다","디질래"]
        for i in picking:
            if i in text:
                be = 2

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub("[^ㄱ-힣]", "", newtext)
        text = re.sub('보g', '보지', text)
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
        pussy = ["보지","버지물","버짓물"]
        for i in pussy:
            if i in text:
                ce = 3


        text = re.sub("[^ㄱ-힣]", "", newtext)
        onahole = ["ㅈㅈ빨", "자ㅈ", "ㅈ지빨"]
        for i in onahole:
            if i in text:
                ce = 3
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
        for i in dicks:
            if i in text:
                ce = 3


        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('sex', '섹스', text)
        text = re.sub('s', 'ㅅ', text)
        text = re.sub('x', 'ㅅ', text)
        text = re.sub('엑', '', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        sex = ["ㅅㅔㄱ스", "섹ㅅ", "ㅅ스", "세ㄱㅅ", "ㅅㅔㄱㅅ"]
        for i in sex:
            if i in text:
                ce = 3
        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub("야스오", "", text)
        sex = ["섹스", "섻스", "쉑스", "섿스", "섹그", "야스", "색스", "셱스", "섁스", "세엑스", "썩스","섹수","섹파","섹하자"]
        for i in sex:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        fireegg = ["불알", "부랄", "뽕알", "뿅알", "뿌랄", "뿔알"]
        for i in fireegg:
            if i in text:
                ce = 3

        text = re.sub("[^ㄱ-힣]", "", newtext)
        onahole = ["오나홍", "오나홀", "ㅇㄴ홀"]
        for i in onahole:
            if i in text:
                ce = 3
        

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["매춘부","성노예"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["자궁문신"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["모유물","로리물","근친상간","룸섹스","원조교재"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["딸딸이","질싸","안에사정","자위남","자위녀","폰섹","포르노","폰세엑","폰쉑","폰쎅"]
        for i in onahole:
            if i in text:
                ce = 3

        onahole = ["g스팟"]
        for i in onahole:
            if i in newtext:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["크리토리스","클리토리스","페니스"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["젖까","젖가튼","젖나","젖만"]
        for i in onahole:
            if i in text:
                ce = 3

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub('련', '년', newtext)
        text = re.sub('뇬', '년', text)
        text = re.sub('놈', '년', text)
        text = re.sub('넘', '년', text)
        text = re.sub('러운지', '', text)
        text = re.sub('려운지', '', text)
        text = re.sub("[^가-힣]", "", text)
        belittling = ["따까리", "장애년", "찐따년", "싸가지", "창년", "썅년", "버러지", "고아년", "고아년", "개간년", "종간나", "도구년", "걸래년", "썅년", "씹년",
                    "창녀", "머저리", "씹쓰래기", "씹쓰레기", "씹장생", "씹자식", "운지", "급식충", "틀딱충", "조센징", "매국노", "똥꼬충", "진지충", "듣보잡",
                    "한남충","정신병자","중생아","돌팔이","김치녀","폰팔이","틀딱년","같은년","개돼중","쓰글년"]
        for i in belittling:
            if i in text:
                de = 4

 #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub("[^가-힣]", "", newtext)
        nigger = ["깜둥이", "흑형","조센진","짱개","짱깨","짱께","짱게","쪽바리","쪽파리","빨갱이",]
        for i in nigger:
            if i in text:
                ee = 5

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub("[^ㄱ-힣]", "", newtext)
        your = ["ㄴㄱㅁ", "ㄴ금마", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠"]
        for i in your:
            if i in text:
                fe = 6
        text = re.sub("[^가-힣]", "", newtext)
        your = ["느금마", "느그엄마", "늑엄마", "늑금마", "느그애미", "넉엄마", "느그부모", "느그애비", "느금빠", "느그메", "느그빠"]
        for i in your:
            if i in text:
                fe = 6

        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub("도", "", text)
        motherfuck = ["니애미", "노애미", "노앰", "앰뒤련",
                    "아버지도없는게", "애미도없는게", "애비도없는게", "어머니도없는게", "니애비", "노애비","애미없","애비없","애미뒤","애비뒤"]
        for i in motherfuck:
            if i in text:
                fe = 6

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub('[^a-z]', '', newtext)
        if "fuck" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "commie" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "knod" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "cunt" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "Dotard" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "Dyke" in text:
            ge = 7

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        emoji = ["🖕🏻", "👌🏻👈🏻", "👉🏻👌🏻", "🤏🏻", "🖕", "🖕🏼", "🖕🏽", "🖕🏾", "🖕🏿"]
        for i in emoji:
            if i in newtext:
                le = 9

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        mh = ["노시개", "노알라", "뇌사모", "뇌물현"]
        for i in mh:
            if i in newtext:
                qe = 10

        ji = ["귀걸이아빠", "달창", "대깨문", "문재앙", "문죄앙", "문죄인", "문크예거", "훠훠훠", "문빠"]
        for i in ji:
            if i in newtext:
                qe = 10

        gh = ["근혜어", "길라임", "나대블츠", "닭근혜", "댓통령", "레이디가카", "바쁜벌꿀", "수첩공주", "유신공주", "유체이탈화법", "칠푼이", "쿼터갓"]
        for i in gh:
            if i in newtext:
                qe = 10

        jh = ["반인반신", "데미갓", "박정희"]
        for i in jh:
            if i in newtext:
                qe = 10

        cs = ["간철수"]
        for i in cs:
            if i in newtext:
                qe = 10

        text = re.sub('가카카오톡', '', newtext)
        text = re.sub('가카톡', '', newtext)
        text = re.sub('가카페', '', newtext)
        mb = ["가카", "이명박근혜", "다스는누구겁니까?"]
        for i in mb:
            if i in text:
                qe = 10

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        if ae == 1:
            return True
        if be == 2:
            return True
        if ce == 3:
            return True
        if de == 4:
            return True
        if ee == 5:
            return True
        if fe == 6:
            return True
        if ge == 7:
            return True
        if le == 9:
            return True
        if qe == 10:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    def general(self, text):
        ae = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        text = re.sub('ㅗ먹어', 'ㅗ', newtext)
        text = re.sub('오ㅗㅗ', '', text)
        text = re.sub('오ㅗ', '', text)
        text = re.sub('호ㅗㅗ', '', text)
        text = re.sub('호ㅗ', '', text)
        text = re.sub('로ㅗㅗ', '', text)
        text = re.sub('로ㅗ', '', text)
        text = re.sub('옹ㅗㅗ', '', text)
        text = re.sub('옹ㅗ', '', text)
        text = re.sub('롤ㅗㅗ', '', text)
        text = re.sub('롤ㅗ', '', text)
        text = re.sub('요ㅗ', '', text)
        text = re.sub('우ㅗ', '', text)
        text = re.sub('하ㅗ', '', text)
        text = re.sub('ㅇㅗ', '', text)
        text = re.sub('ㅗㅜ', '', text)
        fuckyou = ["ㅗ", "┻", "┴", "┹", "_ㅣ_", "_l_", "_/_", "⊥", "_ |\_", "_|\_", "_ㅣ\_", "_I_"]
        for i in fuckyou:
            if i in text:
                ae = 1

        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('人', 'ㅅ', text)
        text = re.sub('丨', 'ㅣ', text)
        text = re.sub('甘', 'ㅂ', text)
        text = re.sub('卜', 'ㅏ', text)
        text = re.sub('1', 'ㅣ', text)
        text = re.sub('l', 'ㅣ', text)
        text = re.sub('bal', '발', text)
        text = re.sub('bar', '발', text)
        text = re.sub('bak', '발', text)
        text = re.sub('r', 'ㅏ', text)
        text = re.sub('ᐲ', 'ㅅ', text)
        text = re.sub('ᗨ', 'ㅂ', text)
        text = re.sub('si', 'ㅅ', text)
        text = re.sub('tl', 'ㅅ', text)
        text = re.sub('qkf', '발', text)
        text = re.sub('qk', '바', text)
        text = re.sub('tl', '시', text)
        text = re.sub('시ㅣ', '시', text)
        text = re.sub('씨ㅣ', '씨', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        fuck = ["시ㅂ", "시ㅏㄹ", "씨ㅂ", "씨ㅏㄹ", "ㅣ발", "ㅆ발", "ㅅ발", "ㅅㅂ", "ㅆㅂ", "ㅆ바", "ㅅ바",
                "시ㅂㅏ", "ㅅㅂㅏ", "시ㅏㄹ", "씨ㅏㄹ", "ㅅ불", "ㅆ불","ㅅ쁠", "ㅆ뿔"]
        for i in fuck:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", text)
        text = re.sub('시발택시', '', text)
        text = re.sub('시발자동차', '', text)
        text = re.sub('정치발', '', text)
        text = re.sub('시발점', '', text)
        text = re.sub('시발유', '', text)
        text = re.sub('시발역', '', text)
        text = re.sub('시발수뢰', '', text)
        text = re.sub('아저씨바', '', text)
        text = re.sub('아저씨발', '', text)
        text = re.sub('시바견', '', text)
        text = re.sub('시바', '', text)
        text = re.sub('이', '', text)
        text = re.sub('일', '', text)
        fuck = ["시발", "씨발", "시봘", "씨봘", "씨바", "시바", "샤발", "씌발", "씹발", "시벌", "시팔", "싯팔",
                "씨빨", "씨랼", "씨파", "띠발", "띡발", "띸발","싸발", "십발", "슈발","야발", "씨불", "씨랄",
                "쉬발", "쓰발", "쓔발", "쌰발", "쉬발", "쒸발", "씨팔", "씨밝", "씨밯", "쑤발", "치발", "샤발",
                "발씨", "리발", "씨볼","찌발", "씨비바라랄", "시바랄", "씨바라"]
        for i in fuck:
            if i in text:
                ae = 1

        text = re.sub('련', '놈', newtext)
        text = re.sub('뇬', '놈', text)
        text = re.sub('놈', '놈', text)
        text = re.sub('넘', '놈', text)
        fuck = ["10련아", "18것", "18넘", "18놈", "18럼", "18롬", "18새끼", "18세끼", "18세리", "18섹", "18쉑"]
        for i in fuck:
            if i in text:
                ae = 1

        text = re.sub("g랄", "지랄", text)
        text = re.sub("[^ㄱ-힣]", "", newtext)
        text = re.sub("근", "ㄹ", text)
        bullshit1 = ["ㅈㄹ", "지ㄹ", "ㅈ랄", "ㅈ라"]
        for i in bullshit1:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", text)
        text = re.sub('지랄탄', '', text)
        text = re.sub('지랄버릇', '', text)
        text = re.sub('이', '', text)
        bullshit2 = ["지랄", "찌랄", "지럴", "지롤", "랄지"]
        for i in bullshit2:
            if i in text:
                ae = 1

        text = re.sub("[^ㄱ-힣]", "", newtext)
        text = re.sub('빙', '병', text)
        text = re.sub('븅', '병', text)
        text = re.sub('등', '병', text)
        text = re.sub('붱', '병', text)
        text = re.sub('뵝', '병', text)
        text = re.sub('뼝', '병', text)
        text = re.sub('싄', '신', text)
        text = re.sub('씬', '신', text)
        asshole = ["ㅄ", "ㅂㅅ", "병ㅅ", "ㅂ신", "ㅕㅇ신"]
        for i in asshole:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", text)
        text = re.sub('영', '', text)
        text = re.sub('엉', '', text)
        asshole = ["병신", "병딱", "벼신"]
        for i in asshole:
            if i in text:
                ae = 1

        text = re.sub(r'[0-9]+', '', newtext)
        text = re.sub("[ㅂㅁㅋㅈㄴㅌㄷㅇㅊㄱㄹㅍㅅㅎㅃㅉㄸㄲㅆㅠㅛㅗㅜㅕㅓㅡㅑㅏㅐㅣㅔㄺㄼㄽㅃㅉㄸㄲㅆㅀㄿㄾㅘㅚㅟㅝㅞㅢㅙ]", "", text)
        text = re.sub("[\--z]", "", text)
        text = re.sub('전염병', '', text)
        motherfucker = ["염병", "엠병", "옘병", "염병", "얨병"]
        for i in motherfucker:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub('왜꺼져', '', text)
        text = re.sub('꺼져요', '', text)
        text = re.sub('이꺼져', '', text)
        text = re.sub('꺼져서', '', text)
        text = re.sub('내꺼져', '', text)
        text = re.sub('제꺼져', '', text)
        text = re.sub('꺼져있', '', text)
        if "꺼져" in text:
            ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        shit = ["엿같", "엿가튼", "엿먹어"]
        for i in shit:
            if i in text:
                ae = 1

        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('H', 'ㅐ', text)
        text = re.sub('10새', '새끼', text)
        text = re.sub('10섹', '새끼', text)
        text = re.sub('10쌔', '새끼', text)
        text = re.sub('10쎄', '새끼', text)
        text = re.sub('10새', '새끼', text)
        text = re.sub('10쉑', '새끼', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        sonofbitch = ["ㅅㄲ", "ㅅ끼", "ㅆ끼"]
        for i in sonofbitch:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", text)
        text = re.sub('의새끼', '', text)
        text = re.sub('애', '', text)
        text = re.sub('에', '', text)
        text = re.sub('루세끼', '', text)
        text = re.sub('시세끼', '', text)
        text = re.sub('세끼먹', '', text)
        sonofbitch = ["새끼", "쉐리", "쌔끼", "썌끼", "쎼끼", "쌬끼", "샠끼","세끼"]
        for i in sonofbitch:
            if i in text:
                ae = 1

        text = re.sub("[^ㄱ-힣]", "", newtext)
        dick = ["ㅈ같", "ㅈ망", "ㅈ까", "ㅈ경"]
        for i in dick:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", text)
        dick = ["좆", "촟", "조까", "좈", "쫒", "졷", "좃","좋같","좃같","좃물","좃밥"]
        for i in dick:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", text)
        damn = ["썅", "씨앙", "씨양"]
        for i in damn:
            if i in text:
                ae = 1

        swear = ["tq", "qt"]
        for i in swear:
            if text == i:
                ae = 1

        text = re.sub("[^ㄱ-힣]", "", newtext)
        whatthefuck = ["뻑유", "뻐킹", "뻐큐"]
        for i in whatthefuck:
            if i in text:
                ae = 1

        if ae == 1:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def minor(self, text):
        be = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        text = re.sub("[^가-힣]", "", newtext)
        sonofagun = ["개같", "개가튼", "개쉑", "개스키", "개세끼", "개색히", "개가뇬", "개새기", "개쌔기", "개쌔끼", "쌖", "쎆", "새긔", "개소리", "개년", "개소리",
                    "개드립","개돼지","개씹창","개간나","개스끼","개섹기","개자식"]
        for i in sonofagun:
            if i in text:
                be = 2

        text = re.sub("[^ㄱ-힣]", "", newtext)
        damnit = ["ㅁㅊ", "ㅁ친", "ㅁ쳤"]
        for i in damnit:
            if i in text:
                be = 2
        text = re.sub("[^가-힣]", "", text)
        text = re.sub('이미친', '', text)
        text = re.sub('미친증', '', text)
        damnit = ["미친", "미쳤"]
        for i in damnit:
            if i in text:
                be = 2

        text = re.sub("[^가-힣]", "", text)
        picking = ["꼽냐", "꼽니", "꼽나"]
        for i in picking:
            if i in text:
                be = 2

        text = re.sub("[^ㄱ-힣]", "", text)
        picking = ["ㅈㄴ","ㅈ나","존ㄴ"]
        for i in picking:
            if i in text:
                be = 2
        text = re.sub("[^가-힣]", "", text)
        picking = ["존나","존내"]
        for i in picking:
            if i in text:
                be = 2

        text = re.sub("[^가-힣]", "", text)
        picking = ["뒤져","뒈져","뒈진","뒈질","디져라","디진다","디질래"]
        for i in picking:
            if i in text:
                be = 2

        if be == 2:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def sexual(self, text):
        ce = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        text = re.sub("[^ㄱ-힣]", "", newtext)
        text = re.sub('보g', '보지', text)
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
        pussy = ["보지","버지물","버짓물"]
        for i in pussy:
            if i in text:
                ce = 3


        text = re.sub("[^ㄱ-힣]", "", newtext)
        onahole = ["ㅈㅈ빨", "자ㅈ", "ㅈ지빨"]
        for i in onahole:
            if i in text:
                ce = 3
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
        for i in dicks:
            if i in text:
                ce = 3


        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('sex', '섹스', text)
        text = re.sub('s', 'ㅅ', text)
        text = re.sub('x', 'ㅅ', text)
        text = re.sub('엑', '', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        sex = ["ㅅㅔㄱ스", "섹ㅅ", "ㅅ스", "세ㄱㅅ", "ㅅㅔㄱㅅ"]
        for i in sex:
            if i in text:
                ce = 3
        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub("야스오", "", text)
        sex = ["섹스", "섻스", "쉑스", "섿스", "섹그", "야스", "색스", "셱스", "섁스", "세엑스", "썩스","섹수","섹파","섹하자"]
        for i in sex:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        fireegg = ["불알", "부랄", "뽕알", "뿅알", "뿌랄", "뿔알"]
        for i in fireegg:
            if i in text:
                ce = 3

        text = re.sub("[^ㄱ-힣]", "", newtext)
        onahole = ["오나홍", "오나홀", "ㅇㄴ홀"]
        for i in onahole:
            if i in text:
                ce = 3
        

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["매춘부","성노예"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["자궁문신"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["모유물","로리물","근친상간","룸섹스","원조교재"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["딸딸이","질싸","안에사정","자위남","자위녀","폰섹","포르노","폰세엑","폰쉑","폰쎅"]
        for i in onahole:
            if i in text:
                ce = 3

        onahole = ["g스팟"]
        for i in onahole:
            if i in newtext:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["크리토리스","클리토리스"],"페니스"
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["젖까","젖가튼","젖나","젖만"]
        for i in onahole:
            if i in text:
                ce = 3

        if ce == 3:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def belittle(self, text):
        de = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        text = re.sub('련', '년', newtext)
        text = re.sub('뇬', '년', text)
        text = re.sub('놈', '년', text)
        text = re.sub('넘', '년', text)
        text = re.sub('러운지', '', text)
        text = re.sub('려운지', '', text)
        text = re.sub("[^가-힣]", "", text)
        belittling = ["따까리", "장애년", "찐따년", "싸가지", "창년", "썅년", "버러지", "고아년", "고아년", "개간년", "종간나", "도구년", "걸래년", "썅년", "씹년",
                    "창녀", "머저리", "씹쓰래기", "씹쓰레기", "씹장생", "씹자식", "운지", "급식충", "틀딱충", "조센징", "매국노", "똥꼬충", "진지충", "듣보잡",
                    "한남충","정신병자","중생아","돌팔이","김치녀","폰팔이","틀딱년","같은년","개돼중","쓰글년"]
        for i in belittling:
            if i in text:
                de = 4

        if de == 4:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def race(self, text):
        ee = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        text = re.sub("[^가-힣]", "", newtext)
        nigger = ["깜둥이", "흑형","조센진","짱개","짱깨","짱께","짱게","쪽바리","쪽파리","빨갱이",]
        for i in nigger:
            if i in text:
                ee = 5

        if ee == 5:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def parent(self, text):
        fe = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        text = re.sub("[^ㄱ-힣]", "", newtext)
        your = ["ㄴㄱㅁ", "ㄴ금마", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠"]
        for i in your:
            if i in text:
                fe = 6
        text = re.sub("[^가-힣]", "", newtext)
        your = ["느금마", "느그엄마", "늑엄마", "늑금마", "느그애미", "넉엄마", "느그부모", "느그애비", "느금빠", "느그메", "느그빠"]
        for i in your:
            if i in text:
                fe = 6

        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub("도", "", text)
        motherfuck = ["니애미", "노애미", "노앰", "앰뒤련",
                    "아버지도없는게", "애미도없는게", "애비도없는게", "어머니도없는게", "니애비", "노애비","애미없","애비없","애미뒤","애비뒤"]
        for i in motherfuck:
            if i in text:
                fe = 6

        if fe == 6:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def foreign(self, text):
        ge = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        text = re.sub('[^a-z]', '', newtext)
        if "fuck" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "commie" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "knod" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "cunt" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "Dotard" in text:
            ge = 7

        text = re.sub('[^a-z]', '', newtext)
        if "Dyke" in text:
            ge = 7

        if ge == 7:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def special(self, text):
        le = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        emoji = ["🖕🏻", "👌🏻👈🏻", "👉🏻👌🏻", "🤏🏻", "🖕", "🖕🏼", "🖕🏽", "🖕🏾", "🖕🏿"]
        for i in emoji:
            if i in newtext:
                le = 9

        if le == 9:
            return True
        else:
            return False

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    def politics(self, text):
        qe = 0

        text = text.lower()
        text = ''.join(char for char in text if char.isalnum())
        newtext = re.sub(' ', '', text)

        mh = ["노시개", "노알라", "뇌사모", "뇌물현"]
        for i in mh:
            if i in newtext:
                qe = 10

        ji = ["귀걸이아빠", "달창", "대깨문", "문재앙", "문죄앙", "문죄인", "문크예거", "훠훠훠", "문빠"]
        for i in ji:
            if i in newtext:
                qe = 10

        gh = ["근혜어", "길라임", "나대블츠", "닭근혜", "댓통령", "레이디가카", "바쁜벌꿀", "수첩공주", "유신공주", "유체이탈화법", "칠푼이", "쿼터갓"]
        for i in gh:
            if i in newtext:
                qe = 10

        jh = ["반인반신", "데미갓", "박정희"]
        for i in jh:
            if i in newtext:
                qe = 10

        cs = ["간철수"]
        for i in cs:
            if i in newtext:
                qe = 10

        mb = ["가카", "이명박근혜", "다스는누구겁니까?"]
        for i in mb:
            if i in newtext:
                qe = 10

        if qe == 10:
            return True
        else:
            return False




if __name__ == "__main__":
    korcen = korcen()
    while True:
        text = input()
        b = korcen.check(text)
        print(b)
