import re
from collections import OrderedDict
from functools import lru_cache
import os
import colorama

try:
    from better_profanity import profanity
    profanity.load_censor_words()
    BETTER_PROFANITY_LOADED = True
except ImportError:
    print(f"{colorama.Fore.YELLOW}korcen: 'better_profanity' library not found. English filtering will be skipped.{colorama.Style.RESET_ALL}")
    BETTER_PROFANITY_LOADED = False
except Exception as e:
    print(f"{colorama.Fore.RED}korcen: Could not load better_profanity censor words. English filtering might be affected. Error: {e}{colorama.Style.RESET_ALL}")
    BETTER_PROFANITY_LOADED = False

colorama.init(autoreset=True)


cache_size = 0
cache = OrderedDict()


SINGLE_CHAR_NORMALIZATION_MAP = {
    '𝗌': 's', '𝘴': 's', '𝙨': 's', '𝚜': 's', '𝐬': 's', '𝑠': 's', '𝒔': 's', '𝓈': 's', '𝓼': 's', '𝔰': 's', '𝖘': 's', '𝕤': 's',
    'ｓ': 's', 'ş': 's', 'ⓢ': 's', '⒮': 's', '🅢': 's', '🆂': 's', '🅂': 's', '𝑺': 's', 'ſ': 's', 'š': 's', 'ś': 's', 'ŝ': 's',
    'ṣ': 's', 'ṡ': 's', 'ș': 's', 'ṥ': 's', 'ṧ': 's', 'ṩ': 's', '$': 's',
    
    '𝖾': 'e', '𝘦': 'e', '𝙚': 'e', '𝚎': 'e', '𝐞': 'e', '𝑒': 'e', '𝒆': 'e', 'ℯ': 'e', '𝓮': 'e', '𝔢': 'e', '𝖊': 'e', '𝕖': 'e',
    'ｅ': 'e', 'ė': 'e', 'ⓔ': 'e', '⒠': 'e', '🅔': 'e', '🅴': 'e', '🄴': 'e', 'є': 'e', 'ê': 'e', 'ë': 'e', 'é': 'e', 'è': 'e',
    'ē': 'e', 'ĕ': 'e', 'ě': 'e', 'ę': 'e', 'ẹ': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ế': 'e', 'ề': 'e', 'ệ': 'e', 'ễ': 'e', 'ể': 'e',
    '3': 'e', '€': 'e',
    
    '𝗑': 'x', '𝘹': 'x', '𝙭': 'x', '𝚡': 'x', '𝐱': 'x', '𝑥': 'x', '𝒙': 'x', '𝓍': 'x', '𝔁': 'x', '𝔵': 'x', '𝖝': 'x', '𝕩': 'x',
    'ｘ': 'x', 'ⓧ': 'x', '⒳': 'x', '🅧': 'x', '🆇': 'x', '🅇': 'x', '×': 'x', '✕': 'x', '✖': 'x', '❌': 'x', '⨯': 'x',
    '⚔': 'x', '*': 'x', '✗': 'x', '✘': 'x',
    
    'ų': 'u', 'ü': 'u', 'ú': 'u', 'ù': 'u', 'û': 'u', 'ũ': 'u', 'ū': 'u', 'ŭ': 'u', 'ů': 'u', 'ű': 'u', 'ụ': 'u', 'ư': 'u',
    'ç': 'c', 'ć': 'c', 'ĉ': 'c', 'č': 'c', 'ċ': 'c', '¢': 'c', '©': 'c', 'ḉ': 'c', '(': 'c', '<': 'c',
    'Ｆ': 'F', 'Ḟ': 'F', 'Ƒ': 'F', 'ℱ': 'F', 'Ꞙ': 'F', 'Ꝼ': 'F',
    'Ｋ': 'K', 'Ḱ': 'K', 'Ǩ': 'K', 'Ḳ': 'K', 'Ḵ': 'K', 'Ⱪ': 'K', 'Ꝁ': 'K',
    'Ｃ': 'C', 'Ć': 'C', 'Ĉ': 'C', 'Č': 'C', 'Ċ': 'C', 'Ç': 'C', 'Ḉ': 'C',
    'Ｕ': 'U', 'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ũ': 'U', 'Ū': 'U', 'Ŭ': 'U', 'Ů': 'U', 'Ű': 'U', 'Ụ': 'U',
    
    'ㅗ': 'ㅗ', '┻': 'ㅗ', '┴': 'ㅗ', '┹': 'ㅗ', '⊥': 'ㅗ', '†': 'ㅗ', '⟂': 'ㅗ', '╨': 'ㅗ', '╧': 'ㅗ', '╥': 'ㅗ',
    '^': 'ㅅ', '人': 'ㅅ', '∧': 'ㅅ', '㉦': 'ㅅ', 'ᐲ': 'ㅅ', 'Λ': 'ㅅ', '⩘': 'ㅅ', '⋀': 'ㅅ', '⩚': 'ㅅ',
    '甘': 'ㅂ', '廿': 'ㅂ', 'ᗨ': 'ㅂ', 'ᗐ': 'ㅂ', 'ᗕ': 'ㅂ', '田': 'ㅂ', '口': 'ㅂ', '日': 'ㅂ', '目': 'ㅂ', '囗': 'ㅂ',
    '己': 'ㄹ', '乙': 'ㄹ', '己': 'ㄹ', '已': 'ㄹ', '巳': 'ㄹ', '匚': 'ㄷ', 
    '卜': 'ㅏ', 'r': 'ㅏ', 'F': 'ㅏ', '丨': 'ㅏ', '|': 'ㅏ', 'ㅣ': 'ㅏ', '/': 'ㅏ', '⼃': 'ㅏ', '⼁': 'ㅏ', '⼂': 'ㅏ',
    'l': 'ㅣ', '1': 'ㅣ', '|': 'ㅣ', 'I': 'ㅣ', '!': 'ㅣ', '¦': 'ㅣ', '｜': 'ㅣ', '￤': 'ㅣ', 'І': 'ㅣ', 'Ӏ': 'ㅣ',
    'H': 'ㅐ', 'ㅖ': 'ㅐ', 'ㅒ': 'ㅐ', 'H': 'ㅐ', 'Н': 'ㅐ', 'Ⲏ': 'ㅐ', 'ℍ': 'ㅐ',
    '🐦': '새', '🐔': '새', '🦅': '새', '🦉': '새', '🦆': '새', '🦜': '새', '🦤': '새', '🦢': '새', '🕊': '새',
    '🐕': '개', '🐶': '개', '🐺': '개',
    '丕': '조', '朝': '조', '則': '조', '兆': '조', '組': '조', '早': '조', '鳥': '조', '潮': '조', '照': '조',
    '0': 'ㅇ', 'O': 'ㅇ', 'o': 'ㅇ', '◯': 'ㅇ', '⭕': 'ㅇ', '○': 'ㅇ', '●': 'ㅇ', '◎': 'ㅇ', '◉': 'ㅇ', '◌': 'ㅇ',
    
    'a': 'a', '@': 'a', '4': 'a', 'α': 'a', 'ä': 'a', 'å': 'a', 'ã': 'a', 'ā': 'a', 'ȧ': 'a', 'ǎ': 'a',
    'b': 'b', '8': 'b', '6': 'b', 'ƃ': 'b', 'ɓ': 'b', 'Ƅ': 'b', 'ℬ': 'b', 'ᖯ': 'b', 'ᑲ': 'b',
    'd': 'd', 'ḋ': 'd', 'ḍ': 'd', 'ᑯ': 'd', 'ᗞ': 'd', 'ᗪ': 'd', 'ᖙ': 'd', 'ⅆ': 'd', 'ɗ': 'd',
    'f': 'f', 'ƒ': 'f', 'ḟ': 'f', 'ſ': 'f', 'ⅎ': 'f', 'ᶂ': 'f', 'ꜰ': 'f', 'ꟻ': 'f',
    'g': 'g', '9': 'g', 'ǥ': 'g', 'ɡ': 'g', 'ġ': 'g', 'ģ': 'g', 'ĝ': 'g', 'ǧ': 'g',
    'h': 'h', 'ĥ': 'h', 'ħ': 'h', 'ƕ': 'h', 'ḥ': 'h', 'ḫ': 'h', 'ⱨ': 'h', 'ꜧ': 'h',
    'i': 'i', '1': 'i', '!': 'i', '|': 'i', 'ī': 'i', 'ĭ': 'i', 'ǐ': 'i', 'į': 'i',
    'j': 'j', 'ĵ': 'j', 'ǰ': 'j', 'ȷ': 'j', 'ɉ': 'j', 'ⱼ': 'j', 'ʝ': 'j', 'ɟ': 'j',
    'k': 'k', 'ķ': 'k', 'ƙ': 'k', 'ǩ': 'k', 'ḱ': 'k', 'ḳ': 'k', 'ḵ': 'k', 'ⱪ': 'k',
    'l': 'l', '1': 'l', '|': 'l', 'ĺ': 'l', 'ļ': 'l', 'ľ': 'l', 'ŀ': 'l', 'ł': 'l',
    'm': 'm', 'ɱ': 'm', 'ḿ': 'm', 'ṁ': 'm', 'ṃ': 'm', 'ⱥ': 'm', 'ᵯ': 'm', 'ᴍ': 'm',
    'n': 'n', 'ń': 'n', 'ň': 'n', 'ñ': 'n', 'ņ': 'n', 'ṅ': 'n', 'ṇ': 'n', 'ṉ': 'n',
    'p': 'p', 'ṕ': 'p', 'ṗ': 'p', 'ƥ': 'p', 'ᵽ': 'p', 'ᵱ': 'p', 'ᴘ': 'p', 'ᑭ': 'p',
    'q': 'q', '9': 'q', 'ʠ': 'q', 'ɋ': 'q', 'ȹ': 'q', 'ⱊ': 'q', 'ⱍ': 'q', 'ꝗ': 'q',
    'r': 'r', 'ŕ': 'r', 'ř': 'r', 'ŗ': 'r', 'ṙ': 'r', 'ṛ': 'r', 'ṝ': 'r', 'ṟ': 'r',
    't': 't', '7': 't', '+': 't', 'ť': 't', 'ţ': 't', 'ŧ': 't', 'ț': 't', 'ṫ': 't',
    'v': 'v', 'ṿ': 'v', 'ⱴ': 'v', 'ᵥ': 'v', 'ᵛ': 'v', '√': 'v', 'ᐱ': 'v', '∨': 'v',
    'w': 'w', 'ẁ': 'w', 'ẃ': 'w', 'ẅ': 'w', 'ŵ': 'w', 'ẇ': 'w', 'ẉ': 'w', 'ⱳ': 'w',
    'y': 'y', 'ý': 'y', 'ỳ': 'y', 'ŷ': 'y', 'ÿ': 'y', 'ȳ': 'y', 'ẏ': 'y', 'ỵ': 'y',
    'z': 'z', '2': 'z', 'ź': 'z', 'ẑ': 'z', 'ž': 'z', 'ż': 'z', 'ẓ': 'z', 'ẕ': 'z',
}

MULTI_CHAR_REPLACEMENTS = {
    '_ㅣ_': 'ㅗ', '_/_': 'ㅗ', '_ |\_': 'ㅗ', '_|\_': 'ㅗ', '_ㅣ\_': 'ㅗ', '_I_': 'ㅗ',
    '／＼': 'ㅅ', '/＼': 'ㅅ',
    '77': 'ㄲ',
    '刀卜': '까',
    '₨': 'rs',
    'ㅇl=스': '섹스',
    'ㅇㅣ-ㅣ': '애',
    'lㅣ': '니',
    'ㅁㅣ': '미',

}

CUSTOM_INCLUDE_FILE = 'custom_profanity_include.txt'
CUSTOM_EXCLUDE_FILE = 'custom_profanity_exclude.txt'

CUSTOM_INCLUDE_REGEXES = []
CUSTOM_EXCLUDE_REGEXES = []

NORMALIZATION_TABLE = str.maketrans(SINGLE_CHAR_NORMALIZATION_MAP)
URL_REGEX = re.compile(r'https?:\/\/\S+|www\.\S+')
MULTI_CHAR_REPLACEMENT_REGEX = re.compile(
    '|'.join(map(re.escape, sorted(MULTI_CHAR_REPLACEMENTS.keys(), key=len, reverse=True)))
)

FALSE_POSITIVE_PATTERNS_GENERAL = [
    'ㅗ먹어', '오ㅗ', '해ㅗ', '호ㅗ', '로ㅗ', '옹ㅗ', '롤ㅗ', '요ㅗ', '우ㅗ', '하ㅗ',
    'ㅗ오', 'ㅗ호', 'ㅗ로', 'ㅗ옹', 'ㅗ롤', 'ㅗ요', 'ㅗ우', 'ㅗ하',
    'ㅗㅗ오', 'ㅗㅗ호', 'ㅗㅗ로', 'ㅗㅗ옹', 'ㅗㅗ롤', 'ㅗㅗ요', 'ㅗㅗ우', 'ㅗㅗ하',
    '오ㅗㅗㅗ', '호ㅗㅗㅗ', '로ㅗㅗㅗ', '옹ㅗㅗㅗ', '롤ㅗㅗㅗ', '요ㅗㅗㅗ', '우ㅗㅗㅗ', '하ㅗㅗㅗ',
    '오ㅗㅗㅗㅗ', '호ㅗㅗㅗㅗ', '로ㅗㅗㅗㅗ', '옹ㅗㅗㅗㅗ', '롤ㅗㅗㅗㅗ', '요ㅗㅗㅗㅗ', '우ㅗㅗㅗㅗ', '하ㅗㅗㅗㅗ',
    'ㅇㅗ', 'ㅗㄷ', 'ㅗㅜ', 'rㅗ', 'ㅗr', 'sㅗ', 'ㅗs', 'eㅗ', 'ㅗe', 'fㅗ', 'ㅗf', 'aㅗ', 'ㅗa',
    'qㅗ', 'ㅗq', 'ㅗw', 'wㅗ', 'ㅗd', 'dㅗ', 'ㅗg', 'gㅗ', 'ㅈㅗ'
    '118', '218', '318', '418', '518', '618', '718', '818', '918', '018',
    '8분', '8시', '8시발',
    '발닦', '동시8', '다시방', '시불이익', '다시바꿀', '다시바꿔', '다시불러', '다시불안',
    '하시바라이노스케', '할시', '시발음', '시발택시', '시발자동차', '정치발', '시발점', '시발유',
    '시발역', '시발수뢰', '아저씨바', '아저씨발', '시바견', '벌어', '시바이누', '시바스리갈',
    '시바산', '시바신', '오리발', '발끝', '다시바', '다시팔', '비슈누시바', '시바핫카이',
    '시바타이쥬', '데스티니시바', '시바루', '시바료타로', '시바라스시', '임시방편', '젤리',
    '발사', '크시야', '크시', '어찌', '가시방석', '발로란트방', '발로란트', '발로', '씨발라',
    '무시발언', '일시불', '우리', '혹시', '아조씨', '아저씨', '바로', '저거시', '우리발',
    '피시방', '피씨방', '방장', '시바사키', '시발차', '구로역시발', '로벅스', '쉬바나', '벌었는데',
    '엠씨방', '빨리', '파엠', '벌금', '시방향', '불법', '발릴', '발표', '방송', '역시', '바보',
    '쿨리발리', '슈발리에', '방탄', '방어', '발표', '상시', '다시팔게', 
    'opgg', 'opgg',
    '있지', '없지', '하지', '알았지', '몰랐지', '근데', '지근거', '지근하', '지근지근', '지근속근',
    '속든지근', '미지근', '지랄탄', '지랄버릇',
    '0등신', '1등신', '2등신', '3등신', '4등신', '5등신', '6등신', '7등신', '8등신', '9등신',
    '붕우유신',
    '전염병', '감염병', '화염병',
    '왜꺼져', '꺼져요', '이꺼져', '꺼져서', '내꺼져', '제꺼져', '꺼져있', '꺼져잇', '꺼져도',
    '계속꺼져', '꺼져가',
    '새로', '의새끼', '루세끼', '시세끼', '세끼먹', '고양이새끼', '호랑이새끼', '용새끼', '말새끼',
    '사자새끼', '범새끼', '삵새끼', '키보드', '새끼손', '셰리프', '로쉐리', '새끼 양', '새끼 고양이',
    '새끼 사자', '새끼 호랑이', '새끼 용', '새끼 범', '새끼 삵', '새끼 개', '새끼 늑대',
    '0개', '1개', '2개', '3개', '4개', '5개', '6개', '7개', '8개', '9개',
    '1년', '2년', '3년', '4년', '5년', '6년', '7년', '8년', '9년',
    '재밌게놈', '있게', '년생', '무지개색', '떠돌이개', '에게', '넘는', '소개', '생긴게', '날개같다',
    '줫습니다', '줫음', '줫잖아', '줫겠지', '쫒아', '쫒는', '쫒기다', '쫒기라', '쫒기로',
    '쫒기를', '쫒기며', '쫒기는', '쫒기나', '쫒겨', '쫒겻', '쫒겼', '쫒았', '쫒다', '쫒고',
    '줫는', '줫어', '줬는', '줫군', '줬다', '줬어', '천조', '쫒기', '해줫더니', '줫다', '내쫒은',
    '내쫒다', '좇아', "날개",
    'ㅡ'
]
FALSE_POSITIVE_PATTERNS_MINOR = [
    '거미', '친구', '개미', '이미친', '미친증', '동그라미',
    '뒤져봐야', '뒤질뻔', '뒤져보다', '뒤져보는', '뒤져보고', '뒤져간다', '뒤져서',
    '뒤져본', '뒤져봄', '뒤져볼',
]
FALSE_POSITIVE_PATTERNS_SEXUAL = [
    '보지도못', '보지도않', '인가보지', '면접보지', '영화보지', '애니보지', '만화보지', '사진보지',
    '그림보지', '을보지', '나보지', '못보지', '안보지', '왜보지', '뭐보지', '다보지', '빨리보지',
    '보지도마', '보지는않', '보지안으', '보지안아', '게보지', '어케보지', '하나보지', '켜보지',
    '보지맙', '초보지', '로보지', '가보지', '홍보지', '서보지', '보지금', '보지못', '정지금',
    '걸보지', '보지는', '보지지', '보지않', '해보지', '보지마', '보지말', '안보지만', '정보',
    '지팡이', '행보', '바보지', '바보짓', '물어보지', '하시나보지', '챙겨보지만', '봐보지', '보지마라',
    '언제자지', '잠자지', '자지말자고', '지급', '남자지', '여자지', '감자지', '왁자지', '자지러',
    '개발자', '관리자', '약탈자', '타자지', '혼자', '자지원', '사용자', '경력자', '지식', '자지마',
    '자지말', '지원자', '부자지', '혜자지', '잘자지', '일자지', '일찍자지', '지원', '자지금', '자지않',
    '어케자지', '자지도마', '자지는않', '자지좀마', '안자지', '못자지', '지건', '감자', '자 지울거죠',
    '자지말아주세요', '자지마세요', '자지마라', '자지말고',
    'cess', '```css', 'ex)', 'exit', 'ext', 'images', 'https', '(ex', '.ex', 'physics', 'features', 'exam',
    'phase', 'except', 'sexual', 'sexy', '엑섹스', '엑',
    '야스오', '크시야', '카구야', '스파이', '말이야', '스티브', '스쿼드', '파랑색', '오야스미', '노란색',
    '빨간색', '초록색', '보라색', '청색', '핑크색', '남색', '검은색', '하양색', '주황색', '연두색',
    '스공', '스시', '스키장', '스킨', '스킬', '스틸', '스탑', '스트레스', '해야', '카시야스', '야스톤', '유니섹스', '스튜디오',
    '위대한', '소유자', '작업자', '자기위로', '위대하지', '암살자', '학자',
    'freenude', "상자"
]
FALSE_POSITIVE_PATTERNS_BELITTLE = [
    '려운지', '무서운지', '라운지', '운지법', '싸운지', '운지버섯', '운지린다', '깔보다', '깔보시',
    '1년', '2년', '3년', '4년', '5년', '6년', '7년', '8년', '9년', '0년',
    '더운지역', '나따까리', '지킬앤하이드', '지킬엔하이드', '지킬앤하이드', '지킬엔하이드',
]
FALSE_POSITIVE_PATTERNS_RACE = ['흑형님']
FALSE_POSITIVE_PATTERNS_PARENT = ['ㄴㄴ', '미국', '엄창못']
FALSE_POSITIVE_PATTERNS_POLITICS = [
    '카카오톡', '카톡', '카페', '하다가', '먹다가', '카와이', '카츠', '카레', '니가', '내가', '너가',
    '우리가', '너희가', '카카오', '카세트', '카플레이어', '카운터', '카정', '카드', '카구'
]
FALSE_POSITIVE_PATTERNS_ENGLISH = ['```css', 'ex)', '*', 'omg']

FP_REGEX_GENERAL = re.compile('|'.join(map(re.escape, FALSE_POSITIVE_PATTERNS_GENERAL)))
FP_REGEX_MINOR = re.compile('|'.join(map(re.escape, FALSE_POSITIVE_PATTERNS_MINOR)))
FP_REGEX_SEXUAL = re.compile('|'.join(map(re.escape, FALSE_POSITIVE_PATTERNS_SEXUAL)))
FP_REGEX_BELITTLE = re.compile('|'.join(map(re.escape, FALSE_POSITIVE_PATTERNS_BELITTLE)))
FP_REGEX_RACE = re.compile('|'.join(map(re.escape, FALSE_POSITIVE_PATTERNS_RACE)))
FP_REGEX_PARENT = re.compile('|'.join(map(re.escape, FALSE_POSITIVE_PATTERNS_PARENT)))
FP_REGEX_POLITICS = re.compile('|'.join(map(re.escape, FALSE_POSITIVE_PATTERNS_POLITICS)))
FP_REGEX_ENGLISH = re.compile('|'.join(map(re.escape, FALSE_POSITIVE_PATTERNS_ENGLISH)))


GENERAL_PROFANITY_PATTERNS = [
    'ㅗ', '씨8', '18아', '18놈', 'tㅂ', 't발', 'ㅆㅍ', 'sibal', 'sival', 'sibar', 'sibak', 'sipal',
    'siqk', 'tlbal', 'tlval', 'tlbar', 'tlbak', 'tlpal', 'tlqk', '시발', '시val', '시bar',
    '시bak', '시pal', '시qk', 'si바', 'si발', 'si불', 'si빨', 'si팔', 'tl바', 'tl발', 'tl불', 'tl빨', 'tl팔',
    'siba', 'tlba', 'siva', 'tlva', 'tlqkf', '10발놈', '10발년', 'tlqkd', 'si8', '10r놈', '시8', '십8',
    's1bal', 'sib알', '씨x', 'siㅂ', '丨발', '丨벌', '丨바', 'ㅅ1', '시ㅣ', '씨ㅣ', '8시발',
    'ㅆ발', 'ㅅ발', 'ㅅㅂ', 'ㅆㅂ', 'ㅆ바', 'ㅅ바', '시ㅂㅏ', 'ㅅㅂㅏ', '시ㅏㄹ', '씨ㅏㄹ',
    'ㅅ불', 'ㅆ불', 'ㅅ쁠', 'ㅆ뿔', 'ㅆㅣ발', 'ㅅㅟ발', 'ㅅㅣㅂㅏ', 'ㅣ바알', 'ㅅ벌', '^^ㅣ벌',
    'ㅆ삐라', '씨ㅃ', '^^/발', '시봘', '씨봘', '씨바', '시바', '샤발', '씌발', '씹발', '시벌',
    '시팔', '싯팔', '씨빨', '씨랼', '씨파', '띠발', '띡발', '띸발', '싸발', '십발', '슈발',
    '야발', '씨불', '씨랄', '쉬발', '쓰발', '쓔발', '쌰발', '쒸발', '씨팔', '씨밝',
    '씨밯', '쑤발', '치발', '발씨', '리발', '씨볼', '찌발', '씨비바라랄', '시바랄',
    '씨바라', '쒸팔', '쉬팔', '씨밮', '쒸밮', '시밮', '씨삐라', '씨벌', '슈벌', '시불',
    '시부렝', '씨부렝', '시부랭', '씨부랭', '발놈시', '뛰발', '뛰봘', '뜨발', '뜨벌',
    '띄발', '씨바알', '샤빨', '스벌', '쓰벌', '신발련', '신발년', '신발놈', '띠바랄', '시방',
    '씨방', '씨부련', '시부련', '씨잇발', '씨잇파알', '씨잇바알', '시잇발', '시잇바알', '쒸이발',
    '쉬이빨', '씹팔', '쉬바', '시병발신', '씱빩', '쉬바난', '쉬바놈', '쉬바녀', '쉬바년', '쉬바노마', '쉬바새', '쉬불', '쉬이바',
    '시벨놈', '시뱅놈', '시봉새', '씻뻘', '씌벌',
    'wlfkf', 'g랄', 'g럴', 'g롤', 'g뢀', 'giral', 'zi랄', 'ji랄', 'ㅈㄹ', '지ㄹ', 'ㅈ랄', 'ㅈ라',
    '지랄', '찌랄', '지럴', '지롤', '랄지', '쥐랄', '쮜랄', '지뢀', '띄랄',
    'ㅄ', 'ㅂㅅ', '병ㅅ', 'ㅂ신', 'ㅕㅇ신', 'ㅂㅇ신', '뷰신', '병신', '병딱', '벼신', '붱신',
    '뼝신', '뿽신', '삥신', '병시니', '병형신', '뵹신', '병긴', '비응신',
    '염병', '엠병', '옘병', '얨병', '옘뼝',
    '꺼져',
    '엿같', '엿가튼', '엿먹어', '뭣같은',
    'rotorl', 'rotprl', 'sib새', 'ah끼', 'sㅐ끼', 'x끼',
    'ㅅㄲ', 'ㅅ끼', 'ㅆ끼', '색ㄲㅣ', 'ㅆㅐㄲㅑ', 'ㅆㅐㄲㅣ', '새끼', '쉐리', '쌔끼', '썌끼',
    '쎼끼', '쌬끼', '샠끼', '세끼', '샊', '쌖', '섺', '쎆', '십새', '새키', '씹색', '새까',
    '새꺄', '샛끼', '새뀌', '새끠', '새캬', '색꺄', '색끼', '섹히', '셁기', '셁끼', '셐기',
    '셰끼', '셰리', '쉐꺄', '십색꺄', '십떼끼', '십데꺄', '십때끼', '십새꺄', '십새캬', '쉑히',
    '씹새기', '고아새기', '샠기', '애새기', '이새기', '느그새기', '장애새기',
    'w같은', 'ㅈ같', 'ㅈ망', 'ㅈ까', 'ㅈ경', 'ㅈ가튼', '좆', '촟', '조까', '좈', '쫒', '졷',
    '좃', '줮', '좋같', '좃같', '좃물', '좃밥', '줫', '좋밥', '좋물', '좇',
    '썅', '씨앙', '씨양', '샤앙', '쌰앙',
    '뻑유', '뻐킹', '뻐큐', '빡큐', '뿩큐', '뻑큐', '빡유', '뻒큐',
    '닥쳐', '닭쳐', '닥치라', '아가리해',
    'dog새', '개ㅐ색',
    '개같', '개가튼', '개쉑', '개스키', '개세끼', '개색히', '개가뇬', '개새기', '개쌔기', '개쌔끼',
    '쌖', '쎆', '새긔', '개소리', '개년', '개드립', '개돼지', '개씹창', '개간나', '개스끼', '개섹기',
    '개자식', '개때꺄', '개때끼', '개발남아', '개샛끼', '개가든', '개가뜬', '개가턴', '개가툰',
    '개갇은', '개갈보', '개걸레', '개너마', '개너므', '개넌', '개넘', '개녀나',
    '개노마', '개노무새끼', '개논', '개놈', '개뇨나', '개뇬', '개뇸', '개뇽', '개눔', '개느마',
    '개늠', '개랙기', '개련', '개발남아', '개발뇬', '개색', '개색기',
    '개색끼', '개샛키', '개샛킹', '개샛히', '개샜끼', '개생키', '개샠', '개샤끼', '개샤킥',
    '개샥', '개샹늠', '개세리', '개세키', '개섹히', '개섺', '개셃', '개셋키', '개셐',
    '개셰리', '개솩', '개쇄끼', '개쇅', '개쇅끼', '개쇅키', '개쇗', '개쇠리', '개쉐끼', '개쉐리',
    '개쉐키', '개쉑갸', '개쉑기', '개쉑꺄', '개쉑끼', '개쉑캬', '개쉑키', '개쉑히',
    '개쉢', '개쉨', '개쉬끼', '개쉬리', '개쉽', '개습', '개습세', '개습쌔',
    '개싀기', '개싀끼', '개싀밸', '개싀킈', '개싀키', '개싏', '개싑창', '개싘', '개시끼',
    '개시퀴', '개시키', '개식기', '개식끼', '개식히', '개십새', '개십팔', '개싯기', '개싯끼',
    '개싯키', '개싴', '개쌍넘', '개쌍년', '개쌍놈', '개쌍눔', '개쌍늠', '개쌍연', '개쌍영',
    '개쌔꺄', '개쌕', '개쌕끼', '개쌰깨', '개썅', '개쎄', '개쎅', '개쎼키',
    '개쐐리', '개쒜', '개쒝', '개쒯', '개쒸', '개쒸빨놈', '개쒹기', '개쓉', '개씀', '개씁',
    '개씌끼', '개씨끼', '개씨팕', '개씨팔', '개잡것', '개잡년', '개잡놈', '개잡뇬', '개젓',
    '개젖', '개젗', '개졋', '개조또', '개조옷', '개족', '개좃', '개좆', '개좇',
    '개지랄', '개지럴', '개창년', '개허러', '개허벌년', '개호러', '개호로', '개후랄', '개후레',
    '개후로', '개후장', '걔섀끼', '걔잡넘', '걔잡년', '걔잡뇬', '게가튼', '게같은', '게너마',
    '게년', '게노마', '게놈', '게뇨나', '게뇬', '게뇸', '게뇽', '게눔', '게늠', '게띠발넘',
    '게부랄', '게부알', '게새끼', '게새리', '게새키', '게색', '게색기', '게색끼', '게샛키',
    '게세꺄', '게자지', '게잡넘', '게잡년', '게잡뇬', '게젓', '게좆', '계같은뇬', '계뇬',
    '계뇽', '쉬댕', '쉬뎅', '개생끼'
]
MINOR_PROFANITY_PATTERNS = [
    'ㅁㅊ', 'ㅁ친', 'ㅁ쳤', 'aㅣ친', 'me친', '미ㅊ', 'di친',
    '미친놈', '미친새끼',
    '꼽냐', '꼽니', '꼽나',
    '뒤져', '뒈져', '뒈진', '뒈질', '디져라', '디진다', '디질래', '뒤질',
]
SEXUAL_PROFANITY_PATTERNS = [
    'ⓑⓞⓩⓘ', 'bozi', '보ㅈㅣ', '보지', '버지물', '버짓물', '보짓', '개보즤', '개보지', '버지벌렁벌렁', '보짖', '뵤즤', '봊이', '보g',
    'ja지', 'ㅈㅈ빨', '자ㅈ', 'ㅈ지빨', '자지', '자짓', '잦이', '쟈지',
    'sex', 's스', 'x스', 'se스', 's하고e싶다x', 'ㅅㅔㅅㄱ', '이=스', '섹ㅅ', '세ㄱㅅ', '섹스', '섻', '쉑스', '섿스', '섹그', '야스', '색스', '셱스', '섁스', '세엑스', '썩스', '섹수', '섹파', '섹하자', '쉐스', '쉐엑스', '색수', '세엑수우', '섹하고', '섹하구', '섹하장', '섹하쟈', '섹한번', '쌕스',
    '꼬3', '꼬툭튀', '꼬톡튀', '불알', '부랄', '뽕알', '뿅알', '뿌랄', '뿔알', '개부달', '개부랄', '개부러럴', '개부럴', '개부뢀', '개부알', '개불알', '똘추', '똥구멍', '부라랄',
    '오나홍', '오나홀', 'ㅇㄴ홀', '텐가', '바이브레이터', '오ㄴ홀', 'ㅇ나홀', '씹하다', '매춘부', '성노예', '자궁문신',
    '모유물', '로리물', '근친상간', '룸섹스', '원조교재', '속박플레이', '야외플레이',
    '딸딸이', '질싸', '안에사정', '자위남', '자위녀', '폰섹', '포르노', '폰세엑', '폰쉑', '폰쎅', '질내사정', '그룹섹', '남창', '男色', '누워라이년아', '누웠냐씨방새', '다리벌려', '대줄년', '뒤로너어줘', '딸따뤼', '딸쳐', '떡쳐라', '막대쑤셔줘', '막대핥아줘', '먹고보니내딸', '먹고보니누나', '먹고보니딸', '먹고보니똥개', '먹고보니엄마', '먹고보니응아', '먹고보니재수', '먹고보니처제', '먹고보니형수', '몸뚱이줄께', '몸안에사정', '밖에다쌀께', '박고빼고', '배위에싸죠', '몸의대화', '섹할', '섹해',
    'g스팟', '지스팟', '크리토리스', '클리토리스', '페니스', '애널', '젖까', '젖가튼', '젖나', '젖만',
    'ja위', '자위', '고자새끼', '고츄', '꺼추', '꼬추',
]
BELITTLE_PROFANITY_PATTERNS = [
    '10련', '따까리', '장애년', '찐따년', '싸가지', '창년', '썅년', '버러지', '고아년', '개간년', '종간나', '도구년', '걸래년', '씹년', '개걸레',
    '창녀', '머저리', '씹쓰래기', '씹쓰레기', '씹장생', '씹자식', '운지', '급식충', '틀딱충', '조센징', '매국노', '똥꼬충', '진지충', '듣보잡', '개찐따',
    '한남충', '정신병자', '중생아', '돌팔이', '김치녀', '폰팔이', '틀딱년', '같은년', '개돼중', '쓰글년', '썩을년', '썩글년', '씹할', '거지새끼', '거지쉐뀌',
    '거지쉑이', '거지쎄끼', '거지쒜리', '걸래가튼', '걸래넘', '걸래년', '걸래놈', '걸레가튼', '걸레년', '그지새끼', '그지새키', '그지색', '기집년', '까진년',
    '깔보', '난잡년', '빡대가리', '더러운년', '돌아이', '또라이', '장애려', '샹놈', '김치남', '김치녀', '혜지련', '한유남충', '페미나치', '페미년', '꼴페미',
]
RACE_PROFANITY_PATTERNS = [
    '깜둥이', '흑형', '조센진', '짱개', '짱깨', '짱께', '짱게', '쪽바리', '쪽파리', '빨갱이', '니그로', '코쟁이', '칭총', '칭챙총', '섬숭이', '왜놈', '짱꼴라', '섬짱깨',
]
PARENT_PROFANITY_PATTERNS = [
    'ㄴ1ㄱ', 'ㄴ1ㅁ', '느금ㅁ', 'ㄴㄱ마', 'ㄴㄱ빠', 'ㄴ금빠', 'ㅇH미', 'ㄴ1에미', '늬애미', '@ㅐ미', '@ㅐ비',
    'ㄴㄱㅁ', 'ㄴ금마', '늬금마',
    '느금마', '느그엄마', '늑엄마', '늑금마', '느그애미', '넉엄마', '느그부모', '느그애비', '느금빠', '느그메', '느그빠', '니미씨', '니미씹',
    '느그마', '니엄마', '엄창', '엠창', '니미럴', '누굼마', '느금', '내미랄', '내미럴', '엄마없는', '아빠없는', '노에미',
    '니애미', '노애미', '노앰', '앰뒤련', '애믿쥐', '아버지없는게', '애미없는게', '애비없는게', '어머니없는게', '엄마없네', '니애비', '노애비', '애미없', '애비없', '애미뒤', '애비뒤',
    '니아빠', '너에미', '눼기미', '뉘귀미', '뉘기미', '뉘김이', '뉘뮈', '뉘미랄', '뉘미럴', '뉘미롤', '뉘밀얼', '뉘밀할', '뉘어미', '뉘에미',
    '느검마', '늬긔미', '늬기미', '니기미', '니믜창', '니미쒸블', '니미씨펄넘', '니미좃', '니밀할', '니부랑', '니뽕좃',
    '애미죽', '애미디진',
]
JAPANESE_PROFANITY_PATTERNS = [
    "肉便器", "糞野郎", "バカ野郎", "腐れ外道", "部落民", "中出し", "強姦",
    "特定アジア", "人非人", "鬼畜", "負け犬", "支那", "トルコ風呂", "淫売", "未開人",
]
CHINESE_PROFANITY_PATTERNS = ['G巴', 'Ｇ巴', 'G叭', 'Ｇ叭', 'G芭', 'Ｇ芭', 'G掰', 'Ｇ掰', 'g點', 'MM屄', 'mm美圖', 'qvod成人', 'sex聊天室', 'SM後庭器具', 'SM援交', 'SM舔穴', 'sm調教', 'XIAAV論壇''ㄊㄇㄉ', '一本道電影', '一夜性網', '一夜情論壇', '一夜情激情成人聊天室', '九九情色帝國', '九城情色', '二B', '二穴中出', '人人有色論壇', '人妻交換', '人妻色誘', '人妻做愛', '人妻榨乳', '人性本色', '入穴一遊', '三唑侖', '三級激情片', '三陪', '上你幹妳', '上門按摩', '下賤', '口內爆射', '口交', '口含雞巴', '口活', '口射', '口淫', '口爆', '大b', '大力抽送', '大奶美逼', '大奶騷女', '大母牛娛樂論壇', '大乳頭', '大波粉B', '大波騷婦', '大花逼', '大眾色情成人網', '大麻', '大雞巴', '大鶏巴', '女尻', '女屄', '女馬ㄉ', '女馬白勺', '女馬的', '女幹', '小b', '小穴', '小姐上門全套', '小姐打飛機', '小姐裸聊', '小逼', '小嫩雞', '小騷BB', '阝月', '中文搜性網', '互淫', '互舔淫穴', '內射', '公媳亂', '勾魂少婦', '午夜天堂成人', '天天干貼圖', '天天情色', '夫妻3p', '夫妻多p', '夫妻俱樂部', '夫妻亂交', '少女小姐上門', '少女被插', '手淫', '日本鬼子', '日死你', '日你', '日屄', '日逼', '欠日', '欠幹', '毛鮑', '王八', '他ㄇㄉ', '他ㄇ的', '他嗎的', '他媽的', '凸他', '凸她', '凸肉優', '凸你', '凸我', '凸妳', '出售冰毒', '出售曲馬多', '出售苯基丙酮', '出售海豹M9', '出售迷幻藥', '出售迷情藥', '出售氫化可的松', '出售麥角醇', '出售麻古', '出售麻果配方', '出售麻黃素', '出售氯胺酮', '出售腎', '出售間苯三酚', '出售黃牙籤', '出售黃白牙籤', '出售黃麻素', '出售黃體酮', '出售羥基環戊基', '出售槍支', '出售監聽王', '出售蒙汗藥', '出售鄰氯苯晴', '出售磚石冰毒', '出售鎂粉', '出售鹽酸曲馬多', '出售鹽酸曲馬多片', '出售鹽酸羥亞胺', '出售鑽石冰毒', '包二奶', '去你媽的', '去氧麻黃堿製作方法', '可卡因', '叼你媽', '失身粉', '奴隷調教', '奶大屄肥', '尻', '左旋黃麻素', '巨騷', '幼交', '幼妓', '幼逼', '扒穴', '扒屄', '打手槍', '打炮', '打飛機', '打野炮', '本土無碼', '母女雙飛', '母子交歡', '母子姦情', '母奸', '玉穴', '玉乳', '生小孩沒屁眼', '生徒胸觸', '甲基苯丙', '甲基苯胺', '白虎小穴', '白虎少婦', '白虎美女貼圖', '白虎陰穴', '白虎嫩B', '白粉', '白液四濺', '白嫩騷婦', '白漿四濺', '穴海', '穴淫', '穴爽', '穴圖', '交換夫妻', '先奸後殺', '全家死光光', '冰毒', '吃精', '吃雞巴', '合成氯胺酮', '合成鹽酸羥亞胺', '多人性愛', '多人輪', '奸幼', '她馬的', '她媽的', '好色cc', '安非他命', '成人A片', '成人bt', '成人下載', '成人五月天', '成人午夜場', '成人百強', '成人自拍', '成人社區', '成人書庫', '成人情色', '成人情色網站', '成人聊天室', '成人軟體', '成人黃色網站', '成人圖片', '成人圖片網站', '成人網站', '成人網站導航', '成人論壇', '成人導航', '成人激情小說', '成人激情電影', '成人激情圖片', '成人激情網站', '死GM', '死全家', '江山如此多嬌txt下載', '江豬媳', '百性閣', '百鳳宮', '老少亂倫', '老師的小穴', '肉穴', '肉具', '肉便器', '肉洞', '肉唇', '肉淫器吞精', '肉莖', '肉壺', '肉棍', '肉棍幹騷婦', '肉絲褲襪', '肉感炮友', '肉溝', '肉逼', '肉慾', '肉縫', '肉簫', '自拍美穴', '自拍寫真', '自插小穴', '自慰摳穴', '舌頭穴', '色97愛', '色BB吧', '色色成人', '色狐狸網址', '色界論��', '色書庫', '色狼小說', '色狼論壇', '色迷城', '色情工廠', '色情倚天屠龍記', '色情論壇', '色窩窩', '西班牙蒼蠅水', '你他馬的', '你他媽的', '你它馬的', '你它媽的', '你她馬的', '你老母', '你娘卡好', '你麻痹', '你媽比', '你媽的', '你媽逼', '吞精', '吞精騷妹', '含屌', '吸精', '吸精少女', '吹蕭', '妓女', '妓女', '妖媚熟母', '完蛋操', '屁眼', '快樂AV', '我日', '我奸', '我的性啟蒙老師', '我要官人', '我要性交', '我要性交網', '我草', '我做騷妻', '我就去色', '我幹', '我愛我色網址', '我操', '我操你', '杜冷丁', '狂乳激揺', '狂插', '狂插男根膠囊', '狂插性器具', '男女交歡', '男女蒲典', '男女激情淫亂', '肛交', '肛交吹喇叭', '肛屄', '肛門拳交', '肛門噴水', '走光偷拍', '足腳交', '迅雷三級影片', '那娘錯比', '那嗎B', '那嗎老比', '那嗎逼', '那嗎瘟比', '那嗎錯比', '乳尻', '乳交', '乳此絲襪', '乳射', '乳爆', '乳霸', '亞洲有碼', '亞洲性交電影', '亞洲性虐', '亞洲情色網', '亞洲淫娃', '亞洲插穴圖', '供應化學冰', '供應天然咖啡因', '供應可哥精', '供應四氫吡喃酮', '供應奶油冰', '供應甲基可哥堿', '供應甲基苯丙胺', '供應白冰', '供應冰糖', '供應咖啡鹼', '供應咖啡鹼', '供應青蒿素', '供應胡椒基甲基', '供應氫化可的松', '供應麥角醇', '供應麻果丸子', '供應麻黃素', '供應麻穀', '供應植物冰', '供應氯胺酮', '供應無水咖啡因', '供應黃冰', '供應黃體酮', '供應罌粟殼', '供應鹽酸氯', '供應鹽酸羥亞胺', '兩性淫亂地址', '制幻劑', '制服狩', '制服美婦', '制服誘惑', '叔嫂肉慾', '夜色王朝', '夜色貴族', '奇淫寶鑒', '妹妹陰毛', '妹妹騷圖', '屄', '屄毛', '屄屄特寫', '性之站', '性奴', '性奴會', '性用品', '性交', '性交自拍', '性交吞精', '性交易', '性交無碼', '性交圖', '性交課', '性免費電影', '性兩', '性具', '性服務', '性虎', '性虎色網', '性派對', '性虐', '性虐待', '性息', '性高潮', '性聊', '性無能', '性視頻', '性傭', '性愛', '性愛韋小寶之玩女大王', '性愛淫圖', '性愛插穴', '性愛視頻下載', '性愛圖', '性愛擂臺', '性感肉絲', '性感妖嬈', '性感沙灘2', '性感乳娘', '性感誘惑', '性感騷女', '性遊戲', '性夢', '性福', '性福源', '性戰擂臺', '性饑渴', '抽插', '拍肩迷藥', '拔屄', '拔屄自拍', '招妓', '招鶏', '放尿', '放蕩少婦', '放蕩少婦賓館', '放蕩熟女', '明星淫圖', '明星裸體照', '東京丸井買賣', '東洋屄', '松島楓迅雷下載', '波霸乳交器具', '狗b', '狗日', '狗卵子', '狗娘', '狗娘養的', '狗狼養的', '狗養', '狗操', '玩穴', '玩逼', '肏', '肏屄', '肥逼', '花和尚導航', '花都逍遙鄉村春光', '花樣性交', '近親相奸', '近親相姦', '金毛穴', '金鱗豈是池中物全本', '亮穴', '亮屄', '俏臀攝魄', '俗人島', '前凸後翹', '咪咪圖片', '咬著龜頭', '品穴', '品色堂', '品色堂網址', '品香堂', '哇嘎成人三級', '姦染', '姦情', '姦淫', '姦淫', '姦淫電車', '姫辱', '屌人也', '屌女也', '屌他', '屌她', '屌你', '屌我', '屌妳', '帝國夜色', '挑情', '春光外瀉', '春藥', '柔陰術', '毒品出售', '毒龍舔腳', '洗腸射尿', '流淫', '流蜜汁', '炮友之家', '相奸', '紅蜘蛛迷奸藥', '美女b毛圖', '美女成人', '美女吞精', '美女性交真圖', '美女面對面激情裸聊', '美女高潮', '美女淫穴', '美女聊天室', '美女視頻聊天室', '美女祼聊', '美女激情視頻網', '美幼', '美穴', '美乳', '美乳美穴', '美乳鬥豔', '美臀夾陰', '美臀嫰穴', '美騷婦', '美體豔姿', '胡瘟', '虐奴', '虐戀花園', '要色色', '訂購大冰磚', '訂購苯基丙酮', '訂購氯胺酮', '訂購鹽酸羥亞胺', '迫奸', '風騷欲女', '風��淫蕩', '風豔閣', '食精', '香水型迷奸藥', '香煙迷藥催眠迷幻藥', '原味絲襪', '哭母', '哭爸', '唐僧和粉塵女子的性愛生活', '套弄花心', '射奶', '射爽', '射精', '射顏', '恥辱輪奸', '拳交', '捏你鶏巴', '捏弄', '桃園蜜洞', '浪女', '浪叫', '浪穴', '浪婦', '浴尿', '浴室亂倫', '浴室幹騷女系列', '海洛因', '狼友',
    '神經病', '秘唇', '粉穴', '粉屄', '粉紅穴', '胯下呻吟', '胸濤乳浪', '草你娘', '草你媽', '草你媽', '草擬媽', '迷幻藥', '迷失禦花園', '迷奸', '迷奸系列', '迷奸香水', '迷奸藥', '迷情水', '迷情藥製作方法', '迷魂藥', '迷魂藥三唑侖', '迷藥', '迷藥迷情藥', '針孔偷拍', '馬白勺', '高效三唑侖', '高級逼', '高清性愛', '高潮白漿', '高潮集錦', '高麗棒子', '鬼畜輪奸', '鬼輪姦', '假陽具插穴', '做愛', '做愛自拍', '做愛電影', '做愛圖片', '偷拍美穴', '偷窺圖片', '偷歡照片', '動漫色圖', '娼', '婊子', '婬亂軍團', '寂寞自摸', '密穴', '密穴貼圖', '採花堂', '採花網', '梅花屄', '欲仙欲死', '欲仙欲浪', '欲海天龍傳', '殺你一家', '殺你全家', '淩辱', '淫B', '淫女', '淫水', '淫叫', '淫奴', '淫母', '淫汁', '淫穴', '淫穴裡騷水', '淫穴騷水', '淫奸電影', '淫肉誘惑', '淫色', '淫色貼圖', '淫告白', '淫妞', '淫妹', '淫妻', '淫妻交換', '淫姐', '淫店', '淫東方', '淫河', '淫娃', '淫流', '淫虐', '淫師蕩母', '淫書', '淫浪', '淫婦', '淫情', '淫液', '淫貨', '淫絲蕩襪', '淫腔', '淫亂工作', '淫亂診所', '淫亂潮吹', '淫亂熟女', '淫逼', '淫圖', '淫網', '淫蜜', '淫慾', '淫樣', '淫漿', '淫賤', '淫戰群P', '淫蕩迷情藥', '淫蕩貴婦', '淫糜', '淫聲浪語', '淫穢', '淫穢', '淫穢bt電影', '淫穢圖片', '淫獸學園', '淫癡', '淫魔', '淫驢屯', '爽穴', '猖妓', '猛插', '猛操狂射', '現代情色小說', '羞恥母', '聊色', '處女開包', '被幹', '被操', '販賣king粉', '販賣搖頭丸', '逍遙遊論壇', '速效迷奸藥', '造愛', '野外性交', '陰戶', '陰毛', '陰水', '陰穴新玩法', '陰屄', '陰門', '陰阜', '陰阜高聳', '陰莖插小穴', '陰道圖片', '雪腿玉胯', '麻古製作工藝', '婷婷激情聊天室', '媚藥少年', '就去日', '廁奴', '廁所偷拍', '廁所盜攝', '扉之陰', '掰穴', '掰穴打洞', '掰穴皮卡丘', '提供K粉', '提供冰毒', '提供氯胺酮', '提供鹽酸羥亞胺', '插b', '插比', '插穴', '插穴手淫', '插穴止癢', '插穴圖', '插老師穴', '插你媽', '插姐姐嫩穴', '插後庭', '插陰莖', '插進', '插逼', '插暴', '換妻', '朝天穴', '氯胺酮出貨', '氯胺酮技術轉讓', '氯胺酮到貨', '氯胺酮訂購', '氯胺酮電話', '無毛穴', '無毛美少女', '無套自拍', '無碼長片', '無碼炮圖', '無碼做愛', '無碼淫女', '無碼淫漫', '無碼無套', '無碼精選', '無碼體驗', '發浪', '發騷', '硝酸甘油炸藥製造', '童顏巨乳', '絲襪足交', '絲襪高跟', '絲襪淫婦', '腚', '菅野亞梨沙迅雷下載', '菊花洞', '街頭扒衣', '買胡椒基甲基酮', '買賣小冰磚', '買賣四氫吡喃酮', '買賣黃麻素', '買賣鹽酸羥亞胺', '超毛大鮑', '酥穴', '酥胸誘惑', '酥癢', '開苞', '陽具', '陽痿', '集體性愛', '集體淫', '黃牙籤出售', '黃色成人網站', '黃色妹妹a級大片', '黃色妹妹a級大片', '黑毛屄', '黑屄', '黑逼', '亂交', '亂倫', '亂輪', '傻比', '塞你公', '塞你母', '塞你老母', '塞你老師', '塞你爸', '塞你娘', '媽B', '媽比', '媽白勺', '媽批', '媽的', '媽媽色', '媽逼', '嫐屄', '幹78', '幹７８', '幹GY', '幹ＧＹ', '幹一家', '幹七八', '幹人也', '幹入', '幹女也', '幹他', '幹他媽', '幹它', '幹尼', '幹穴', '幹全家', '幹她', '幹她媽', '幹死', '幹死你', '幹汝', '幹你', '幹你老比', '幹你老母', '幹你良', '幹你娘', '幹你媽', '幹你媽b', '幹你媽逼', '幹我', '幹牠', '幹妳', '幹妳老母', '幹妳娘', '幹妳馬', '幹妳媽', '幹拎娘', '幹林', '幹炮', '幹砲', '幹勒', '幹啦', '幹您', '幹您娘', '幹逼', '幹機', '幹機掰', '幹雞', '幹爆', '微型袖珍手狗', '想上你', '惹火自拍', '愛幼閣', '愛色cc', '愛妻淫穴', '愛液', '愛液橫流', '愛愛', '搖頭丸', '搖頭丸', '新金瓶梅', '極品奶妹', '極品白虎', '極品波神', '極品波霸', '極品金髮美女美穴圖', '歇逼', '經典炮圖', '群P', '群交', '群交亂舞', '群奸', '群奸亂交', '群奸輪射', '群陰會', '群魔色舞', '聖泉學淫', '萬淫堂', '裙下風光', '裙內偷拍', '跨下呻吟', '農夫電影', '逼毛', '逼奸', '逼樣', '逼癢', '嫖妓指南', '嫖娼', '嫩b', '嫩BB', '嫩女', '嫩奶', '嫩穴', '嫩屄', '嫩逼', '嫩鮑', '嫩鮑魚', '嫩縫', '對準桃源洞口', '摳穴', '摸你鶏巴', '摸陰蒂', '漏逼', '瑪雅網', '瘋狂抽送', '瘋狗', '監禁陵辱', '碧香亭', '精液', '精液浴', '精液榨取', '緄', '緊穴', '緊縛淩辱', '舔B', '舔奶', '舔穴', '舔屁眼', '舔弄大陰唇', '舔弄小雞雞', '舔屄', '舔腳', '舔逼', '舔雞巴', '蒙汗藥', '蜜穴', '蜜洞', '蜜桃成熟時', '裸聊網站', '裸陪', '裸照圖片', '裸露自拍', '裸體少婦', '裹本', '製作氯胺酮', '製作鹽酸羥亞胺', '製造緬古合成', '製造緬古合成', '誘色uu', '誘姦', '誘惑視頻', '豪乳', '銀民吧', '劌', '噴精', '噴霧蒙汗藥', '墮淫', '嫵媚挑逗', '慰春情', '撅起大白腚', '暴力虐待', '暴奸', '暴乳', '暴淫', '暴幹', '歐美大乳', '歐美無套', '潮噴', '熟女亂倫', '熟女顏射', '熟婦騷器', '窮逼', '線上激情電影', '蓮花逼', '蝴蝶逼', '調教性奴', '調教虐待', '豬操', '賣手槍', '賣比', '賣海洛因', '賣淫', '賣騷', '賤', '賤B', '賤bi', '賤人', '賤比', '賤貨', '賤逼', '賤種', '賫', '輪奸', '輪暴', '輪操', '銷售king粉', '銷售乙醚', '銷售天然咖啡因', '銷售水晶冰', '銷售北朝鮮冰', '銷售可哥精', '銷售左旋麻黃素', '銷售甲基苯丙', '銷售冰古', '銷售苯基丙酮', '銷售純古', '銷售麻古果子', '銷售麻黃素', '銷售間苯三酚', '銷售黃綠牙籤', '銷售羥基環戊基', '銷售趙氏弓弩', '銷售鄰氯苯晴', '銷售鹽酸氯胺酮', '銷售鹽酸羥亞胺', '銷魂洞', '鋝', '靠北', '靠母', '靠爸', '魅惑巨乳', '懆您娘', '懆您媽', '操b', '操B指南', '操人也', '操女也', '操比', '操他', '操母狗', '操穴', '操穴噴水', '操她', '操死', '操你', '操你媽', '操我', '操妳', '操妻', '操屄', '操射', '操爽', '操蛋', '操腫', '操逼', '操機掰', '操爛騷婦', '操爛騷貨', '機8', '機Y', '機Ｙ', '機八', '機巴', '機叭', '機芭', '機掰', '激凸走光', '激情打炮', '激情交友', '激情聊天', '激情圖片', '激情裸體', '激情潮噴', '激插', '蕆', '蕩女', '蕩妹', '蕩婦', '閶', '龜公', '龜兒子', '龜孫子', '龜頭對準陰道', '濕穴', '濕身誘惑', '濫B', '濫比', '濫交', '濫貨', '濫逼', '縱情兵團', '賽你老母', '賽妳阿母', '闃', '鴻圖記', '點色論壇', '翹臀嫩穴', '翹臀嫩逼', '豐唇豔姬', '雙管獵槍買賣', '雙龍入洞', '雜交', '雜種', '雞８', '雞Y', '雞Ｙ', '雞八', '雞巴', '雞巴暴脹', '雞叭', '雞奸', '雞吧', '雞芭', '雞掰', '顏射', '顏射自拍', '顏騎', '懶叫', '懶教', '爆乳人妻', '爆乳娘', '爆操', '獸交', '獸奸', '癟三', '癡乳', '鶏8', '鶏八', '鶏女', '鶏巴', '鶏奸', '鶏吧', '鶏院', '麗春苑', '罌粟', '騷B', '騷女', '騷女叫春', '騷水', '騷包', '騷母', '騷穴', '騷卵', '騷乳', '騷妹', '騷妻', '騷姐姐', '騷屄', '騷姨媽', '騷洞', '騷浪', '騷浪美女', '騷婦掰B', '騷婦露逼', '騷貨', '騷棍', '騷棒', '騷逼', '騷逼噴水', '騷鶏', '灌滿精液', '爛b', '爛比', '爛袋', '爛貨', '爛逼', '蘚鮑', '覽叫', '露B', '露穴', '露屄', '露陰照', '露逼', '鷄巴', '囅', '鹽酸氯胺酮', '鹽酸羥亞胺', '豔母淫臀', '豔乳', '豔婦淫女', '豔情小說', '豔舞淫業',
]
SPECIAL_PROFANITY_PATTERNS = ["🖕🏻", "👌🏻👈🏻", "👉🏻👌🏻", "🤏🏻", "🖕", "🖕🏼", "🖕🏽", "🖕🏾", "🖕🏿", ":middle_finger:"]
POLITICS_PROFANITY_PATTERNS = [
    "노시개", "노알라", "뇌사모", "뇌물현", "응디시티",
    "귀걸이아빠", "달창", "대깨문", "문재앙", "문죄앙", "문죄인", "문크예거", "훠훠훠", "문빠",
    "근혜어", "길라임", "나대블츠", "닭근혜", "댓통령", "레이디가카", "바쁜벌꿀", "수첩공주", "유신공주", "유체이탈화법", "칠푼이", "쿼터갓", 
    "반인반신", "데미갓", "박정희",
    "간철수",
    "가카", "이명박근혜", "다스는누구겁니까",
]

P_REGEX_GENERAL = re.compile('|'.join(map(re.escape, GENERAL_PROFANITY_PATTERNS)))
P_REGEX_MINOR = re.compile('|'.join(map(re.escape, MINOR_PROFANITY_PATTERNS)))
P_REGEX_SEXUAL = re.compile('|'.join(map(re.escape, SEXUAL_PROFANITY_PATTERNS)))
P_REGEX_BELITTLE = re.compile('|'.join(map(re.escape, BELITTLE_PROFANITY_PATTERNS)))
P_REGEX_RACE = re.compile('|'.join(map(re.escape, RACE_PROFANITY_PATTERNS)))
P_REGEX_PARENT = re.compile('|'.join(map(re.escape, PARENT_PROFANITY_PATTERNS)))
P_REGEX_JAPANESE = re.compile('|'.join(map(re.escape, JAPANESE_PROFANITY_PATTERNS)))
P_REGEX_CHINESE = re.compile('|'.join(map(re.escape, CHINESE_PROFANITY_PATTERNS)))
P_REGEX_SPECIAL = re.compile('|'.join(map(re.escape, SPECIAL_PROFANITY_PATTERNS)))
P_REGEX_POLITICS = re.compile('|'.join(map(re.escape, POLITICS_PROFANITY_PATTERNS)))

_FALSE_POSITIVE_REGEX_BY_LEVEL = {
    'general': FP_REGEX_GENERAL,
    'minor': FP_REGEX_MINOR,
    'sexual': FP_REGEX_SEXUAL,
    'belittle': FP_REGEX_BELITTLE,
    'race': FP_REGEX_RACE,
    'parent': FP_REGEX_PARENT,
    'politics': FP_REGEX_POLITICS,
    'english': FP_REGEX_ENGLISH,
}

_PROFANITY_REGEX_BY_LEVEL = {
    'general': P_REGEX_GENERAL,
    'minor': P_REGEX_MINOR,
    'sexual': P_REGEX_SEXUAL,
    'belittle': P_REGEX_BELITTLE,
    'race': P_REGEX_RACE,
    'parent': P_REGEX_PARENT,
    'japanese': P_REGEX_JAPANESE,
    'chinese': P_REGEX_CHINESE,
    'special': P_REGEX_SPECIAL,
    'politics': P_REGEX_POLITICS,
}

_FINAL_FILTER_REGEX_BY_LEVEL = {
    'general': r'[^a-z0-9ㄱ-ㅎㅏ-ㅣ가-힣ㅗ@=\-_]+',
    'sexual': r'[^a-z0-9ㄱ-ㅎㅏ-ㅣ가-힣ㅗ@=\-_]+',
    'parent': r'[^a-z0-9ㄱ-ㅎㅏ-ㅣ가-힣ㅗ@=\-_]+',
    'english': r'[^a-z0-9ㄱ-ㅎㅏ-ㅣ가-힣ㅗ@=\-_]+',
    'chinese': r'[^a-z0-9ㄱ-ㅎㅏ-ㅣ가-힣ㅗ@=\-_]+',
    'special': r'[^a-z0-9ㄱ-ㅎㅏ-ㅣ가-힣ㅗ@=\-_]+',
    'politics': r'[^a-z0-9ㄱ-ㅎㅏ-ㅣ가-힣ㅗ@=\-_]+',
    'minor': r'[^ㄱ-ㅎㅏ-ㅣ가-힣]+',
    'belittle': r'[^ㄱ-ㅎㅏ-ㅣ가-힣]+',
    'race': r'[^ㄱ-ㅎㅏ-ㅣ가-힣]+',
    'japanese': r'[^ㄱ-ㅎㅏ-ㅣ가-힣]+',
}


def _build_reverse_map(normalization_map: dict) -> dict:
    reverse_map = {}
    for source, target in normalization_map.items():
        reverse_map.setdefault(target.lower(), set()).add(source)
    return reverse_map


_REVERSE_SINGLE_CHAR_MAP = _build_reverse_map(SINGLE_CHAR_NORMALIZATION_MAP)
_REVERSE_MULTI_CHAR_MAP = _build_reverse_map(MULTI_CHAR_REPLACEMENTS)


EXACT_MATCH_PROFANITY = {'tq', 'qt'}


def apply_multi_char_replacements(text):
    def replace_match(match):
        return MULTI_CHAR_REPLACEMENTS[match.group(0)]
    return MULTI_CHAR_REPLACEMENT_REGEX.sub(replace_match, text)

def preprocess_text(text: str, level: str):
    processed_text = text.lower()

    processed_text = processed_text.translate(NORMALIZATION_TABLE)
    processed_text = apply_multi_char_replacements(processed_text)
    processed_text = re.sub(r'\s+', '', processed_text)

    if level == 'minor':
        processed_text = re.sub('년', '놈', processed_text)
        processed_text = re.sub('련', '놈', processed_text)
    elif level == 'belittle': 
        processed_text = re.sub('뇬', '련', processed_text)
        processed_text = re.sub('놈', '련', processed_text)
        processed_text = re.sub('넘', '련', processed_text)

        processed_text = re.sub('련', '년', processed_text)

    elif level == 'sexual' and '보g' in processed_text:
        processed_text = re.sub('보g', '보지', processed_text)
    elif level == 'parent':
        pass


    return processed_text

@lru_cache(maxsize=2048)
def build_flexible_regex(pattern_in_processed_text: str):
    flexible_parts = []

    for char in pattern_in_processed_text:
        char_lower = char.lower()
        original_forms = set()
        original_forms.add(re.escape(char))
        original_forms.update(re.escape(k) for k in _REVERSE_SINGLE_CHAR_MAP.get(char_lower, set()))
        original_forms.update(re.escape(k) for k in _REVERSE_MULTI_CHAR_MAP.get(char_lower, set()))
        original_forms = {f for f in original_forms if f}

        if not original_forms:
            flexible_parts.append(re.escape(char))
        elif len(original_forms) == 1:
            flexible_parts.append(next(iter(original_forms)))
        else:
            flexible_parts.append(f"({'|'.join(sorted(original_forms))})")
    return r'\s*'.join(flexible_parts)


def get_false_positive_regex(level: str):
    return _FALSE_POSITIVE_REGEX_BY_LEVEL.get(level)

def get_profanity_regex(level: str):
    return _PROFANITY_REGEX_BY_LEVEL.get(level)

def normalize_for_custom_comparison(text: str) -> str:
    """Applies basic normalization (lowercase, single/multi char, space removal) for custom pattern matching."""
    processed_text = text.lower()
    processed_text = processed_text.translate(NORMALIZATION_TABLE)
    processed_text = apply_multi_char_replacements(processed_text)
    processed_text = re.sub(r'\s+', '', processed_text)
    return processed_text

def load_and_compile_custom_patterns(filepath: str) -> list:
    """Loads patterns from a file, normalizes, escapes, and compiles them."""
    compiled_regexes = []
    if not os.path.exists(filepath):
        return compiled_regexes

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                pattern = line.strip()
                if not pattern or pattern.startswith('#'):
                    continue

                normalized_pattern = normalize_for_custom_comparison(pattern)

                escaped_pattern = re.escape(normalized_pattern)

                try:
                    compiled_regexes.append(re.compile(rf"{escaped_pattern}"))
                except re.error as e:
                    print(f"{colorama.Fore.RED}korcen: Error compiling custom regex '{pattern}' from {filepath}: {e}{colorama.Style.RESET_ALL}")

    except Exception as e:
        print(f"{colorama.Fore.RED}korcen: Error loading custom filter file {filepath}: {e}{colorama.Style.RESET_ALL}")

    return compiled_regexes

def get_final_filter_regex_str(level: str) -> str:
    return _FINAL_FILTER_REGEX_BY_LEVEL.get(level, r'[^a-zA-Z0-9ㄱ-ㅎㅏ-ㅣ가-힣\s]+')


def check_and_report_profanity_pattern(text: str, level: str = 'general'):
    text_no_urls = URL_REGEX.sub('', text)

    processed_text_for_includes = preprocess_text(text_no_urls, level)
    for include_regex in CUSTOM_INCLUDE_REGEXES:
        include_match = include_regex.search(processed_text_for_includes)
        if include_match:
            return include_match.group(0)

    processed_text = preprocess_text(text_no_urls, level)

    if level == 'english' and BETTER_PROFANITY_LOADED:
        fp_regex_english = get_false_positive_regex('english')
        if fp_regex_english:
            text_for_better_profanity = fp_regex_english.sub('', text_for_better_profanity)

        text_for_better_profanity = text_for_better_profanity.replace("*", "")

        censored_text = profanity.censor(text_for_better_profanity, '▩')
        if '▩' in censored_text:
            detected_word_approx = None
            words_in_segment = re.findall(r'\b\w+\b', text_for_better_profanity.lower())
            censored_words_in_segment = re.findall(r'\b\w*▩+\w*\b', censored_text.lower())

            if censored_words_in_segment:
                original_words_split = text_for_better_profanity.split()
                censored_words_split = censored_text.split()
                for ow, cw in zip(original_words_split, censored_words_split):
                    if '▩' in cw:
                        detected_word_approx = ow
                        break

            if detected_word_approx:
                normalized_detected_word = normalize_for_custom_comparison(detected_word_approx)
                for exclude_regex in CUSTOM_EXCLUDE_REGEXES:
                    if exclude_regex.search(normalized_detected_word):
                        return None 
                return detected_word_approx

            fallback_pattern = "english_profanity_detected"
            normalized_fallback = normalize_for_custom_comparison(fallback_pattern)
            for exclude_regex in CUSTOM_EXCLUDE_REGEXES:
                if exclude_regex.search(normalized_fallback):
                    return None
            return fallback_pattern

    if level != 'english' or not BETTER_PROFANITY_LOADED:
        fp_regex = get_false_positive_regex(level)
        text_after_fp = fp_regex.sub('', processed_text) if fp_regex else processed_text

        if level == 'special':
            final_processed_text = text_after_fp
        else:
            final_filter_regex_str = get_final_filter_regex_str(level)
            final_processed_text = re.sub(final_filter_regex_str, '', text_after_fp)

        profanity_regex = get_profanity_regex(level)
        if profanity_regex:
            match = profanity_regex.search(final_processed_text)
            if match:
                detected_profanity_string = match.group(0)

                normalized_detected_profanity = normalize_for_custom_comparison(detected_profanity_string)
                for exclude_regex in CUSTOM_EXCLUDE_REGEXES:
                    if exclude_regex.search(normalized_detected_profanity):
                        return None
                return detected_profanity_string

        if processed_text in EXACT_MATCH_PROFANITY and level == 'general':
            normalized_processed_text = normalize_for_custom_comparison(processed_text)
            for exclude_regex in CUSTOM_EXCLUDE_REGEXES:
                if exclude_regex.search(normalized_processed_text):
                    return None
            return processed_text


    return None


def create_filter_function(level_name: str):
    def filter_func(text: str, id: int = None) -> bool:
        if id is not None:
            if cache_size < 2:
                print(f"{colorama.Fore.YELLOW}korcen: Cache size must be at least 2 for ID based filtering ({level_name}).{colorama.Style.RESET_ALL}")
                return False
        return check_and_report_profanity_pattern(text, level=level_name) is not None
    return filter_func

general = create_filter_function('general')
minor = create_filter_function('minor')
sexual = create_filter_function('sexual')
belittle = create_filter_function('belittle')
race = create_filter_function('race')
parent = create_filter_function('parent')
english = create_filter_function('english')
japanese = create_filter_function('japanese')
chinese = create_filter_function('chinese')
special = create_filter_function('special')
politics = create_filter_function('politics')

def highlight_profanity(text: str, id: int = None, level: str = 'general', highlight_char: str = '!') -> str:
    if id is not None:
        if cache_size < 2:
            print(f"{colorama.Fore.YELLOW}korcen: Cache size must be at least 2 for ID based filtering (highlighting {level}).{colorama.Style.RESET_ALL}")
            return text

    if level.lower() == 'all':
        levels = ['general', 'minor', 'sexual', 'belittle', 'race', 'parent', 
                'special', 'politics']
        
        if BETTER_PROFANITY_LOADED:
            levels.append('english')
            
        levels.extend(['japanese', 'chinese'])
        
        result = text
        for current_level in levels:
            result = highlight_profanity(result, id, current_level, highlight_char)
        return result

    matched_pattern = check_and_report_profanity_pattern(text, level=level)

    if not matched_pattern:
        return text

    text_to_highlight_on = text
    flexible_regex_pattern = build_flexible_regex(matched_pattern)

    try:
        flexible_regex = re.compile(flexible_regex_pattern, re.IGNORECASE)
        highlighted_text = flexible_regex.sub(
            lambda m: f"{highlight_char}{m.group(0)}{highlight_char}",
            text_to_highlight_on
        )
    except re.error as e:
        print(f"{colorama.Fore.RED}korcen: Error compiling flexible regex for '{matched_pattern}' (level {level}): {e}{colorama.Style.RESET_ALL}")
        return text
    return highlighted_text

def set_custom_filter_paths(include_path: str = CUSTOM_INCLUDE_FILE, exclude_path: str = CUSTOM_EXCLUDE_FILE):
    """
    Loads and compiles custom profanity include/exclude patterns from specified files.
    This function can be called by the user to change the paths after initial load.

    Args:
        include_path: Path to the custom include patterns file. Defaults to CUSTOM_INCLUDE_FILE.
        exclude_path: Path to the custom exclude patterns file. Defaults to CUSTOM_EXCLUDE_FILE.
    """
    global CUSTOM_INCLUDE_REGEXES, CUSTOM_EXCLUDE_REGEXES
    CUSTOM_INCLUDE_REGEXES = load_and_compile_custom_patterns(include_path)
    if CUSTOM_INCLUDE_REGEXES:
        print(f"{colorama.Fore.GREEN}korcen: Loaded {len(CUSTOM_INCLUDE_REGEXES)} custom include patterns from {include_path}{colorama.Style.RESET_ALL}")
    CUSTOM_EXCLUDE_REGEXES = load_and_compile_custom_patterns(exclude_path)
    if CUSTOM_EXCLUDE_REGEXES:
        print(f"{colorama.Fore.GREEN}korcen: Loaded {len(CUSTOM_EXCLUDE_REGEXES)} custom exclude patterns from {exclude_path}{colorama.Style.RESET_ALL}")

set_custom_filter_paths()

def check(text: str, id: int=None, foreign: bool=False) -> bool:
    if general(text, id): return True
    if minor(text, id): return True
    if sexual(text, id): return True
    if belittle(text, id): return True
    if race(text, id): return True
    if parent(text, id): return True
    if special(text, id): return True
    if politics(text, id): return True
    if foreign:
        if BETTER_PROFANITY_LOADED and english(text, id): return True
        if japanese(text, id): return True
        if chinese(text, id): return True 

    return False

def check_and_report_profanity_pattern(text: str, level: str = 'general'):
    text_no_urls = URL_REGEX.sub('', text)
    processed_text = preprocess_text(text_no_urls, level)

    for include_regex in CUSTOM_INCLUDE_REGEXES:
        include_match = include_regex.search(processed_text)
        if include_match:
            return include_match.group(0)

    if processed_text in EXACT_MATCH_PROFANITY and level == 'general':
        pass

    fp_regex = get_false_positive_regex(level)
    text_without_false_positives = fp_regex.sub('', processed_text) if fp_regex else processed_text


    if level == 'english':
        if BETTER_PROFANITY_LOADED:
            text_for_better_profanity = text_without_false_positives.replace("*", "")
            censored_text = profanity.censor(text_for_better_profanity, '▩')
            if '▩' in censored_text:
                original_words = text_for_better_profanity.split()
                censored_words = censored_text.split()
                detected_word = None
                for ow, cw in zip(original_words, censored_words):
                    if '▩' in cw:
                        detected_word = ow.lower()
                        break

                if detected_word:
                    normalized_detected_word = normalize_for_custom_comparison(detected_word)
                    for exclude_regex in CUSTOM_EXCLUDE_REGEXES:
                        if exclude_regex.fullmatch(normalized_detected_word):
                            return None
                    return detected_word

                fallback_pattern = "english_profanity_detected"
                normalized_fallback = normalize_for_custom_comparison(fallback_pattern)
                for exclude_regex in CUSTOM_EXCLUDE_REGEXES:
                    if exclude_regex.fullmatch(normalized_fallback):
                        return None
                return fallback_pattern

        else:
            return None

    profanity_regex = get_profanity_regex(level)
    if not profanity_regex:
        return None

    if level == 'special':
        final_processed_text = text_without_false_positives
    else:
        final_filter_regex_str = get_final_filter_regex_str(level)
        final_processed_text = re.sub(final_filter_regex_str, '', text_without_false_positives)

    match = profanity_regex.search(final_processed_text)
    if match:
        detected_profanity_string = match.group(0)

        normalized_detected_profanity = normalize_for_custom_comparison(detected_profanity_string)
        for exclude_regex in CUSTOM_EXCLUDE_REGEXES:
            if exclude_regex.fullmatch(normalized_detected_profanity):
                return None

        return detected_profanity_string

    if processed_text in EXACT_MATCH_PROFANITY and level == 'general':
        normalized_processed_text = normalize_for_custom_comparison(processed_text)
        for exclude_regex in CUSTOM_EXCLUDE_REGEXES:
            if exclude_regex.fullmatch(normalized_processed_text):
                return None
        return processed_text

    return None

# Copyright© All rights reserved.
#  _____                 _
# |_   _|_ _ _ __   __ _| |_
#   | |/ _` | '_ \ / _` | __|
#   | | (_| | | | | (_| | |_
#   |_|\__,_|_| |_|\__,_|\__|


if __name__ == '__main__':
    print("\n--- Custom Filter Tests ---")

    custom_include_text_1 = "이 문장은 나만의 비속어를 포함합니다."
    print(f"Custom Include Test 1 ('{custom_include_text_1}'): {check(custom_include_text_1)}")
    print(f"Highlight Custom Include 1: {highlight_profanity(custom_include_text_1, level='all')}")

    custom_include_text_2 = "이것은 절대 금지 구문입니다."
    print(f"Custom Include Test 2 ('{custom_include_text_2}'): {check(custom_include_text_2)}")
    print(f"Highlight Custom Include 2: {highlight_profanity(custom_include_text_2, level='all')}")

    custom_exclude_text_sexual = "이 영화는 정말 보지도못 할 수준이다."
    print(f"Custom Exclude Test (Sexual) ('{custom_exclude_text_sexual}'): {check(custom_exclude_text_sexual)}")

    custom_exclude_text_general = "무슨 이런 지랄이야!"
    print(f"Custom Exclude Test (General) ('{custom_exclude_text_general}'): {check(custom_exclude_text_general)}")
    print(f"Highlight Custom Exclude (General): {highlight_profanity(custom_exclude_text_general, level='all')}")

    include_vs_exclude_text = "나만의 비속어를 쓰면서 무슨 지랄이야!"
    print(f"Include vs Exclude Test ('{include_vs_exclude_text}'): {check(include_vs_exclude_text)}")
    print(f"Highlight Include vs Exclude: {highlight_profanity(include_vs_exclude_text, level='all')}")

    print("\n--- Boolean Checks (all levels) ---")
    print(f"'시발놈아' (general): {general('시발놈아')}")
    print(f"'보지마' (sexual - false positive): {sexual('보지마')}")
    print(f"'내 보ㅈㅣ 보여줄게' (sexual): {sexual('내 보ㅈㅣ 보여줄게')}")
    print(f"'틀딱년 나가' (belittle): {belittle(' 틀딱년 나가')}")
    print(f"'깜둥이 꺼져' (race): {race('깜둥이 꺼져')}")
    print(f"'ㄴㄱㅁ' (parent): {parent('ㄴㄱㅁ')}")
    if BETTER_PROFANITY_LOADED:
        print(f"'you are a bitch' (english): {english('you are a bitch')}")
    else:
        print("'you are a bitch' (english): SKIPPED (better_profanity not loaded)")
    print(f"'糞野郎め' (japanese): {japanese('糞野郎め')}")
    print(f"'他媽的' (chinese): {chinese('他媽的')}")
    print(f"'🖕🏻' (special): {special('🖕🏻')}")
    print(f"'문죄앙 out' (politics): {politics('문죄앙 out')}")

    print("\n--- Highlighting Profanity (all levels) ---")
    print(f"'시발놈아' (general): {highlight_profanity('시발놈아', level='general')}")
    print(f"'시발놈아 느그보지 찢어줄까?' (all): {highlight_profanity('시발놈아 느그보지 찢어줄까?', level='all')}")
    print(f"'내 보ㅈㅣ 보여줄게' (sexual): {highlight_profanity('내 보ㅈㅣ 보여줄게', level='sexual')}")
    print(f"'이런 틀딱년은 처음봐' (belittle): {highlight_profanity('이런 틀딱년은 처음봐', level='belittle')}")
    print(f"'저기 깜둥이 지나간다' (race): {highlight_profanity('저기 깜둥이 지나간다', level='race')}")
    print(f"'아 ㄴㄱㅁ 뭐하냐' (parent): {highlight_profanity('아 ㄴㄱㅁ 뭐하냐', level='parent')}")
    if BETTER_PROFANITY_LOADED:
        print(f"'you are a stupid bitch' (english): {highlight_profanity('you are a stupid bitch', level='english')}")
    print(f"'이 糞野郎이!' (japanese): {highlight_profanity('이 糞野郎이!', level='japanese')}")
    print(f"'他媽的뭐야' (chinese): {highlight_profanity('他媽的뭐야', level='chinese')}")
    print(f"'손가락 🖕🏻 그만' (special): {highlight_profanity('손가락 🖕🏻 그만', level='special')}")
    print(f"'우리 문죄앙 대통령님' (politics): {highlight_profanity('우리 문죄앙 대통령님', level='politics')}")
    print(f"'http://example.com/sex 섹스하자' (sexual with URL): {highlight_profanity('http://example.com/sex 섹스하자', level='sexual')}")

    print("\n--- Comprehensive Check Function ---")
    print(f"'그냥 일반적인 문장입니다.' (check): {check('그냥 일반적인 문장입니다.')}")
    print(f"'시발 이게 말이 되냐' (check): {check('시발 이게 말이 되냐')}")
    print(f"'야스각인데?' (check): {check('야스각인데?')}")
    if BETTER_PROFANITY_LOADED:
        print(f"'This is absolute bullshit' (check): {check('This is absolute bullshit')}")
    print(f"'꺼져, 이 糞野郎아' (check): {check('꺼져, 이 糞野郎아')}")


# Copyright© All rights reserved.
#  _____                 _
# |_   _|_ _ _ __   __ _| |_
#   | |/ _` | '_ \ / _` | __|
#   | | (_| | | | | (_| | |_
#   |_|\__,_|_| |_|\__,_|\__|
