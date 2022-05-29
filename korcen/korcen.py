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
        text = text.lower()
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
        text = re.sub('오ㅗㅗㅗㅗ', '', text)
        text = re.sub('오ㅗㅗㅗ', '', text)
        text = re.sub('호ㅗㅗㅗㅗ', '', text)
        text = re.sub('호ㅗㅗㅗ', '', text)
        text = re.sub('로ㅗㅗㅗㅗ', '', text)
        text = re.sub('로ㅗㅗㅗ', '', text)
        text = re.sub('옹ㅗㅗㅗㅗ', '', text)
        text = re.sub('옹ㅗㅗㅗ', '', text)
        text = re.sub('롤ㅗㅗㅗㅗ', '', text)
        text = re.sub('롤ㅗㅗㅗ', '', text)
        text = re.sub('요ㅗㅗㅗ', '', text)
        text = re.sub('우ㅗㅗㅗ', '', text)
        text = re.sub('하ㅗㅗㅗ', '', text)
        text = re.sub('ㅇㅗ', '', text)
        text = re.sub('ㅗㅜ', '', text)
        text = re.sub('rㅗ', '', text)
        text = re.sub('ㅗr', '', text)
        text = re.sub('sㅗ', '', text)
        text = re.sub('ㅗs', '', text)
        text = re.sub('eㅗ', '', text)
        text = re.sub('ㅗe', '', text)
        text = re.sub('fㅗ', '', text)
        text = re.sub('ㅗf', '', text)
        text = re.sub('aㅗ', '', text)
        text = re.sub('ㅗa', '', text)
        text = re.sub('qㅗ', '', text)
        text = re.sub('ㅗq', '', text)
        text = re.sub('ㅗw', '', text)
        text = re.sub('wㅗ', '', text)
        text = re.sub('ㅗd', '', text)
        text = re.sub('dㅗ', '', text)
        text = re.sub('ㅗg', '', text)
        text = re.sub('gㅗ', '', text)
        fuckyou = ["ㅗ", "┻", "┴", "┹", "_ㅣ_", "_l_", "_/_", "⊥", "_ |\_", "_|\_", "_ㅣ\_", "_I_"]
        for i in fuckyou:
            if i in text:
                ae = 1


        fuck = ["tq","qt"]
        for i in fuck:
            if i == text:
                ae = 1
        text = re.sub('118', '', text)
        text = re.sub('218', '', text)
        text = re.sub('318', '', text)
        text = re.sub('418', '', text)
        text = re.sub('518', '', text)
        text = re.sub('618', '', text)
        text = re.sub('718', '', text)
        text = re.sub('818', '', text)
        text = re.sub('918', '', text)
        text = re.sub('018', '', text)
        fuck = ["씨8","18아","18놈","18련""tㅂ","t발","ㅅㅍ","ㅆㅍ","18뇬",
                "sibal","sival","sibar","sibak","sipal","siqk","tlbal","tlval","tlbar","tlbak","tlpal","tlqk"
                "시bal","시val","시bar","시bak","시pal","시qk","시bal","시val","시bar","시bak","시pal","시qk"
                "si바","si발","si불","si빨","si팔","tl바","tl발","tl불","tl빨""tl팔",
                "siba","tlba","siva","tlva","tlqkf","10발련","10발넘","10발놈","10발년","tlqkd","si8"]
        for i in fuck:
            if i in text:
                ae = 1
        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('人', 'ㅅ', text)
        text = re.sub('丨', 'ㅣ', text)
        text = re.sub('甘', 'ㅂ', text)
        text = re.sub('卜', 'ㅏ', text)
        text = re.sub('l', 'ㅣ', text)
        text = re.sub('r', 'ㅏ', text)
        text = re.sub('ᐲ', 'ㅅ', text)
        text = re.sub('ᗨ', 'ㅂ', text)
        text = re.sub('시ㅣ', '시', text)
        text = re.sub('씨ㅣ', '씨', text)
        text = re.sub('ㅅ1', '시', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        fuck = ["시ㅂ", "시ㅏㄹ", "씨ㅂ", "씨ㅏㄹ", "ㅣ발", "ㅆ발", "ㅅ발", "ㅅㅂ", "ㅆㅂ", "ㅆ바", "ㅅ바",
                "시ㅂㅏ", "ㅅㅂㅏ", "시ㅏㄹ", "씨ㅏㄹ", "ㅅ불", "ㅆ불","ㅅ쁠", "ㅆ뿔","ㅆㅣ발","ㅅㅟ발","ㅅㅣㅂㅏ",
                "ㅣ바알","씨바알","샤빨","샤발","스벌","쓰벌","신발련","신발년","신발놈","ㅅ벌","시불","시부렝"
                ,"씨부렝","시부랭","씨부랭","^^ㅣ벌","시부랭"]
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
        text = re.sub('이', '', text)
        text = re.sub('일', '', text)
        text = re.sub('벌어', '', text)
        text = re.sub('시바이누', '', text)
        text = re.sub('시바스리갈', '', text)
        text = re.sub('시바산', '', text)
        text = re.sub('시바신', '', text)
        text = re.sub('오리발', '', text)
        text = re.sub('발끝', '', text)
        text = re.sub('다시바', '', text)
        text = re.sub('비슈누시바', '', text)
        text = re.sub('시바핫카이', '', text)
        text = re.sub('시바타이쥬', '', text)
        text = re.sub('데스티니시바', '', text)
        text = re.sub('시바루', '', text)
        text = re.sub('시바료타로', '', text)
        text = re.sub('시바라스시', '', text)
        text = re.sub('젤리', '', text)
        text = re.sub('발사', '', text)
        text = re.sub('크시', '', text)
        text = re.sub('크시야', '', text)
        text = re.sub('어찌', '', text)
        text = re.sub('발로란트', '', text)
        fuck = ["시발", "씨발", "시봘", "씨봘", "씨바", "시바", "샤발", "씌발", "씹발", "시벌", "시팔", "싯팔",
                "씨빨", "씨랼", "씨파", "띠발", "띡발", "띸발","싸발", "십발", "슈발","야발", "씨불", "씨랄",
                "쉬발", "쓰발", "쓔발", "쌰발", "쉬발", "쒸발", "씨팔", "씨밝", "씨밯", "쑤발", "치발", "샤발",
                "발씨", "리발", "씨볼","찌발", "씨비바라랄", "시바랄", "씨바라","쒸팔","쉬팔","씨밮","쒸밮","시밮","씨삐라","ㅆ삐라","씨벌","슈벌"]
        for i in fuck:
            if i in text:
                ae = 1

        text = re.sub('련', '놈', newtext)
        text = re.sub('뇬', '놈', text)
        text = re.sub('놈', '놈', text)
        text = re.sub('넘', '놈', text)
        fuck = ["18것", "18놈", "18럼", "18롬", "18새끼", "18세끼", "18세리", "18섹", "18쉑", "10쉑"]
        for i in fuck:
            if i in text:
                ae = 1

        bullshit1 = ["wlfkf","g랄", "g럴", "g롤","g뢀"]
        for i in bullshit1:
            if i in text:
                ae = 1
        text = re.sub("g랄", "지랄", newtext)
        text = re.sub("[^ㄱ-힣]", "", text)
        text = re.sub("있지", "", text)
        text = re.sub("없지", "", text)
        text = re.sub("하지", "", text)
        text = re.sub("근", "ㄹ", text)
        text = re.sub("ㄹㅇ", "", text)
        bullshit1 = ["ㅈㄹ", "지ㄹ", "ㅈ랄", "ㅈ라"]
        for i in bullshit1:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub('지랄탄', '', text)
        text = re.sub('지랄버릇', '', text)
        text = re.sub('이', '', text)
        bullshit2 = ["지랄", "찌랄", "지럴", "지롤", "랄지","쥐랄","쮜랄","지뢀"]
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
        text = re.sub('우', '', text)
        text = re.sub('웅', '', text)
        asshole = ["ㅄ", "ㅂㅅ", "병ㅅ", "ㅂ신", "ㅕㅇ신","ㅂㅇ신","뷰신"]
        for i in asshole:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", text)
        text = re.sub('영', '', text)
        text = re.sub('엉', '', text)
        asshole = ["병신", "병딱", "벼신","붱신","뼝신","뿽신","삥신","병시니"]
        for i in asshole:
            if i in text:
                ae = 1

        text = re.sub(r'[0-9]+', '', newtext)
        text = re.sub("[ㅂㅁㅋㅈㄴㅌㄷㅇㅊㄱㄹㅍㅅㅎㅃㅉㄸㄲㅆㅠㅛㅗㅜㅕㅓㅡㅑㅏㅐㅣㅔㄺㄼㄽㅃㅉㄸㄲㅆㅀㄿㄾㅘㅚㅟㅝㅞㅢㅙ]", "", text)
        text = re.sub("[\--z]", "", text)
        text = re.sub('전염병', '', text)
        motherfucker = ["염병", "엠병", "옘병", "염병", "얨병","옘뼝"]
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
        text = re.sub('꺼져도', '', text)
        if "꺼져" in text:
            ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        shit = ["엿같", "엿가튼", "엿먹어"]
        for i in shit:
            if i in text:
                ae = 1

        sonofbitch = ["rotorl","rotprl","sib새"]
        for i in sonofbitch:
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
        text = re.sub('고양이새끼', '', text)
        text = re.sub('키보드', '', text)
        sonofbitch = ["새끼", "쉐리", "쌔끼", "썌끼", "쎼끼", "쌬끼", "샠끼","세끼","샊","쌖","섺","쎆","십새","새키","씹색"]
        for i in sonofbitch:
            if i in text:
                ae = 1

        dick = ["w같은"]
        for i in dick:
            if i in newtext:
                ae = 1
        text = re.sub("[^ㄱ-힣]", "", newtext)
        text = re.sub('줫습니다', '', text)
        dick = ["ㅈ같", "ㅈ망", "ㅈ까", "ㅈ경"]
        for i in dick:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", text)
        dick = ["좆", "촟", "조까", "좈", "쫒", "졷", "좃","좋같","좃같","좃물","좃밥","줫","좋밥","좋물","좇"]
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
        whatthefuck = ["뻑유", "뻐킹", "뻐큐","빡큐","뿩큐","뻑큐","빡유"]
        for i in whatthefuck:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        shutup = ["닥쳐", "닭쳐","닥치라"]
        for i in shutup:
            if i in text:
                ae = 1

        text = re.sub(r'[0-9]+', '', newtext)
        sonofagun = ["dog새"]
        for i in sonofagun:
            if i in text:
                ae = 1
        text = re.sub("[^ㄱ-힣]", "", newtext)
        sonofagun = ["개ㅐ색"]
        for i in sonofagun:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", newtext)
        sonofagun = ["개같", "개가튼", "개쉑", "개스키", "개세끼", "개색히", "개가뇬", "개새기", "개쌔기", "개쌔끼", "쌖", "쎆", "새긔", "개소리", "개년", "개소리",
                    "개드립","개돼지","개씹창","개간나","개스끼","개섹기","개자식","개때꺄","개때끼","개발남아","개샛끼","개가든","개가뜬","개가턴","개가툰","개가튼",
                    "개갇은","개갈보","개걸레","개너마","개너므","개넌","개넘","개녀나","개년","개노마","개노무새끼","개논","개놈","개뇨나","개뇬","개뇸","개뇽","개눔",
                    "개느마","개늠","개때꺄","개때끼","개떼끼","개랙기","개련","개발남아","개발뇬","개색","개색끼","개샊","개샛끼","개샛키","개샛킹","개샛히","개샜끼",
                    "개생키","개샠","개샤끼","개샤킥","개샥","개샹늠","개세끼","개세리","개세키","개섹히","개섺","개셃","개셋키","개셐","개셰리","개솩","개쇄끼","개쇅",
                    "개쇅끼","개쇅키","개쇗","개쇠리","개쉐끼","개쉐리","개쉐키","개쉑","개쉑갸","개쉑기","개쉑꺄","개쉑끼","개쉑캬","개쉑키","개쉑히","개쉢","개쉨",
                    "개쉬","개쉬끼","개쉬리","개쉽","개스끼","개스키","개습","개습세","개습쌔","개싀기","개싀끼","개싀밸","개싀킈","개싀키","개싏","개싑창","개싘",
                    "개시끼","개시퀴","개시키","개식기","개식끼","개식히","개십새","개십팔","개싯기","개싯끼","개싯키","개싴","개쌍넘","개쌍년","개쌍놈","개쌍눔",
                    "개쌍늠","개쌍연","개쌍영","개쌔꺄","개쌔끼","개쌕","개쌕끼","개쌰깨","개썅","개쎄","개쎅","개쎼키","개쐐리","개쒜","개쒝","개쒯","개쒸","개쒸빨놈",
                    "개쒹기","개쓉","개쒹기","개쓉","개씀","개씁","개씌끼","개씨끼","개씨팕","개씨팔","개잡것","개잡년","개잡놈","개잡뇬","개젓","개젖","개젗","개졋",
                    "개졎","개조또","개조옷","개족","개좃","개좆","개좇","개지랄","개지럴","개창년","개허러","개허벌년","개호러","개호로","개후랄","개후레","개후로",
                    "개후장","걔섀끼","걔잡넘","걔잡년","걔잡뇬","게가튼","게같은","게너마","게넘","게년","게노마","게놈","게뇨나","게뇬","게뇸","게뇽","게눔","게늠",
                    "게띠발넘","게부랄","게부알","게새끼","게새리","게새키","게색","게색기","게색끼","게샛키","게세꺄","게자지","게잡넘","게잡년","게잡뇬","게젓",
                    "게좆","계같은뇬","계뇬","계뇽"]
        for i in sonofagun:
            if i in text:
                ae = 1

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub("[^ㄱ-힣]", "", newtext)
        damnit = ["ㅁㅊ", "ㅁ친", "ㅁ쳤","aㅣ친","me친"]
        for i in damnit:
            if i in text:
                be = 2
        text = re.sub("[^가-힣]", "", text)
        text = re.sub('이미친', '', text)
        text = re.sub('미친증', '', text)
        text = re.sub('거미', '', text)
        text = re.sub('친구', '', text)
        damnit = ["미친", "미쳤","무친놈"]
        for i in damnit:
            if i in text:
                be = 2

        text = re.sub("[^가-힣]", "", text)
        picking = ["꼽냐", "꼽니", "꼽나"]
        for i in picking:
            if i in text:
                be = 2

        text = re.sub("[^ㄱ-힣]", "", text)
        picking = ["ㅈㄴ","ㅈ나","존ㄴ","존맛"]
        for i in picking:
            if i in text:
                be = 2
        text = re.sub("[^가-힣]", "", text)
        text = re.sub("그만 졸라", "ㄹ", text)
        text = re.sub("졸라서", "", text)
        picking = ["존나","존내","쫀나","존네","졸라"]
        for i in picking:
            if i in text:
                be = 2

        text = re.sub("[^가-힣]", "", text)
        picking = ["뒤져","뒈져","뒈진","뒈질","디져라","디진다","디질래"]
        for i in picking:
            if i in text:
                be = 2

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        pussy = ["ⓑⓞⓩⓘ","bozi"]
        for i in pussy:
            if i in newtext:
                ce = 3
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
        text = re.sub('정보', '', text)
        text = re.sub('지팡이', '', text)
        text = re.sub('행보', '', text)
        text = re.sub('오', '', text)
        pussy = ["보지","버지물","버짓물","보짓","ⓑⓞⓩⓘ","bozi","개보즤","개보지"]
        for i in pussy:
            if i in text:
                ce = 3


        dicks = ["ja지"]
        for i in dicks:
            if i in newtext:
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
        text = re.sub('개발자', '', text)
        text = re.sub('관리자', '', text)
        text = re.sub('타자지', '', text)
        text = re.sub('혼자', '', text)
        text = re.sub('못자지', '', text)
        text = re.sub('자지원', '', text)
        text = re.sub('사용자', '', text)
        text = re.sub('자지않', '', text)
        text = re.sub('자지마', '', text)
        text = re.sub('자지말', '', text)
        text = re.sub('지원자', '', text)
        text = re.sub('안자지', '', text)
        text = re.sub('부자지', '', text)
        text = re.sub('아', '', text)
        dicks = ["자지","자짓"]
        for i in dicks:
            if i in text:
                ce = 3


        sex = ["s스", "x스", "se스", "se스", "s스","ㅅㅅ","s하고e싶다x"]
        for i in sex:
            if i in newtext:
                ce = 3
        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('sex', '섹스', text)
        text = re.sub('엑', '', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        sex = ["ㅅㅔㄱ스", "섹ㅅ", "ㅅ스", "세ㄱㅅ", "ㅅㅔㄱㅅ"]
        for i in sex:
            if i in text:
                ce = 3
        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub("야스오", "", text)
        text = re.sub("크시야", "", text)
        text = re.sub("카구야", "", text)
        text = re.sub("스파이", "", text)
        sex = ["섹스", "섻스", "쉑스", "섿스", "섹그", "야스", "색스", "셱스", "섁스", "세엑스", "썩스","섹수","섹파","섹하자","쉐스","쉑스","쉐엑스"]
        for i in sex:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        fireegg = ["불알", "부랄", "뽕알", "뿅알", "뿌랄", "뿔알","개부달","개부랄","개부러럴","개부럴","개부뢀","개부알","개불알"]
        for i in fireegg:
            if i in text:
                ce = 3

        text = re.sub("[^ㄱ-힣]", "", newtext)
        onahole = ["오나홍", "오나홀", "ㅇㄴ홀","텐가","바이브레이터","오ㄴ홀","ㅇ나홀"]
        for i in onahole:
            if i in text:
                ce = 3
        
        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["씹하다"]
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
        onahole = ["모유물","로리물","근친상간","룸섹스","원조교재","속박플레이","야플","야외플레이"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["딸딸이","질싸","안에사정","자위남","자위녀","폰섹","포르노","폰세엑","폰쉑","폰쎅","질내사정","그룹섹","남창","男色","누워라이년아","누웠냐씨방새",]
        for i in onahole:
            if i in text:
                ce = 3

        onahole = ["g스팟","지스팟"]
        for i in onahole:
            if i in newtext:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["크리토리스","클리토리스","페니스","애널"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["젖까","젖가튼","젖나","젖만"]
        for i in onahole:
            if i in text:
                ce = 3

        onahole = ["ja위"]
        for i in onahole:
            if i in text:
                ce = 3
        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["자위","고자새끼","고츄","꺼추","께세","꼬추"]
        for i in onahole:
            if i in text:
                ce = 3

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub('뇬', '련', newtext)
        text = re.sub('놈', '련', text)
        text = re.sub('넘', '련', text)
        belittling = ["10련"]
        for i in belittling:
            if i in text:
                de = 4
        text = re.sub('련', '년', newtext)
        text = re.sub('뇬', '년', text)
        text = re.sub('놈', '년', text)
        text = re.sub('넘', '년', text)
        text = re.sub('러운지', '', text)
        text = re.sub('려운지', '', text)
        text = re.sub('무서운지', '', text)
        text = re.sub("[^가-힣]", "", text)
        belittling = ["따까리", "장애년", "찐따년", "싸가지", "창년", "썅년", "버러지", "고아년", "고아년", "개간년", "종간나", "도구년", "걸래년", "썅년", "씹년",
                    "창녀", "머저리", "씹쓰래기", "씹쓰레기", "씹장생", "씹자식", "운지", "급식충", "틀딱충", "조센징", "매국노", "똥꼬충", "진지충", "듣보잡",
                    "한남충","정신병자","중생아","돌팔이","김치녀","폰팔이","틀딱년","같은년","개돼중","쓰글년","썩을년","썩글년","씹할","거지새끼","거지쉐뀌",
                    "거지쉑이","거지쎄끼","거지쒜리","걸래가튼","걸래넘","걸래년","걸래놈","걸레가튼","걸레년","그지새끼","그지새키","그지색","기집년","까진년",
                    "깔보","난잡년"]
        for i in belittling:
            if i in text:
                de = 4

 #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub("[^가-힣]", "", newtext)
        nigger = ["깜둥이", "흑형","조센진","짱개","짱깨","짱께","짱게","쪽바리","쪽파리","빨갱이"]
        for i in nigger:
            if i in text:
                ee = 5

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        your = ["ㄴ1ㄱ", "ㄴ1ㅁ", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠","ㅇH미","ㄴ1에미"]
        for i in your:
            if i in newtext:
                fe = 6
        text = re.sub("[^ㄱ-힣]", "", newtext)
        your = ["ㄴㄱㅁ", "ㄴ금마", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠","ㄴ미"]
        for i in your:
            if i in text:
                fe = 6
        text = re.sub("[^가-힣]", "", newtext)
        your = ["느금마", "느그엄마", "늑엄마", "늑금마", "느그애미", "넉엄마", "느그부모", "느그애비", "느금빠", "느그메", "느그빠","니미씨","니미씹",
        "느그마","니엄마","엄창","엠창","니미럴","누굼마","느금","내미랄","내미럴"]
        for i in your:
            if i in text:
                fe = 6

        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub("도", "", text)
        motherfuck = ["니애미", "노애미", "노앰", "앰뒤련",
                    "아버지도없는게", "애미도없는게", "애비도없는게", "어머니도없는게", "니애비", "노애비","애미없","애비없","애미뒤","애비뒤","니아빠","너에미"]
        for i in motherfuck:
            if i in text:
                fe = 6

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        text = re.sub('[^a-z]', '', newtext)
        eng = ['abbo', 'abo'
        , 'abortion', 'abuse', 'addict', 'addicts', 'adult', 'africa', 'african', 'alla', 'allah', 'alligatorbait', 'amateur', 'american'
        , 'anal', 'analannie', 'analsex', 'angie', 'angry', 'anus', 'arab', 'arabs', 'areola', 'argie', 'aroused', 'arse', 'arsehole', 'asian'
        , 'ass', 'assassin', 'assassinate', 'assassination', 'assault', 'assbagger', 'assblaster', 'assclown', 'asscowboy', 'asses', 'assfuck'
        , 'assfucker', 'asshat', 'asshole', 'assholes', 'asshore', 'assjockey', 'asskiss', 'asskisser', 'assklown', 'asslick', 'asslicker', 'asslover'
        , 'assman', 'assmonkey', 'assmunch', 'assmuncher', 'asspacker', 'asspirate', 'asspuppies', 'assranger', 'asswhore', 'asswipe', 'athletesfoot'
        , 'attack', 'australian', 'backdoor', 'backdoorman', 'backseat', 'badfuck', 'balllicker', 'balls', 'ballsack', 'banging', 'baptist', 'barelylegal'
        , 'barf', 'barface', 'barfface', 'bast', 'bastard', 'bazongas', 'bazooms', 'beaner', 'beast', 'beastality', 'beastial', 'beastiality', 'beatoff'
        , 'beat-off', 'beatyourmeat', 'beaver', 'bestial', 'bestiality', 'bi', 'biatch', 'bicurious', 'bigass', 'bigbastard', 'bigbutt', 'bigger', 'bisexual'
        , 'bi-sexual', 'bitch', 'bitcher', 'bitches', 'bitchez', 'bitchin', 'bitching', 'bitchslap', 'bitchy', 'biteme', 'black', 'blackman', 'blackout'
        , 'blacks', 'blind', 'blow', 'blowjob', 'boang', 'bogan', 'bohunk', 'bollick', 'bollock', 'bomb', 'bombers', 'bombing', 'bombs', 'bomd', 'bondage'
        , 'boner', 'bong', 'boob', 'boobies', 'boobs', 'booby', 'boody', 'boom', 'boong', 'boonga', 'boonie', 'booty', 'bootycall', 'bountybar', 'bra', 'brea5t'
        , 'breast', 'breastjob', 'breastlover', 'breastman', 'brothel', 'bugger', 'buggered', 'buggery', 'bullcrap', 'bulldike', 'bulldyke', 'bullshit'
        , 'bumblefuck', 'bumfuck', 'bunga', 'bunghole', 'buried', 'burn', 'butchbabes', 'butchdike', 'butchdyke', 'butt', 'buttbang', 'butt-bang', 'buttface'
        , 'buttfuck', 'butt-fuck', 'buttfucker', 'butt-fucker', 'buttfuckers', 'butt-fuckers', 'butthead', 'buttman', 'buttmunch', 'buttmuncher', 'buttpirate'
        , 'buttplug', 'buttstain', 'byatch', 'cacker', 'cameljockey', 'cameltoe', 'canadian', 'cancer', 'carpetmuncher', 'carruth', 'catholic', 'catholics'
        , 'cemetery', 'chav', 'cherrypopper', 'chickslick', "children's", 'chin', 'chinaman', 'chinamen', 'chinese', 'chink', 'chinky', 'choad', 'chode'
        , 'christ', 'christian', 'church', 'cigarette', 'cigs', 'clamdigger', 'clamdiver', 'clit', 'clitoris', 'clogwog', 'cocaine', 'cock', 'cockblock'
        , 'cockblocker', 'cockcowboy', 'cockfight', 'cockhead', 'cockknob', 'cocklicker', 'cocklover', 'cocknob', 'cockqueen', 'cockrider', 'cocksman'
        , 'cocksmith', 'cocksmoker', 'cocksucer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocktail', 'cocktease', 'cocky', 'cohee'
        , 'coitus', 'color', 'colored', 'coloured', 'commie', 'communist', 'condom', 'conservative', 'conspiracy', 'coolie', 'cooly', 'coon', 'coondog'
        , 'copulate', 'cornhole', 'corruption', 'cra5h', 'crabs', 'crack', 'crackpipe', 'crackwhore', 'crack-whore', 'crap', 'crapola', 'crapper'
        , 'crappy', 'crash', 'creamy', 'crime', 'crimes', 'criminal', 'criminals', 'crotch', 'crotchjockey', 'crotchmonkey', 'crotchrot', 'cum'
        , 'cumbubble', 'cumfest', 'cumjockey', 'cumm', 'cummer', 'cumming', 'cumquat', 'cumqueen', 'cumshot', 'cunilingus', 'cunillingus', 'cunn'
        , 'cunnilingus', 'cunntt', 'cunt', 'cunteyed', 'cuntfuck', 'cuntfucker', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cuntsucker', 'cybersex'
        , 'cyberslimer', 'dago', 'dahmer', 'dammit', 'damn', 'damnation', 'damnit', 'darkie', 'darky', 'datnigga', 'dead', 'deapthroat', 'death'
        , 'deepthroat', 'defecate', 'dego', 'demon', 'deposit', 'desire', 'destroy', 'deth', 'devil', 'devilworshipper', 'dick', 'dickbrain'
        , 'dickforbrains', 'dickhead', 'dickless', 'dicklick', 'dicklicker', 'dickman', 'dickwad', 'dickweed', 'diddle', 'die', 'died', 'dies', 'dike'
        , 'dildo', 'dingleberry', 'dink', 'dipshit', 'dipstick', 'dirty', 'disease', 'diseases', 'disturbed', 'dive', 'dix', 'dixiedike'
        , 'dixiedyke', 'doggiestyle', 'doggystyle', 'dong', 'doodoo', 'doo-doo', 'doom', 'dope', 'dragqueen', 'dragqween', 'dripdick', 'drug'
        , 'drunk', 'drunken', 'dumb', 'dumbass', 'dumbbitch', 'dumbfuck', 'dyefly', 'dyke', 'easyslut', 'eatballs', 'eatme', 'eatpussy'
        , 'ecstacy', 'ejaculate', 'ejaculated', 'ejaculating', 'ejaculation', 'enema', 'enemy', 'erect', 'erection', 'ero', 'escort', 'ethiopian'
        , 'ethnic', 'european', 'evl', 'excrement', 'execute', 'executed', 'execution', 'executioner', 'explosion', 'facefucker', 'faeces'
        , 'fag', 'fagging', 'faggot', 'fagot', 'failed', 'failure', 'fairies', 'fairy', 'faith', 'fannyfucker', 'fart', 'farted', 'farting', 'farty'
        , 'fastfuck', 'fat', 'fatah', 'fatass', 'fatfuck', 'fatfucker', 'fatso', 'fckcum', 'fear', 'feces', 'felatio', 'felch', 'felcher', 'felching'
        , 'fellatio', 'feltch', 'feltcher', 'feltching', 'fetish', 'fight', 'filipina', 'filipino', 'fingerfood', 'fingerfuck', 'fingerfucked'
        , 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fire', 'firing', 'fister', 'fistfuck', 'fistfucked', 'fistfucker'
        , 'fistfucking', 'fisting', 'flange', 'flasher', 'flatulence', 'floo', 'flydie', 'flydye', 'fok', 'fondle', 'footaction'
        , 'footfuck', 'footfucker', 'footlicker', 'footstar', 'fore', 'foreskin', 'forni', 'fornicate', 'foursome', 'fourtwenty'
        , 'fraud', 'freakfuck', 'freakyfucker', 'freefuck', 'fu', 'fubar', 'fuc', 'fucck', 'fuck', 'fucka', 'fuckable', 'fuckbag'
        , 'fuckbuddy', 'fucked', 'fuckedup', 'fucker', 'fuckers', 'fuckface', 'fuckfest', 'fuckfreak', 'fuckfriend', 'fuckhead'
        , 'fuckher', 'fuckin', 'fuckina', 'fucking', 'fuckingbitch', 'fuckinnuts', 'fuckinright', 'fuckit', 'fuckknob', 'fuckme'
        , 'fuckmehard', 'fuckmonkey', 'fuckoff', 'fuckpig', 'fucks', 'fucktard', 'fuckwhore', 'fuckyou', 'fudgepacker', 'fugly'
        , 'fuk', 'fuks', 'funeral', 'funfuck', 'fungus', 'fuuck', 'gangbang', 'gangbanged', 'gangbanger', 'gangsta', 'gatorbait'
        , 'gay', 'gaymuthafuckinwhore', 'gaysex', 'geez', 'geezer', 'geni', 'genital', 'german', 'getiton', 'gin', 'ginzo', 'gipp'
        , 'girls', 'givehead', 'glazeddonut', 'gob', 'god', 'godammit', 'goddamit', 'goddammit', 'goddamn', 'goddamned', 'goddamnes', 'goddamnit'
        , 'goddamnmuthafucker', 'goldenshower', 'gonorrehea', 'gonzagas', 'gook', 'gotohell', 'goy', 'goyim', 'greaseball', 'gringo'
        , 'groe', 'gross', 'grostulation', 'gubba', 'gummer', 'gun', 'gyp', 'gypo', 'gypp', 'gyppie', 'gyppo', 'gyppy', 'hamas', 'handjob', 'hapa', 'harder', 'hardon', 'harem', 'headfuck', 'headlights', 'hebe', 'heeb', 'hell', 'henhouse', 'heroin', 'herpes', 'heterosexual', 'hijack', 'hijacker', 'hijacking'
        , 'hillbillies', 'hindoo', 'hiscock', 'hitler', 'hitlerism', 'hitlerist', 'hiv', 'ho', 'hobo', 'hodgie', 'hoes', 'hole', 'holestuffer', 'homicide', 'homo', 'homobangers', 'homosexual', 'honger', 'honk', 'honkers', 'honkey', 'honky', 'hook', 'hooker', 'hookers', 'hooters', 'hore'
        , 'hork', 'horn', 'horney', 'horniest', 'horny', 'horseshit', 'hosejob', 'hoser', 'hostage', 'hotdamn', 'hotpussy', 'hottotrot', 'hummer', 'husky', 'hussy', 'hustler', 'hymen', 'hymie', 'iblowu', 'idiot', 'ikey', 'illegal', 'incest', 'insest', 'intercourse', 'interracial', 'intheass', 'inthebuff', 'israel', 'israeli', "israel's", 'italiano', 'itch', 'jackass', 'jackoff', 'jackshit', 'jacktheripper', 'jade', 'jap', 'japanese', 'japcrap', 'jebus', 'jeez', 'jerkoff', 'jesus', 'jesuschrist', 'jew', 'jewish', 'jiga', 'jigaboo', 'jigg', 'jigga', 'jiggabo', 'jigger', 'jiggy', 'jihad', 'jijjiboo', 'jimfish', 'jism', 'jiz', 'jizim', 'jizjuice', 'jizm', 'jizz', 'jizzim', 'jizzum', 'joint', 'juggalo', 'jugs', 'junglebunny', 'kaffer', 'kaffir', 'kaffre', 'kafir', 'kanake', 'kid', 'kigger', 'kike', 'kill', 'killed', 'killer', 'killing', 'kills', 'kink', 'kinky', 'kissass', 'kkk', 'knife', 'knockers', 'kock', 'kondum', 'koon', 'kotex', 'krap', 'krappy', 'kraut', 'kum', 'kumbubble', 'kumbullbe', 'kummer', 'kumming', 'kumquat', 'kums', 'kunilingus', 'kunnilingus', 'kunt', 'ky', 'kyke', 'lactate', 'laid', 'lapdance', 'latin', 'lesbain', 'lesbayn', 'lesbian', 'lesbin', 'lesbo', 'lez', 'lezbe', 'lezbefriends', 'lezbo', 'lezz', 'lezzo', 'liberal', 'libido', 'licker', 'lickme', 'lies', 'limey', 'limpdick', 'limy', 'lingerie', 'liquor', 'livesex', 'loadedgun', 'lolita', 'looser', 'loser', 'lotion', 'lovebone', 'lovegoo', 'lovegun', 'lovejuice', 'lovemuscle', 'lovepistol', 'loverocket', 'lowlife', 'lsd', 'lubejob', 'lucifer', 'luckycammeltoe', 'lugan', 'lynch', 'macaca', 'mad', 'mafia', 'magicwand', 'mams', 'manhater', 'manpaste', 'marijuana', 'mastabate', 'mastabater', 'masterbate', 'masterblaster', 'mastrabator', 'masturbate', 'masturbating', 'mattressprincess', 'meatbeatter', 'meatrack', 'meth', 'mexican', 'mgger', 'mggor', 'mickeyfinn', 'mideast', 'milf', 'minority', 'mockey', 'mockie', 'mocky', 'mofo', 'moky', 'moles', 'molest', 'molestation', 'molester', 'molestor', 'moneyshot', 'mooncricket', 'mormon', 'moron', 'moslem', 'mosshead', 'mothafuck', 'mothafucka', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckin', 'mothafucking', 'mothafuckings', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherlovebone', 'muff', 'muffdive', 'muffdiver', 'muffindiver', 'mufflikcer', 'mulatto', 'muncher', 'munt', 'murder', 'murderer', 'muslim', 'naked', 'narcotic', 'nasty', 'nastybitch', 'nastyho', 'nastyslut', 'nastywhore', 'nazi', 'necro', 'negro', 'negroes', 'negroid', "negro's", 'nig', 'niger', 'nigerian', 'nigerians', 'nigg', 'nigga', 'niggah', 'niggaracci', 'niggard', 'niggarded', 'niggarding', 'niggardliness', "niggardliness's", 'niggardly', 'niggards', "niggard's", 'niggaz', 'nigger', 'niggerhead', 'niggerhole', 'niggers', "nigger's", 'niggle', 'niggled', 'niggles', 'niggling', 'nigglings', 'niggor', 'niggur', 'niglet', 'nignog', 'nigr', 'nigra', 'nigre', 'nip', 'nipple', 'nipplering', 'nittit', 'nlgger', 'nlggor', 'nofuckingway', 'nook', 'nookey', 'nookie', 'noonan', 'nooner', 'nude', 'nudger', 'nuke', 'nutfucker', 'nymph', 'ontherag', 'oral', 'orga', 'orgasim', 'orgasm', 'orgies', 'orgy', 'osama', 'paki', 'palesimian', 'palestinian', 'pansies', 'pansy', 'panti', 'panties', 'payo', 'pearlnecklace', 'peck', 'pecker', 'peckerwood', 'pee', 'peehole', 'pee-pee', 'peepshow', 'peepshpw', 'pendy', 'penetration', 'peni5', 'penile', 'penis', 'penises', 'penthouse', 'period', 'perv', 'phonesex', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phungky', 'phuq', 'pi55', 'picaninny', 'piccaninny', 'pickaninny', 'piker', 'pikey', 'piky', 'pimp', 'pimped', 'pimper', 'pimpjuic', 'pimpjuice', 'pimpsimp', 'pindick', 'piss', 'pissed', 'pisser', 'pisses', 'pisshead', 'pissin', 'pissing', 'pissoff', 'pistol', 'pixie', 'pixy', 'playboy', 'playgirl', 'pocha', 'pocho', 'pocketpool', 'pohm', 'polack', 'pom', 'pommie', 'pommy', 'poo', 'poon', 'poontang', 'poop', 'pooper', 'pooperscooper', 'pooping', 'poorwhitetrash', 'popimp', 'porchmonkey', 'porn', 'pornflick', 'pornking', 'porno', 'pornography', 'pornprincess', 'pot', 'poverty', 'premature', 'pric', 'prick', 'prickhead', 'primetime', 'propaganda', 'pros', 'prostitute', 'protestant', 'pu55i', 'pu55y', 'pube', 'pubic', 'pubiclice', 'pud', 'pudboy', 'pudd', 'puddboy', 'puke', 'puntang', 'purinapricness', 'puss', 'pussie', 'pussies', 'pussy', 'pussycat', 'pussyeater', 'pussyfucker', 'pussylicker', 'pussylips', 'pussylover', 'pussypounder', 'pusy', 'quashie', 'queef', 'queer', 'quickie', 'quim', 'ra8s', 'rabbi', 'racial', 'racist', 'radical', 'radicals', 'raghead', 'randy', 'rape', 'raped', 'raper', 'rapist', 'rearend', 'rearentry', 'rectum', 'redlight', 'redneck', 'reefer', 'reestie', 'refugee', 'reject', 'remains', 'rentafuck', 'republican', 'rere', 'retard', 'retarded', 'ribbed', 'rigger', 'rimjob', 'rimming', 'roach', 'robber', 'roundeye', 'rump', 'russki', 'russkie', 'sadis', 'sadom', 'samckdaddy', 'sandm', 'sandnigger', 'satan', 'scag', 'scallywag', 'scat', 'schlong', 'screw', 'screwyou', 'scrotum', 'scum', 'semen', 'seppo', 'servant', 'sex', 'sexed', 'sexfarm', 'sexhound', 'sexhouse', 'sexing', 'sexkitten', 'sexpot', 'sexslave', 'sextogo', 'sextoy', 'sextoys', 'sexual', 'sexually', 'sexwhore', 'sexy', 'sexymoma', 'sexy-slim', 'shag', 'shaggin', 'shagging', 'shat', 'shav', 'shawtypimp', 'sheeney', 'shhit', 'shinola', 'shit', 'shitcan', 'shitdick', 'shite', 'shiteater', 'shited', 'shitface', 'shitfaced', 'shitfit', 'shitforbrains', 'shitfuck', 'shitfucker', 'shitfull', 'shithapens', 'shithappens', 'shithead', 'shithouse', 'shiting', 'shitlist', 'shitola', 'shitoutofluck', 'shits', 'shitstain', 'shitted', 'shitter', 'shitting', 'shitty', 'shortfuck', 'sissy', 'sixtyniner', 'skank', 'skankbitch', 'skankfuck', 'skankwhore', 'skanky', 'skankybitch', 'skankywhore', 'skinflute', 'skum', 'skumbag', 'slant', 'slanteye', 'slapper', 'slav', 'slave', 'slavedriver', 'sleezebag', 'sleezeball', 'slideitin', 'slime', 'slimeball', 'slimebucket', 'slopehead', 'slopey', 'slopy', 'slut', 'sluts', 'slutt', 'slutting', 'slutty', 'slutwear', 'slutwhore', 'smack', 'smackthemonkey', 'smut', 'snatch', 'snatchpatch', 'snigger', 'sniggered', 'sniggering', 'sniggers', "snigger's", 'sniper', 'snot', 'snowback', 'snownigger', 'sob', 'sodom', 'sodomise', 'sodomite', 'sodomize', 'sodomy', 'sonofabitch', 'sonofbitch', 'sooty', 'soviet', 'spaghettibender', 'spaghettinigger', 'spank', 'spankthemonkey', 'sperm', 'spermacide', 'spermbag', 'spermhearder', 'spermherder', 'spic', 'spick', 'spig', 'spigotty', 'spik', 'spit', 'spitter', 'splittail', 'spooge', 'spreadeagle', 'spunk', 'spunky', 'squaw', 'stagg', 'stiffy', 'strapon', 'stringer', 'stripclub', 'stroke', 'stroking', 'stupid', 'stupidfuck', 'stupidfucker', 'suck', 'suckdick', 'sucker', 'suckme', 'suckmyass', 'suckmydick', 'suckmytit', 'suckoff', 'suicide', 'swallow', 'swallower', 'swalow', 'swastika', 'sweetness', 'syphilis', 'taboo', 'taff', 'tampon', 'tang', 'tantra', 'tarbaby', 'tard', 'teat', 'terror', 'terrorist', 'teste', 'testicle', 'testicles', 'thicklips', 'thirdeye', 'thirdleg', 'threesome', 'threeway', 'timbernigger', 'tinkle', 'tit', 'titbitnipply', 'titfuck', 'titfucker', 'titfuckin', 'titjob', 'titlicker', 'titlover', 'tits', 'tittie', 'titties', 'titty', 'tnt', 'tongethruster', 'tongue', 'tonguethrust', 'tonguetramp', 'tortur', 'torture', 'tosser', 'towelhead', 'trailertrash', 'tramp', 'trannie', 'tranny', 'transexual', 'transsexual', 'transvestite', 'triplex', 'trisexual', 'trojan', 'trots'
        , 'tuckahoe', 'tunneloflove', 'turd', 'turnon', 'twat', 'twink', 'twinkie', 'twobitwhore', 'uck', 'uk', 'unfuckable'
        , 'upskirt', 'uptheass', 'upthebutt', 'urinary', 'urinate', 'urine', 'usama', 'uterus', 'vagina', 'vaginal', 'vatican'
        , 'vibr', 'vibrater', 'vibrator', 'vietcong', 'violence', 'virgin', 'virginbreaker', 'vomit', 'vulva', 'wab', 'wank'
        , 'wanker', 'wanking', 'waysted', 'weapon', 'weenie', 'weewee', 'welcher', 'welfare', 'wetb', 'wetback'
        , 'wetspot', 'whacker', 'whash', 'whigger', 'whiskey', 'whiskeydick', 'whiskydick', 'whit', 'whitenigger'
        , 'whites', 'whitetrash', 'whitey', 'whiz', 'whop', 'whore', 'whorefucker', 'whorehouse', 'wigger', 'willie'
        , 'williewanker', 'willy', 'wn', 'wog', 'wop', 'wtf', 'wuss', 'wuzzie', 'xtc', 'xxx', 'yankee', 'yellowman'
        , 'zigabo', 'zipperhead', 'douche', 'lmfao', 'lmao']
        for i in eng:
            if i in text:
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

        text = re.sub('카카오톡', '', newtext)
        text = re.sub('카톡', '', text)
        text = re.sub('카페', '', text)
        text = re.sub('하다가', '', text)
        text = re.sub('먹다가', '', text)
        text = re.sub('카와이', '', text)
        text = re.sub('카츠', '', text)
        text = re.sub('카레', '', text)
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
        text = re.sub('오ㅗㅗㅗㅗ', '', text)
        text = re.sub('오ㅗㅗㅗ', '', text)
        text = re.sub('호ㅗㅗㅗㅗ', '', text)
        text = re.sub('호ㅗㅗㅗ', '', text)
        text = re.sub('로ㅗㅗㅗㅗ', '', text)
        text = re.sub('로ㅗㅗㅗ', '', text)
        text = re.sub('옹ㅗㅗㅗㅗ', '', text)
        text = re.sub('옹ㅗㅗㅗ', '', text)
        text = re.sub('롤ㅗㅗㅗㅗ', '', text)
        text = re.sub('롤ㅗㅗㅗ', '', text)
        text = re.sub('요ㅗㅗㅗ', '', text)
        text = re.sub('우ㅗㅗㅗ', '', text)
        text = re.sub('하ㅗㅗㅗ', '', text)
        text = re.sub('ㅇㅗ', '', text)
        text = re.sub('ㅗㅜ', '', text)
        text = re.sub('rㅗ', '', text)
        text = re.sub('ㅗr', '', text)
        text = re.sub('sㅗ', '', text)
        text = re.sub('ㅗs', '', text)
        text = re.sub('eㅗ', '', text)
        text = re.sub('ㅗe', '', text)
        text = re.sub('fㅗ', '', text)
        text = re.sub('ㅗf', '', text)
        text = re.sub('aㅗ', '', text)
        text = re.sub('ㅗa', '', text)
        text = re.sub('qㅗ', '', text)
        text = re.sub('ㅗq', '', text)
        text = re.sub('ㅗw', '', text)
        text = re.sub('wㅗ', '', text)
        text = re.sub('ㅗd', '', text)
        text = re.sub('dㅗ', '', text)
        text = re.sub('ㅗg', '', text)
        text = re.sub('gㅗ', '', text)
        fuckyou = ["ㅗ", "┻", "┴", "┹", "_ㅣ_", "_l_", "_/_", "⊥", "_ |\_", "_|\_", "_ㅣ\_", "_I_"]
        for i in fuckyou:
            if i in text:
                ae = 1


        fuck = ["tq","qt"]
        for i in fuck:
            if i == text:
                ae = 1
        text = re.sub('118', '', text)
        text = re.sub('218', '', text)
        text = re.sub('318', '', text)
        text = re.sub('418', '', text)
        text = re.sub('518', '', text)
        text = re.sub('618', '', text)
        text = re.sub('718', '', text)
        text = re.sub('818', '', text)
        text = re.sub('918', '', text)
        text = re.sub('018', '', text)
        fuck = ["씨8","18아","18놈","18련""tㅂ","t발","ㅅㅍ","ㅆㅍ","18뇬",
                "sibal","sival","sibar","sibak","sipal","siqk","tlbal","tlval","tlbar","tlbak","tlpal","tlqk"
                "시bal","시val","시bar","시bak","시pal","시qk","시bal","시val","시bar","시bak","시pal","시qk"
                "si바","si발","si불","si빨","si팔","tl바","tl발","tl불","tl빨""tl팔",
                "siba","tlba","siva","tlva","tlqkf","10발련","10발넘","10발놈","10발년","tlqkd","si8"]
        for i in fuck:
            if i in text:
                ae = 1
        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('人', 'ㅅ', text)
        text = re.sub('丨', 'ㅣ', text)
        text = re.sub('甘', 'ㅂ', text)
        text = re.sub('卜', 'ㅏ', text)
        text = re.sub('l', 'ㅣ', text)
        text = re.sub('r', 'ㅏ', text)
        text = re.sub('ᐲ', 'ㅅ', text)
        text = re.sub('ᗨ', 'ㅂ', text)
        text = re.sub('시ㅣ', '시', text)
        text = re.sub('씨ㅣ', '씨', text)
        text = re.sub('ㅅ1', '시', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        fuck = ["시ㅂ", "시ㅏㄹ", "씨ㅂ", "씨ㅏㄹ", "ㅣ발", "ㅆ발", "ㅅ발", "ㅅㅂ", "ㅆㅂ", "ㅆ바", "ㅅ바",
                "시ㅂㅏ", "ㅅㅂㅏ", "시ㅏㄹ", "씨ㅏㄹ", "ㅅ불", "ㅆ불","ㅅ쁠", "ㅆ뿔","ㅆㅣ발","ㅅㅟ발","ㅅㅣㅂㅏ",
                "ㅣ바알","씨바알","샤빨","샤발","스벌","쓰벌","신발련","신발년","신발놈","ㅅ벌","시불","시부렝"
                ,"씨부렝","시부랭","씨부랭","^^ㅣ벌","시부랭"]
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
        text = re.sub('이', '', text)
        text = re.sub('일', '', text)
        text = re.sub('벌어', '', text)
        text = re.sub('시바이누', '', text)
        text = re.sub('시바스리갈', '', text)
        text = re.sub('시바산', '', text)
        text = re.sub('시바신', '', text)
        text = re.sub('오리발', '', text)
        text = re.sub('발끝', '', text)
        text = re.sub('다시바', '', text)
        text = re.sub('비슈누시바', '', text)
        text = re.sub('시바핫카이', '', text)
        text = re.sub('시바타이쥬', '', text)
        text = re.sub('데스티니시바', '', text)
        text = re.sub('시바루', '', text)
        text = re.sub('시바료타로', '', text)
        text = re.sub('시바라스시', '', text)
        text = re.sub('젤리', '', text)
        text = re.sub('발사', '', text)
        text = re.sub('크시', '', text)
        text = re.sub('크시야', '', text)
        text = re.sub('어찌', '', text)
        text = re.sub('발로란트', '', text)
        fuck = ["시발", "씨발", "시봘", "씨봘", "씨바", "시바", "샤발", "씌발", "씹발", "시벌", "시팔", "싯팔",
                "씨빨", "씨랼", "씨파", "띠발", "띡발", "띸발","싸발", "십발", "슈발","야발", "씨불", "씨랄",
                "쉬발", "쓰발", "쓔발", "쌰발", "쉬발", "쒸발", "씨팔", "씨밝", "씨밯", "쑤발", "치발", "샤발",
                "발씨", "리발", "씨볼","찌발", "씨비바라랄", "시바랄", "씨바라","쒸팔","쉬팔","씨밮","쒸밮","시밮","씨삐라","ㅆ삐라","씨벌","슈벌"]
        for i in fuck:
            if i in text:
                ae = 1

        text = re.sub('련', '놈', newtext)
        text = re.sub('뇬', '놈', text)
        text = re.sub('놈', '놈', text)
        text = re.sub('넘', '놈', text)
        fuck = ["18것", "18놈", "18럼", "18롬", "18새끼", "18세끼", "18세리", "18섹", "18쉑", "10쉑"]
        for i in fuck:
            if i in text:
                ae = 1

        bullshit1 = ["wlfkf","g랄", "g럴", "g롤","g뢀"]
        for i in bullshit1:
            if i in text:
                ae = 1
        text = re.sub("g랄", "지랄", newtext)
        text = re.sub("[^ㄱ-힣]", "", text)
        text = re.sub("있지", "", text)
        text = re.sub("없지", "", text)
        text = re.sub("하지", "", text)
        text = re.sub("근", "ㄹ", text)
        text = re.sub("ㄹㅇ", "", text)
        bullshit1 = ["ㅈㄹ", "지ㄹ", "ㅈ랄", "ㅈ라"]
        for i in bullshit1:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub('지랄탄', '', text)
        text = re.sub('지랄버릇', '', text)
        text = re.sub('이', '', text)
        bullshit2 = ["지랄", "찌랄", "지럴", "지롤", "랄지","쥐랄","쮜랄","지뢀"]
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
        text = re.sub('우', '', text)
        text = re.sub('웅', '', text)
        asshole = ["ㅄ", "ㅂㅅ", "병ㅅ", "ㅂ신", "ㅕㅇ신","ㅂㅇ신","뷰신"]
        for i in asshole:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", text)
        text = re.sub('영', '', text)
        text = re.sub('엉', '', text)
        asshole = ["병신", "병딱", "벼신","붱신","뼝신","뿽신","삥신","병시니"]
        for i in asshole:
            if i in text:
                ae = 1

        text = re.sub(r'[0-9]+', '', newtext)
        text = re.sub("[ㅂㅁㅋㅈㄴㅌㄷㅇㅊㄱㄹㅍㅅㅎㅃㅉㄸㄲㅆㅠㅛㅗㅜㅕㅓㅡㅑㅏㅐㅣㅔㄺㄼㄽㅃㅉㄸㄲㅆㅀㄿㄾㅘㅚㅟㅝㅞㅢㅙ]", "", text)
        text = re.sub("[\--z]", "", text)
        text = re.sub('전염병', '', text)
        motherfucker = ["염병", "엠병", "옘병", "염병", "얨병","옘뼝"]
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
        text = re.sub('꺼져도', '', text)
        if "꺼져" in text:
            ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        shit = ["엿같", "엿가튼", "엿먹어"]
        for i in shit:
            if i in text:
                ae = 1

        sonofbitch = ["rotorl","rotprl","sib새"]
        for i in sonofbitch:
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
        text = re.sub('고양이새끼', '', text)
        text = re.sub('키보드', '', text)
        sonofbitch = ["새끼", "쉐리", "쌔끼", "썌끼", "쎼끼", "쌬끼", "샠끼","세끼","샊","쌖","섺","쎆","십새","새키","씹색"]
        for i in sonofbitch:
            if i in text:
                ae = 1

        dick = ["w같은"]
        for i in dick:
            if i in newtext:
                ae = 1
        text = re.sub("[^ㄱ-힣]", "", newtext)
        text = re.sub('줫습니다', '', text)
        dick = ["ㅈ같", "ㅈ망", "ㅈ까", "ㅈ경"]
        for i in dick:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", text)
        dick = ["좆", "촟", "조까", "좈", "쫒", "졷", "좃","좋같","좃같","좃물","좃밥","줫","좋밥","좋물","좇"]
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
        whatthefuck = ["뻑유", "뻐킹", "뻐큐","빡큐","뿩큐","뻑큐","빡유"]
        for i in whatthefuck:
            if i in text:
                ae = 1

        text = re.sub("[^가-힣]", "", newtext)
        shutup = ["닥쳐", "닭쳐","닥치라"]
        for i in shutup:
            if i in text:
                ae = 1

        text = re.sub(r'[0-9]+', '', newtext)
        sonofagun = ["dog새"]
        for i in sonofagun:
            if i in text:
                ae = 1
        text = re.sub("[^ㄱ-힣]", "", newtext)
        sonofagun = ["개ㅐ색"]
        for i in sonofagun:
            if i in text:
                ae = 1
        text = re.sub("[^가-힣]", "", newtext)
        sonofagun = ["개같", "개가튼", "개쉑", "개스키", "개세끼", "개색히", "개가뇬", "개새기", "개쌔기", "개쌔끼", "쌖", "쎆", "새긔", "개소리", "개년", "개소리",
                    "개드립","개돼지","개씹창","개간나","개스끼","개섹기","개자식","개때꺄","개때끼","개발남아","개샛끼","개가든","개가뜬","개가턴","개가툰","개가튼",
                    "개갇은","개갈보","개걸레","개너마","개너므","개넌","개넘","개녀나","개년","개노마","개노무새끼","개논","개놈","개뇨나","개뇬","개뇸","개뇽","개눔",
                    "개느마","개늠","개때꺄","개때끼","개떼끼","개랙기","개련","개발남아","개발뇬","개색","개색끼","개샊","개샛끼","개샛키","개샛킹","개샛히","개샜끼",
                    "개생키","개샠","개샤끼","개샤킥","개샥","개샹늠","개세끼","개세리","개세키","개섹히","개섺","개셃","개셋키","개셐","개셰리","개솩","개쇄끼","개쇅",
                    "개쇅끼","개쇅키","개쇗","개쇠리","개쉐끼","개쉐리","개쉐키","개쉑","개쉑갸","개쉑기","개쉑꺄","개쉑끼","개쉑캬","개쉑키","개쉑히","개쉢","개쉨",
                    "개쉬","개쉬끼","개쉬리","개쉽","개스끼","개스키","개습","개습세","개습쌔","개싀기","개싀끼","개싀밸","개싀킈","개싀키","개싏","개싑창","개싘",
                    "개시끼","개시퀴","개시키","개식기","개식끼","개식히","개십새","개십팔","개싯기","개싯끼","개싯키","개싴","개쌍넘","개쌍년","개쌍놈","개쌍눔",
                    "개쌍늠","개쌍연","개쌍영","개쌔꺄","개쌔끼","개쌕","개쌕끼","개쌰깨","개썅","개쎄","개쎅","개쎼키","개쐐리","개쒜","개쒝","개쒯","개쒸","개쒸빨놈",
                    "개쒹기","개쓉","개쒹기","개쓉","개씀","개씁","개씌끼","개씨끼","개씨팕","개씨팔","개잡것","개잡년","개잡놈","개잡뇬","개젓","개젖","개젗","개졋",
                    "개졎","개조또","개조옷","개족","개좃","개좆","개좇","개지랄","개지럴","개창년","개허러","개허벌년","개호러","개호로","개후랄","개후레","개후로",
                    "개후장","걔섀끼","걔잡넘","걔잡년","걔잡뇬","게가튼","게같은","게너마","게넘","게년","게노마","게놈","게뇨나","게뇬","게뇸","게뇽","게눔","게늠",
                    "게띠발넘","게부랄","게부알","게새끼","게새리","게새키","게색","게색기","게색끼","게샛키","게세꺄","게자지","게잡넘","게잡년","게잡뇬","게젓",
                    "게좆","계같은뇬","계뇬","계뇽"]
        for i in sonofagun:
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

        text = re.sub("[^ㄱ-힣]", "", newtext)
        damnit = ["ㅁㅊ", "ㅁ친", "ㅁ쳤","aㅣ친","me친"]
        for i in damnit:
            if i in text:
                be = 2
        text = re.sub("[^가-힣]", "", text)
        text = re.sub('이미친', '', text)
        text = re.sub('미친증', '', text)
        text = re.sub('거미', '', text)
        text = re.sub('친구', '', text)
        damnit = ["미친", "미쳤","무친놈"]
        for i in damnit:
            if i in text:
                be = 2

        text = re.sub("[^가-힣]", "", text)
        picking = ["꼽냐", "꼽니", "꼽나"]
        for i in picking:
            if i in text:
                be = 2

        text = re.sub("[^ㄱ-힣]", "", text)
        picking = ["ㅈㄴ","ㅈ나","존ㄴ","존맛"]
        for i in picking:
            if i in text:
                be = 2
        text = re.sub("[^가-힣]", "", text)
        text = re.sub("그만 졸라", "ㄹ", text)
        text = re.sub("졸라서", "", text)
        picking = ["존나","존내","쫀나","존네","졸라"]
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

        pussy = ["ⓑⓞⓩⓘ","bozi"]
        for i in pussy:
            if i in newtext:
                ce = 3
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
        text = re.sub('정보', '', text)
        text = re.sub('지팡이', '', text)
        text = re.sub('행보', '', text)
        text = re.sub('오', '', text)
        pussy = ["보지","버지물","버짓물","보짓","ⓑⓞⓩⓘ","bozi","개보즤","개보지"]
        for i in pussy:
            if i in text:
                ce = 3


        dicks = ["ja지"]
        for i in dicks:
            if i in newtext:
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
        text = re.sub('개발자', '', text)
        text = re.sub('관리자', '', text)
        text = re.sub('타자지', '', text)
        text = re.sub('혼자', '', text)
        text = re.sub('못자지', '', text)
        text = re.sub('자지원', '', text)
        text = re.sub('사용자', '', text)
        text = re.sub('자지않', '', text)
        text = re.sub('자지마', '', text)
        text = re.sub('자지말', '', text)
        text = re.sub('지원자', '', text)
        text = re.sub('안자지', '', text)
        text = re.sub('부자지', '', text)
        text = re.sub('아', '', text)
        dicks = ["자지","자짓"]
        for i in dicks:
            if i in text:
                ce = 3


        sex = ["s스", "x스", "se스", "se스", "s스","ㅅㅅ","s하고e싶다x"]
        for i in sex:
            if i in newtext:
                ce = 3
        text = re.sub(r'\^', 'ㅅ', newtext)
        text = re.sub('sex', '섹스', text)
        text = re.sub('엑', '', text)
        text = re.sub("[^ㄱ-힣]", "", text)
        sex = ["ㅅㅔㄱ스", "섹ㅅ", "ㅅ스", "세ㄱㅅ", "ㅅㅔㄱㅅ"]
        for i in sex:
            if i in text:
                ce = 3
        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub("야스오", "", text)
        text = re.sub("크시야", "", text)
        text = re.sub("카구야", "", text)
        text = re.sub("스파이", "", text)
        sex = ["섹스", "섻스", "쉑스", "섿스", "섹그", "야스", "색스", "셱스", "섁스", "세엑스", "썩스","섹수","섹파","섹하자","쉐스","쉑스","쉐엑스"]
        for i in sex:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        fireegg = ["불알", "부랄", "뽕알", "뿅알", "뿌랄", "뿔알","개부달","개부랄","개부러럴","개부럴","개부뢀","개부알","개불알"]
        for i in fireegg:
            if i in text:
                ce = 3

        text = re.sub("[^ㄱ-힣]", "", newtext)
        onahole = ["오나홍", "오나홀", "ㅇㄴ홀","텐가","바이브레이터","오ㄴ홀","ㅇ나홀"]
        for i in onahole:
            if i in text:
                ce = 3
        
        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["씹하다"]
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
        onahole = ["모유물","로리물","근친상간","룸섹스","원조교재","속박플레이","야플","야외플레이"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["딸딸이","질싸","안에사정","자위남","자위녀","폰섹","포르노","폰세엑","폰쉑","폰쎅","질내사정","그룹섹","남창","男色","누워라이년아","누웠냐씨방새",]
        for i in onahole:
            if i in text:
                ce = 3

        onahole = ["g스팟","지스팟"]
        for i in onahole:
            if i in newtext:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["크리토리스","클리토리스","페니스","애널"]
        for i in onahole:
            if i in text:
                ce = 3

        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["젖까","젖가튼","젖나","젖만"]
        for i in onahole:
            if i in text:
                ce = 3

        onahole = ["ja위"]
        for i in onahole:
            if i in text:
                ce = 3
        text = re.sub("[^가-힣]", "", newtext)
        onahole = ["자위","고자새끼","고츄","꺼추","께세","꼬추"]
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

        text = re.sub('뇬', '련', newtext)
        text = re.sub('놈', '련', text)
        text = re.sub('넘', '련', text)
        belittling = ["10련"]
        for i in belittling:
            if i in text:
                de = 4
        text = re.sub('련', '년', newtext)
        text = re.sub('뇬', '년', text)
        text = re.sub('놈', '년', text)
        text = re.sub('넘', '년', text)
        text = re.sub('러운지', '', text)
        text = re.sub('려운지', '', text)
        text = re.sub('무서운지', '', text)
        text = re.sub("[^가-힣]", "", text)
        belittling = ["따까리", "장애년", "찐따년", "싸가지", "창년", "썅년", "버러지", "고아년", "고아년", "개간년", "종간나", "도구년", "걸래년", "썅년", "씹년",
                    "창녀", "머저리", "씹쓰래기", "씹쓰레기", "씹장생", "씹자식", "운지", "급식충", "틀딱충", "조센징", "매국노", "똥꼬충", "진지충", "듣보잡",
                    "한남충","정신병자","중생아","돌팔이","김치녀","폰팔이","틀딱년","같은년","개돼중","쓰글년","썩을년","썩글년","씹할","거지새끼","거지쉐뀌",
                    "거지쉑이","거지쎄끼","거지쒜리","걸래가튼","걸래넘","걸래년","걸래놈","걸레가튼","걸레년","그지새끼","그지새키","그지색","기집년","까진년",
                    "깔보","난잡년"]
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

        your = ["ㄴ1ㄱ", "ㄴ1ㅁ", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠","ㅇH미","ㄴ1에미"]
        for i in your:
            if i in newtext:
                fe = 6
        text = re.sub("[^ㄱ-힣]", "", newtext)
        your = ["ㄴㄱㅁ", "ㄴ금마", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠","ㄴ미"]
        for i in your:
            if i in text:
                fe = 6
        text = re.sub("[^가-힣]", "", newtext)
        your = ["느금마", "느그엄마", "늑엄마", "늑금마", "느그애미", "넉엄마", "느그부모", "느그애비", "느금빠", "느그메", "느그빠","니미씨","니미씹",
        "느그마","니엄마","엄창","엠창","니미럴","누굼마","느금","내미랄","내미럴"]
        for i in your:
            if i in text:
                fe = 6

        text = re.sub("[^가-힣]", "", newtext)
        text = re.sub("도", "", text)
        motherfuck = ["니애미", "노애미", "노앰", "앰뒤련",
                    "아버지도없는게", "애미도없는게", "애비도없는게", "어머니도없는게", "니애비", "노애비","애미없","애비없","애미뒤","애비뒤","니아빠","너에미"]
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
        eng = ['abbo', 'abo'
        , 'abortion', 'abuse', 'addict', 'addicts', 'adult', 'africa', 'african', 'alla', 'allah', 'alligatorbait', 'amateur', 'american'
        , 'anal', 'analannie', 'analsex', 'angie', 'angry', 'anus', 'arab', 'arabs', 'areola', 'argie', 'aroused', 'arse', 'arsehole', 'asian'
        , 'ass', 'assassin', 'assassinate', 'assassination', 'assault', 'assbagger', 'assblaster', 'assclown', 'asscowboy', 'asses', 'assfuck'
        , 'assfucker', 'asshat', 'asshole', 'assholes', 'asshore', 'assjockey', 'asskiss', 'asskisser', 'assklown', 'asslick', 'asslicker', 'asslover'
        , 'assman', 'assmonkey', 'assmunch', 'assmuncher', 'asspacker', 'asspirate', 'asspuppies', 'assranger', 'asswhore', 'asswipe', 'athletesfoot'
        , 'attack', 'australian', 'backdoor', 'backdoorman', 'backseat', 'badfuck', 'balllicker', 'balls', 'ballsack', 'banging', 'baptist', 'barelylegal'
        , 'barf', 'barface', 'barfface', 'bast', 'bastard', 'bazongas', 'bazooms', 'beaner', 'beast', 'beastality', 'beastial', 'beastiality', 'beatoff'
        , 'beat-off', 'beatyourmeat', 'beaver', 'bestial', 'bestiality', 'bi', 'biatch', 'bicurious', 'bigass', 'bigbastard', 'bigbutt', 'bigger', 'bisexual'
        , 'bi-sexual', 'bitch', 'bitcher', 'bitches', 'bitchez', 'bitchin', 'bitching', 'bitchslap', 'bitchy', 'biteme', 'black', 'blackman', 'blackout'
        , 'blacks', 'blind', 'blow', 'blowjob', 'boang', 'bogan', 'bohunk', 'bollick', 'bollock', 'bomb', 'bombers', 'bombing', 'bombs', 'bomd', 'bondage'
        , 'boner', 'bong', 'boob', 'boobies', 'boobs', 'booby', 'boody', 'boom', 'boong', 'boonga', 'boonie', 'booty', 'bootycall', 'bountybar', 'bra', 'brea5t'
        , 'breast', 'breastjob', 'breastlover', 'breastman', 'brothel', 'bugger', 'buggered', 'buggery', 'bullcrap', 'bulldike', 'bulldyke', 'bullshit'
        , 'bumblefuck', 'bumfuck', 'bunga', 'bunghole', 'buried', 'burn', 'butchbabes', 'butchdike', 'butchdyke', 'butt', 'buttbang', 'butt-bang', 'buttface'
        , 'buttfuck', 'butt-fuck', 'buttfucker', 'butt-fucker', 'buttfuckers', 'butt-fuckers', 'butthead', 'buttman', 'buttmunch', 'buttmuncher', 'buttpirate'
        , 'buttplug', 'buttstain', 'byatch', 'cacker', 'cameljockey', 'cameltoe', 'canadian', 'cancer', 'carpetmuncher', 'carruth', 'catholic', 'catholics'
        , 'cemetery', 'chav', 'cherrypopper', 'chickslick', "children's", 'chin', 'chinaman', 'chinamen', 'chinese', 'chink', 'chinky', 'choad', 'chode'
        , 'christ', 'christian', 'church', 'cigarette', 'cigs', 'clamdigger', 'clamdiver', 'clit', 'clitoris', 'clogwog', 'cocaine', 'cock', 'cockblock'
        , 'cockblocker', 'cockcowboy', 'cockfight', 'cockhead', 'cockknob', 'cocklicker', 'cocklover', 'cocknob', 'cockqueen', 'cockrider', 'cocksman'
        , 'cocksmith', 'cocksmoker', 'cocksucer', 'cocksuck', 'cocksucked', 'cocksucker', 'cocksucking', 'cocktail', 'cocktease', 'cocky', 'cohee'
        , 'coitus', 'color', 'colored', 'coloured', 'commie', 'communist', 'condom', 'conservative', 'conspiracy', 'coolie', 'cooly', 'coon', 'coondog'
        , 'copulate', 'cornhole', 'corruption', 'cra5h', 'crabs', 'crack', 'crackpipe', 'crackwhore', 'crack-whore', 'crap', 'crapola', 'crapper'
        , 'crappy', 'crash', 'creamy', 'crime', 'crimes', 'criminal', 'criminals', 'crotch', 'crotchjockey', 'crotchmonkey', 'crotchrot', 'cum'
        , 'cumbubble', 'cumfest', 'cumjockey', 'cumm', 'cummer', 'cumming', 'cumquat', 'cumqueen', 'cumshot', 'cunilingus', 'cunillingus', 'cunn'
        , 'cunnilingus', 'cunntt', 'cunt', 'cunteyed', 'cuntfuck', 'cuntfucker', 'cuntlick', 'cuntlicker', 'cuntlicking', 'cuntsucker', 'cybersex'
        , 'cyberslimer', 'dago', 'dahmer', 'dammit', 'damn', 'damnation', 'damnit', 'darkie', 'darky', 'datnigga', 'dead', 'deapthroat', 'death'
        , 'deepthroat', 'defecate', 'dego', 'demon', 'deposit', 'desire', 'destroy', 'deth', 'devil', 'devilworshipper', 'dick', 'dickbrain'
        , 'dickforbrains', 'dickhead', 'dickless', 'dicklick', 'dicklicker', 'dickman', 'dickwad', 'dickweed', 'diddle', 'die', 'died', 'dies', 'dike'
        , 'dildo', 'dingleberry', 'dink', 'dipshit', 'dipstick', 'dirty', 'disease', 'diseases', 'disturbed', 'dive', 'dix', 'dixiedike'
        , 'dixiedyke', 'doggiestyle', 'doggystyle', 'dong', 'doodoo', 'doo-doo', 'doom', 'dope', 'dragqueen', 'dragqween', 'dripdick', 'drug'
        , 'drunk', 'drunken', 'dumb', 'dumbass', 'dumbbitch', 'dumbfuck', 'dyefly', 'dyke', 'easyslut', 'eatballs', 'eatme', 'eatpussy'
        , 'ecstacy', 'ejaculate', 'ejaculated', 'ejaculating', 'ejaculation', 'enema', 'enemy', 'erect', 'erection', 'ero', 'escort', 'ethiopian'
        , 'ethnic', 'european', 'evl', 'excrement', 'execute', 'executed', 'execution', 'executioner', 'explosion', 'facefucker', 'faeces'
        , 'fag', 'fagging', 'faggot', 'fagot', 'failed', 'failure', 'fairies', 'fairy', 'faith', 'fannyfucker', 'fart', 'farted', 'farting', 'farty'
        , 'fastfuck', 'fat', 'fatah', 'fatass', 'fatfuck', 'fatfucker', 'fatso', 'fckcum', 'fear', 'feces', 'felatio', 'felch', 'felcher', 'felching'
        , 'fellatio', 'feltch', 'feltcher', 'feltching', 'fetish', 'fight', 'filipina', 'filipino', 'fingerfood', 'fingerfuck', 'fingerfucked'
        , 'fingerfucker', 'fingerfuckers', 'fingerfucking', 'fire', 'firing', 'fister', 'fistfuck', 'fistfucked', 'fistfucker'
        , 'fistfucking', 'fisting', 'flange', 'flasher', 'flatulence', 'floo', 'flydie', 'flydye', 'fok', 'fondle', 'footaction'
        , 'footfuck', 'footfucker', 'footlicker', 'footstar', 'fore', 'foreskin', 'forni', 'fornicate', 'foursome', 'fourtwenty'
        , 'fraud', 'freakfuck', 'freakyfucker', 'freefuck', 'fu', 'fubar', 'fuc', 'fucck', 'fuck', 'fucka', 'fuckable', 'fuckbag'
        , 'fuckbuddy', 'fucked', 'fuckedup', 'fucker', 'fuckers', 'fuckface', 'fuckfest', 'fuckfreak', 'fuckfriend', 'fuckhead'
        , 'fuckher', 'fuckin', 'fuckina', 'fucking', 'fuckingbitch', 'fuckinnuts', 'fuckinright', 'fuckit', 'fuckknob', 'fuckme'
        , 'fuckmehard', 'fuckmonkey', 'fuckoff', 'fuckpig', 'fucks', 'fucktard', 'fuckwhore', 'fuckyou', 'fudgepacker', 'fugly'
        , 'fuk', 'fuks', 'funeral', 'funfuck', 'fungus', 'fuuck', 'gangbang', 'gangbanged', 'gangbanger', 'gangsta', 'gatorbait'
        , 'gay', 'gaymuthafuckinwhore', 'gaysex', 'geez', 'geezer', 'geni', 'genital', 'german', 'getiton', 'gin', 'ginzo', 'gipp'
        , 'girls', 'givehead', 'glazeddonut', 'gob', 'god', 'godammit', 'goddamit', 'goddammit', 'goddamn', 'goddamned', 'goddamnes', 'goddamnit'
        , 'goddamnmuthafucker', 'goldenshower', 'gonorrehea', 'gonzagas', 'gook', 'gotohell', 'goy', 'goyim', 'greaseball', 'gringo'
        , 'groe', 'gross', 'grostulation', 'gubba', 'gummer', 'gun', 'gyp', 'gypo', 'gypp', 'gyppie', 'gyppo', 'gyppy', 'hamas', 'handjob', 'hapa', 'harder', 'hardon', 'harem', 'headfuck', 'headlights', 'hebe', 'heeb', 'hell', 'henhouse', 'heroin', 'herpes', 'heterosexual', 'hijack', 'hijacker', 'hijacking'
        , 'hillbillies', 'hindoo', 'hiscock', 'hitler', 'hitlerism', 'hitlerist', 'hiv', 'ho', 'hobo', 'hodgie', 'hoes', 'hole', 'holestuffer', 'homicide', 'homo', 'homobangers', 'homosexual', 'honger', 'honk', 'honkers', 'honkey', 'honky', 'hook', 'hooker', 'hookers', 'hooters', 'hore'
        , 'hork', 'horn', 'horney', 'horniest', 'horny', 'horseshit', 'hosejob', 'hoser', 'hostage', 'hotdamn', 'hotpussy', 'hottotrot', 'hummer', 'husky', 'hussy', 'hustler', 'hymen', 'hymie', 'iblowu', 'idiot', 'ikey', 'illegal', 'incest', 'insest', 'intercourse', 'interracial', 'intheass', 'inthebuff', 'israel', 'israeli', "israel's", 'italiano', 'itch', 'jackass', 'jackoff', 'jackshit', 'jacktheripper', 'jade', 'jap', 'japanese', 'japcrap', 'jebus', 'jeez', 'jerkoff', 'jesus', 'jesuschrist', 'jew', 'jewish', 'jiga', 'jigaboo', 'jigg', 'jigga', 'jiggabo', 'jigger', 'jiggy', 'jihad', 'jijjiboo', 'jimfish', 'jism', 'jiz', 'jizim', 'jizjuice', 'jizm', 'jizz', 'jizzim', 'jizzum', 'joint', 'juggalo', 'jugs', 'junglebunny', 'kaffer', 'kaffir', 'kaffre', 'kafir', 'kanake', 'kid', 'kigger', 'kike', 'kill', 'killed', 'killer', 'killing', 'kills', 'kink', 'kinky', 'kissass', 'kkk', 'knife', 'knockers', 'kock', 'kondum', 'koon', 'kotex', 'krap', 'krappy', 'kraut', 'kum', 'kumbubble', 'kumbullbe', 'kummer', 'kumming', 'kumquat', 'kums', 'kunilingus', 'kunnilingus', 'kunt', 'ky', 'kyke', 'lactate', 'laid', 'lapdance', 'latin', 'lesbain', 'lesbayn', 'lesbian', 'lesbin', 'lesbo', 'lez', 'lezbe', 'lezbefriends', 'lezbo', 'lezz', 'lezzo', 'liberal', 'libido', 'licker', 'lickme', 'lies', 'limey', 'limpdick', 'limy', 'lingerie', 'liquor', 'livesex', 'loadedgun', 'lolita', 'looser', 'loser', 'lotion', 'lovebone', 'lovegoo', 'lovegun', 'lovejuice', 'lovemuscle', 'lovepistol', 'loverocket', 'lowlife', 'lsd', 'lubejob', 'lucifer', 'luckycammeltoe', 'lugan', 'lynch', 'macaca', 'mad', 'mafia', 'magicwand', 'mams', 'manhater', 'manpaste', 'marijuana', 'mastabate', 'mastabater', 'masterbate', 'masterblaster', 'mastrabator', 'masturbate', 'masturbating', 'mattressprincess', 'meatbeatter', 'meatrack', 'meth', 'mexican', 'mgger', 'mggor', 'mickeyfinn', 'mideast', 'milf', 'minority', 'mockey', 'mockie', 'mocky', 'mofo', 'moky', 'moles', 'molest', 'molestation', 'molester', 'molestor', 'moneyshot', 'mooncricket', 'mormon', 'moron', 'moslem', 'mosshead', 'mothafuck', 'mothafucka', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckin', 'mothafucking', 'mothafuckings', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherlovebone', 'muff', 'muffdive', 'muffdiver', 'muffindiver', 'mufflikcer', 'mulatto', 'muncher', 'munt', 'murder', 'murderer', 'muslim', 'naked', 'narcotic', 'nasty', 'nastybitch', 'nastyho', 'nastyslut', 'nastywhore', 'nazi', 'necro', 'negro', 'negroes', 'negroid', "negro's", 'nig', 'niger', 'nigerian', 'nigerians', 'nigg', 'nigga', 'niggah', 'niggaracci', 'niggard', 'niggarded', 'niggarding', 'niggardliness', "niggardliness's", 'niggardly', 'niggards', "niggard's", 'niggaz', 'nigger', 'niggerhead', 'niggerhole', 'niggers', "nigger's", 'niggle', 'niggled', 'niggles', 'niggling', 'nigglings', 'niggor', 'niggur', 'niglet', 'nignog', 'nigr', 'nigra', 'nigre', 'nip', 'nipple', 'nipplering', 'nittit', 'nlgger', 'nlggor', 'nofuckingway', 'nook', 'nookey', 'nookie', 'noonan', 'nooner', 'nude', 'nudger', 'nuke', 'nutfucker', 'nymph', 'ontherag', 'oral', 'orga', 'orgasim', 'orgasm', 'orgies', 'orgy', 'osama', 'paki', 'palesimian', 'palestinian', 'pansies', 'pansy', 'panti', 'panties', 'payo', 'pearlnecklace', 'peck', 'pecker', 'peckerwood', 'pee', 'peehole', 'pee-pee', 'peepshow', 'peepshpw', 'pendy', 'penetration', 'peni5', 'penile', 'penis', 'penises', 'penthouse', 'period', 'perv', 'phonesex', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phungky', 'phuq', 'pi55', 'picaninny', 'piccaninny', 'pickaninny', 'piker', 'pikey', 'piky', 'pimp', 'pimped', 'pimper', 'pimpjuic', 'pimpjuice', 'pimpsimp', 'pindick', 'piss', 'pissed', 'pisser', 'pisses', 'pisshead', 'pissin', 'pissing', 'pissoff', 'pistol', 'pixie', 'pixy', 'playboy', 'playgirl', 'pocha', 'pocho', 'pocketpool', 'pohm', 'polack', 'pom', 'pommie', 'pommy', 'poo', 'poon', 'poontang', 'poop', 'pooper', 'pooperscooper', 'pooping', 'poorwhitetrash', 'popimp', 'porchmonkey', 'porn', 'pornflick', 'pornking', 'porno', 'pornography', 'pornprincess', 'pot', 'poverty', 'premature', 'pric', 'prick', 'prickhead', 'primetime', 'propaganda', 'pros', 'prostitute', 'protestant', 'pu55i', 'pu55y', 'pube', 'pubic', 'pubiclice', 'pud', 'pudboy', 'pudd', 'puddboy', 'puke', 'puntang', 'purinapricness', 'puss', 'pussie', 'pussies', 'pussy', 'pussycat', 'pussyeater', 'pussyfucker', 'pussylicker', 'pussylips', 'pussylover', 'pussypounder', 'pusy', 'quashie', 'queef', 'queer', 'quickie', 'quim', 'ra8s', 'rabbi', 'racial', 'racist', 'radical', 'radicals', 'raghead', 'randy', 'rape', 'raped', 'raper', 'rapist', 'rearend', 'rearentry', 'rectum', 'redlight', 'redneck', 'reefer', 'reestie', 'refugee', 'reject', 'remains', 'rentafuck', 'republican', 'rere', 'retard', 'retarded', 'ribbed', 'rigger', 'rimjob', 'rimming', 'roach', 'robber', 'roundeye', 'rump', 'russki', 'russkie', 'sadis', 'sadom', 'samckdaddy', 'sandm', 'sandnigger', 'satan', 'scag', 'scallywag', 'scat', 'schlong', 'screw', 'screwyou', 'scrotum', 'scum', 'semen', 'seppo', 'servant', 'sex', 'sexed', 'sexfarm', 'sexhound', 'sexhouse', 'sexing', 'sexkitten', 'sexpot', 'sexslave', 'sextogo', 'sextoy', 'sextoys', 'sexual', 'sexually', 'sexwhore', 'sexy', 'sexymoma', 'sexy-slim', 'shag', 'shaggin', 'shagging', 'shat', 'shav', 'shawtypimp', 'sheeney', 'shhit', 'shinola', 'shit', 'shitcan', 'shitdick', 'shite', 'shiteater', 'shited', 'shitface', 'shitfaced', 'shitfit', 'shitforbrains', 'shitfuck', 'shitfucker', 'shitfull', 'shithapens', 'shithappens', 'shithead', 'shithouse', 'shiting', 'shitlist', 'shitola', 'shitoutofluck', 'shits', 'shitstain', 'shitted', 'shitter', 'shitting', 'shitty', 'shortfuck', 'sissy', 'sixtyniner', 'skank', 'skankbitch', 'skankfuck', 'skankwhore', 'skanky', 'skankybitch', 'skankywhore', 'skinflute', 'skum', 'skumbag', 'slant', 'slanteye', 'slapper', 'slav', 'slave', 'slavedriver', 'sleezebag', 'sleezeball', 'slideitin', 'slime', 'slimeball', 'slimebucket', 'slopehead', 'slopey', 'slopy', 'slut', 'sluts', 'slutt', 'slutting', 'slutty', 'slutwear', 'slutwhore', 'smack', 'smackthemonkey', 'smut', 'snatch', 'snatchpatch', 'snigger', 'sniggered', 'sniggering', 'sniggers', "snigger's", 'sniper', 'snot', 'snowback', 'snownigger', 'sob', 'sodom', 'sodomise', 'sodomite', 'sodomize', 'sodomy', 'sonofabitch', 'sonofbitch', 'sooty', 'soviet', 'spaghettibender', 'spaghettinigger', 'spank', 'spankthemonkey', 'sperm', 'spermacide', 'spermbag', 'spermhearder', 'spermherder', 'spic', 'spick', 'spig', 'spigotty', 'spik', 'spit', 'spitter', 'splittail', 'spooge', 'spreadeagle', 'spunk', 'spunky', 'squaw', 'stagg', 'stiffy', 'strapon', 'stringer', 'stripclub', 'stroke', 'stroking', 'stupid', 'stupidfuck', 'stupidfucker', 'suck', 'suckdick', 'sucker', 'suckme', 'suckmyass', 'suckmydick', 'suckmytit', 'suckoff', 'suicide', 'swallow', 'swallower', 'swalow', 'swastika', 'sweetness', 'syphilis', 'taboo', 'taff', 'tampon', 'tang', 'tantra', 'tarbaby', 'tard', 'teat', 'terror', 'terrorist', 'teste', 'testicle', 'testicles', 'thicklips', 'thirdeye', 'thirdleg', 'threesome', 'threeway', 'timbernigger', 'tinkle', 'tit', 'titbitnipply', 'titfuck', 'titfucker', 'titfuckin', 'titjob', 'titlicker', 'titlover', 'tits', 'tittie', 'titties', 'titty', 'tnt', 'tongethruster', 'tongue', 'tonguethrust', 'tonguetramp', 'tortur', 'torture', 'tosser', 'towelhead', 'trailertrash', 'tramp', 'trannie', 'tranny', 'transexual', 'transsexual', 'transvestite', 'triplex', 'trisexual', 'trojan', 'trots'
        , 'tuckahoe', 'tunneloflove', 'turd', 'turnon', 'twat', 'twink', 'twinkie', 'twobitwhore', 'uck', 'uk', 'unfuckable'
        , 'upskirt', 'uptheass', 'upthebutt', 'urinary', 'urinate', 'urine', 'usama', 'uterus', 'vagina', 'vaginal', 'vatican'
        , 'vibr', 'vibrater', 'vibrator', 'vietcong', 'violence', 'virgin', 'virginbreaker', 'vomit', 'vulva', 'wab', 'wank'
        , 'wanker', 'wanking', 'waysted', 'weapon', 'weenie', 'weewee', 'welcher', 'welfare', 'wetb', 'wetback'
        , 'wetspot', 'whacker', 'whash', 'whigger', 'whiskey', 'whiskeydick', 'whiskydick', 'whit', 'whitenigger'
        , 'whites', 'whitetrash', 'whitey', 'whiz', 'whop', 'whore', 'whorefucker', 'whorehouse', 'wigger', 'willie'
        , 'williewanker', 'willy', 'wn', 'wog', 'wop', 'wtf', 'wuss', 'wuzzie', 'xtc', 'xxx', 'yankee', 'yellowman'
        , 'zigabo', 'zipperhead', 'douche', 'lmfao', 'lmao']
        for i in eng:
            if i in text:
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

        text = re.sub('카카오톡', '', newtext)
        text = re.sub('카톡', '', text)
        text = re.sub('카페', '', text)
        text = re.sub('하다가', '', text)
        text = re.sub('먹다가', '', text)
        text = re.sub('카와이', '', text)
        text = re.sub('카츠', '', text)
        text = re.sub('카레', '', text)
        mb = ["가카", "이명박근혜", "다스는누구겁니까?"]
        for i in mb:
            if i in text:
                qe = 10

        if qe == 10:
            return True
        else:
            return False




if __name__ == "__main__":
    korcen = korcen()
    while True:
        print(korcen.check(input()))
