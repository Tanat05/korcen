import re


def check(text):
    ae = 0 #0=검열X  1=검열O
    be = 0
    ce = 0
    de = 0
    ee = 0
    fe = 0
    ge = 0
    he = 0
    le = 0
    qe = 0
    #--------------------------------------------------------------------------------------------
       
    text = text.lower() #대문자 > 소문자
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

    
    #띄어쓰기 지우기
    #text = re.sub(' ', '', text)
    #숫자&특문 지우기 
    # text = re.sub(r'[0-9]+', '', text)
    #자음&모음 지우기
    #text = re.sub("[ㅂㅁㅋㅈㄴㅌㄷㅇㅊㄱㄹㅍㅅㅎㅃㅉㄸㄲㅆㅠㅛㅗㅜㅕㅓㅡㅑㅏㅐㅣㅔㄺㄼㄽㅃㅉㄸㄲㅆㅀㄿㄾㅘㅚㅟㅝㅞㅢㅙ]","", text)
    #자음&모음 한글 빼고 다 지우기
    #text = re.sub("[^ㄱ-힣]","", text)
    #한글만 남기기
    #text = re.sub("[^가-힣]","", text)
    #영어 지우기
    #text = re.sub("[\--z]", "", text)
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
    ㅗ = ["ㅗ","┻","┴","┹","_ㅣ_","_l_","_/_","⊥","_ |\_","_|\_","_ㅣ\_","_I_"]
    for i in ㅗ:
        if i in text:
            ae = 1

    text = re.sub(r'\^', 'ㅅ', newtext)#여기가 문제
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
    text = re.sub("[^ㄱ-힣]","", text)
    시발 = ["시ㅂ","시ㅏㄹ","씨ㅂ","씨ㅏㄹ","ㅣ발","ㅆ발","ㅅ발","ㅅㅂ","ㅆㅂ","ㅆ바","ㅅ바","시ㅂㅏ","ㅅㅂㅏ","시ㅏㄹ","씨ㅏㄹ","ㅅ불","ㅆ불","ㅅ쁠","ㅆ뿔"]
    for i in 시발:
        if i in text :
            ae = 1

    text = re.sub("[^가-힣]","", text)
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
    text = re.sub('ㅣ', '', text)
    시발 = ["시발","씨발","시봘","씨봘","씨바","시바","샤발","씌발","씹발","시벌","시팔","싯팔","씨빨","씨랼","씨파","띠발","띡발","띸발","싸발","십발","슈발","야발","씨불","씨랄","쉬발","쓰발","쓔발","쌰발","쉬발","쒸발","씨팔","씨밝","씨밯","쑤발","치발","샤발","발씨","리발","씨볼","찌발","씨비바라랄","시바랄","씨바라"]
    for i in 시발:
        if i in text :
            ae = 1

    text = re.sub("[^ㄱ-힣]","", newtext)
    text = re.sub("근","ㄹ", newtext)
    text = re.sub("[^ㄱ-힣]","", newtext)
    ㅈㄹ = ["ㅈㄹ","지ㄹ","ㅈ랄","ㅈ라"]
    for i in ㅈㄹ:
        if i in text :
            ae = 1

    text = re.sub("[^가-힣]","", text)
    text = re.sub('지랄탄', '', text)
    text = re.sub('지랄버릇', '', text)
    text = re.sub('이', '', text)
    지랄 = ["지랄","찌랄","지럴","지롤","랄지"]
    for i in 지랄:
        if i in text :
            ae = 1

    
    text = re.sub("[^ㄱ-힣]","", newtext)
    text = re.sub('빙', '병', text)
    text = re.sub('븅', '병', text)
    text = re.sub('등', '병', text)
    text = re.sub('붱', '병', text)
    text = re.sub('뵝', '병', text)
    text = re.sub('뼝', '병', text)
    text = re.sub('싄', '신', text)
    text = re.sub('씬', '신', text)
    병신 = ["ㅄ","ㅂㅅ","병ㅅ","ㅂ신","ㅕㅇ신"]
    for i in 병신:
        if i in text :
            ae = 1

    text = re.sub("[^가-힣]","", text)
    text = re.sub('영', '', text)
    text = re.sub('엉', '', text)
    병신 = ["병신","병딱","벼신"]
    for i in 병신:
        if i in text :
            ae = 1

    text = re.sub(r'[0-9]+', '', newtext)
    text = re.sub("[ㅂㅁㅋㅈㄴㅌㄷㅇㅊㄱㄹㅍㅅㅎㅃㅉㄸㄲㅆㅠㅛㅗㅜㅕㅓㅡㅑㅏㅐㅣㅔㄺㄼㄽㅃㅉㄸㄲㅆㅀㄿㄾㅘㅚㅟㅝㅞㅢㅙ]","", text)
    text = re.sub("[\--z]", "", text)
    text = re.sub('전염병', '', text)
    염병 = ["염병","엠병","옘병","염병","얨병"]
    for i in 염병 :
        if i in text :
            ae = 1

    text = re.sub("[^가-힣]","", newtext)
    text = re.sub('왜꺼져', '', text)
    text = re.sub('꺼져요', '', text)
    text = re.sub('이꺼져', '', text)
    text = re.sub('꺼져서', '', text)
    text = re.sub('내꺼져', '', text)
    text = re.sub('제꺼져', '', text)
    text = re.sub('꺼져있', '', text)
    if "꺼져" in text:
        ae = 1

    text = re.sub("[^가-힣]","", newtext)
    개 = ["엿같","엿가튼","엿먹어"]
    for i in 개 :
        if i in text :
            ae = 1

    
    text = re.sub(r'\^', 'ㅅ', newtext)
    text = re.sub('H', 'ㅐ', text) 
    text = re.sub("[^가-힣]","", text)
    새끼 = ["ㅅㄲ","ㅅ끼","ㅆ끼","쎆","쌖"]
    for i in 새끼:
        if i in text :
            ae = 1

    text = re.sub('의새끼', '', text)
    text = re.sub('애', '', text)
    text = re.sub('에', '', text)
    새끼 = ["새끼","쉐리","쌔끼","썌끼","쎼끼","쌬끼","샠끼"]
    동물 = ["고양이,""사바나캣","너구리","붉은여우","사막여우","북극여우","코요테","딩고","서벌","오셀롯","페럿","스컹크","라쿤","수달","몽구스","미어캣","사향고양이","햄스터","양","알파카","라마","사슴","토끼","다람쥐","앵무새","부엉이","올빼미","거북이","개구리"]
    for i in 동물:
        if not i in text :
            text = re.sub('새끼', '', text)
    for i in 새끼:
        if i in text :
            ae = 1

    text = re.sub("[^ㄱ-힣]","", newtext)
    좆 = ["ㅈ같","ㅈ망","ㅈ까","ㅈ경"]
    for i in 좆:
        if i in text :
            ae = 1

    text = re.sub("[^가-힣]","", text)
    좆 = ["좆","촟","조까","좈","쫒","졷","좃"]
    for i in 좆:
        if i in text :
            ae = 1

    text = re.sub("[^가-힣]","", text)
    썅 = ["썅","씨앙","씨양"]
    for i in 썅:
        if i in text :
            ae = 1

    욕 = ["tq","qt"]
    for i in 욕:
        if text == i :
            ae = 1


    text = re.sub("[^가-힣]","", newtext)
    text = re.sub('전염병', '', text)
    text = re.sub('이꺼져', '', text)
    개 = ["개같","개가튼","개쉑","개스키","개세끼","개색히","개가뇬","개새기","개쌔기","개쌔끼","쌖","쎆","새긔","개소리","개년","개소리","개드립"]
    for i in 개 :
        if i in text :
            be = 2

    
    text = re.sub("[^ㄱ-힣]","", newtext)
    미친 = ["ㅁㅊ","ㅁ친","ㅁ쳤"]
    for i in 미친:
        if i in text :
            be = 2

    text = re.sub("[^가-힣]","", text)
    text = re.sub('이미친', '', text)
    text = re.sub('미친증', '', text)
    미친 = ["미친","미쳤"]
    for i in 미친:
        if i in text :
            be = 2

    text = re.sub("[^가-힣]","", text)
    꼽냐 = ["꼽냐","꼽니","꼽나"]
    for i in 꼽냐:
        if i in text :
            print("꼽냐")

    
    text = re.sub("[^ㄱ-힣]","", newtext)
    text = re.sub('보지도못', '', text)
    text = re.sub('보지도않', '', text)
    text = re.sub('켜보지', '', text)
    text = re.sub('보지맙', '', text)
    text = re.sub('초보지', '', text)
    text = re.sub('로보지', '', text)
    text = re.sub('홍보지', '', text)
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
    보지 = ["보지"]
    for i in 보지:
        if i in text :
            ce = 3

    text = re.sub("[^ㄱ-힣]","", newtext)
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
    자지 = ["자지"]
    for i in 자지:
        if i in text :
            ce = 3

    text = re.sub('wase', '', text)
    text = re.sub(r'\^', 'ㅅ', newtext)
    text = re.sub('sex', '섹스', text)
    text = re.sub('s', 'ㅅ', text)
    text = re.sub('x', 'ㅅ', text)
    text = re.sub('엑', '', text)
    text = re.sub("[^ㄱ-힣]","", text)
    섹스 = ["ㅅㅔㄱ스","섹ㅅ","ㅅ스","세ㄱㅅ","ㅅㅔㄱㅅ"]
    for i in 섹스:
        if i in text :
            ce = 3

    text = re.sub("[^가-힣]","", text)
    text = re.sub("야스오","", text)
    섹스 = ["섹스","섻스","쉑스","섿스","섹그","야스","색스","셱스","섁스","세엑스","썩스"]
    for i in 섹스:
        if i in text :
            ce = 3

    text = re.sub("[^가-힣]","", text)
    불알 = ["불알","부랄","뽕알","뿅알","뿌랄","뿔알"]
    for i in 불알:
        if i in text:
            ce = 3

    text = re.sub("[^ㄱ-힣]","", text)
    오나홀 = ["오나홍","오나홀","ㅇㄴ홀"]
    for i in 오나홀:
        if i in text:
            ce = 3

    text = re.sub("[^가-힣]","", text)
    불알 = ["불알","부랄","뽕알","뿅알","뿌랄","뿔알"]
    for i in 불알:
        if i in text:
            ce = 3

            

    text = re.sub('련','년',text)
    text = re.sub('뇬','년',text)
    text = re.sub('놈','년',text)
    text = re.sub('러운지','',text)
    text = re.sub('려운지','',text)
    text = re.sub("[^가-힣]","", text)
    비하 = ["따까리","장애년","찐따년","싸가지","창년","썅년","버러지","고아년","고아년","개간년","종간나","도구년","걸래년","썅년","씹년","창녀","머저리","씹쓰래기","씹쓰레기","씹장생","씹자식","운지","급식충","틀딱충","조센징","매국노","똥꼬충","진지충","듣보잡","한남충"]
    for i in 비하:
        if i in text:
            de = 4


    text = re.sub("[^가-힣]","", text)
    비하 = ["깜둥이","흑형"]
    for i in 비하:
        if i in text:
            ee = 5


    text = re.sub("[^ㄱ-힣]","", text)
    느그 = ["ㄴㄱㅁ","ㄴ금마","느금ㅁ","ㄴㄱ마","ㄴㄱ빠","ㄴ금빠"]
    for i in 느그:
        if i in text :
            fe = 6

    text = re.sub("[^가-힣]","", text)
    느그 = ["느금마","느그엄마","늑엄마","늑금마","느그애미","넉엄마","느그부모","느그애비","느금빠","느그메","느그빠"]
    for i in 느그:
        if i in text :
            fe = 6

    text = re.sub("[^가-힣]","", newtext)
    text = re.sub("[^가-힣]","", text)
    
    애미 = ["니애미","노애미","노앰","앰뒤련",
            "아버지도없는게","애미도없는게","애비도                      없는게","어머니도없는게","니애비","노애비"]              
    for i in 애미:
        if i in text :
            fe = 6


    text = re.sub('[^a-z]','',newtext)
    if "fuck" in text:
        ge = 7

    text = re.sub('[^a-z]','',newtext)
    if "commie" in text:
        ge = 7

    text = re.sub('[^a-z]','',newtext)
    if "knod" in text:
        ge = 7

    text = re.sub('[^a-z]','',newtext)
    if "cunt" in text:
        ge = 7

    text = re.sub('[^a-z]','',newtext)
    if "Dotard" in text:
        ge = 7

    text = re.sub('[^a-z]','',newtext)
    if "Dyke" in text:
        ge = 7

    text = re.sub("[^ㄱ-힣]","", newtext)
    뻑유 = ["뻑유","뻐킹","뻐큐"]
    for i in 뻑유:
        if i in text :
            ae = 1


    이모지 = ["🖕🏻", "👌🏻👈🏻", "👉🏻👌🏻", "🤏🏻", "🖕", "🖕🏼", "🖕🏽", "🖕🏾", "🖕🏿"]
    for i in 이모지:
        if i in newtext:
            le = 9

  
    노무현 = ["노시개","노알라","뇌사모","뇌물현"]
    for i in 노무현:
        if i in newtext:
            qe = 10

    문재인 = ["귀걸이아빠","달창","대깨문","문재앙","문죄앙","문죄인","문크예거","훠훠훠","문빠"]
    for i in 문재인:
        if i in newtext:
            qe = 10

    박근혜 = ["근혜어","길라임","나대블츠","닭근혜","댓통령","레이디가카","바쁜벌꿀","수첩공주","유신공주","유체이탈화법","칠푼이","쿼터갓"]
    for i in 박근혜:
        if i in newtext:
            qe = 10

    
    박정희 = ["반인반신","데미갓","박정희"]
    for i in 박정희:
        if i in newtext:
            qe = 10

    안철수 = ["간철수"]
    for i in 안철수:
        if i in newtext:
            qe = 10

    이명박 = ["가카","이명박근혜","다스는누구겁니까?"]
    for i in 이명박:
        if i in newtext:
            qe = 10

    
    
    if ae == 1:
        return 1
    if be == 2:
        return 2
    if ce == 3:
        return 3
    if de == 4:
        return 4
    if ee == 5:
        return 5
    if fe == 6:
        return 6
    if ge == 7:
        return 7
    if le == 9:
        return 8
    if qe == 10:
        return 9
    else :
        return 0


if __name__=="__main__":
    a = check("씨발")
    print(a)