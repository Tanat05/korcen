<div align="center">
  <h1>Korcen</h1>
  <h2>Every journey begins with a single step.</h2>
</div>

![131_20220604170616](https://user-images.githubusercontent.com/85154556/171998341-9a7439c8-122f-4a9f-beb6-0e0b3aad05ed.png)

<div align="center">
  
  [![PyPI version](https://img.shields.io/pypi/v/korcen.svg?style=flat-square)](https://python.org/pypi/korcen)
  [![downloads](https://img.shields.io/pypi/dm/korcen.svg?style=flat-square)](https://pypi.org/project/korcen/)
  [![downloads](https://img.shields.io/pepy/dt/korcen.svg?style=flat-square)](https://pypi.org/project/korcen/)
</div>

"Easy and Powerful Korean Profanity Filtering, Now Accessible to Everyone!"

This project is an intuitive keyword-based profanity filtering system. Developed in Python and optimized for the Korean language, its goal is to enable anyone to easily implement a clean and safe communication environment across various platforms such as websites and applications through simple integration.

[Korcen.ts](https://github.com/KR-korcen/korcen.ts): Same essence, different expression.

[Korcen-go](https://github.com/fluffy-melli/korcen-go): Same essence, different expression.

[Korcen-kogpt2](https://github.com/Tanat05/korcen-kogpt2): This failure is the seed of innovation.

## Installation
>PyPI
```sh
$ pip install korcen
```

>Python
```py
from korcen import korcen

custom_include_text_1 = "이 문장은 나만의 비속어를 포함합니다."
print(f"Custom Include Test 1 ('{custom_include_text_1}'): {check(custom_include_text_1)}")
print(f"Highlight Custom Include 1: {highlight_profanity(custom_include_text_1, level='all')}")

custom_include_text_2 = "이것은 절대 금지 구문입니다."
print(f"Custom Include Test 2 ('{custom_include_text_2}'): {check(custom_include_text_2)}")
print(f"Highlight Custom Include 2: {highlight_profanity(custom_include_text_2, level='all')}")

custom_exclude_text_sexual = "이 영화는 정말 보지도못 할 수준이다."
print(f"Custom Exclude Test (Sexual) ('{custom_exclude_text_sexual}'): {check(custom_exclude_text_sexual)}")
print(f"Highlight Custom Exclude (Sexual): {highlight_profanity(custom_exclude_text_sexual, level='all')}")

custom_exclude_text_general = "무슨 이런 지랄이야!"
print(f"Custom Exclude Test (General) ('{custom_exclude_text_general}'): {check(custom_exclude_text_general)}")
print(f"Highlight Custom Exclude (General): {highlight_profanity(custom_exclude_text_general, level='all')}")

include_vs_exclude_text = "나만의 비속어를 쓰면서 무슨 지랄이야!"
print(f"Include vs Exclude Test ('{include_vs_exclude_text}'): {check(include_vs_exclude_text)}")
print(f"Highlight Include vs Exclude: {highlight_profanity(include_vs_exclude_text, level='all')}")

print("\n--- Demonstrating Changing Custom Filter Paths ---")
alt_include_file = 'alt_custom_include.txt'
alt_exclude_file = 'alt_custom_exclude.txt'

try:
    with open(alt_include_file, 'w', encoding='utf-8') as f:
        f.write("새로운 비속어\n")
    with open(alt_exclude_file, 'w', encoding='utf-8') as f:
        f.write("새로운제외단어\n")
    print(f"korcen: Created temporary test files: {alt_include_file}, {alt_exclude_file}")

    set_custom_filter_paths(include_path=alt_include_file, exclude_path=alt_exclude_file)

    new_include_text = "이것은 새로운 비속어입니다."
    print(f"New Include Test ('{new_include_text}'): {check(new_include_text)}")
    print(f"Highlight New Include: {highlight_profanity(new_include_text, level='all')}")

    old_include_text = "나만의 비속어를 포함합니다."
    print(f"Old Include Test ('{old_include_text}') - Should NOT be flagged: {check(old_include_text)}")

    new_exclude_text = "테스트 문장 새로운제외단어 여기."
    print(f"New Exclude Test ('{new_exclude_text}') - Should NOT be flagged: {check(new_exclude_text)}")
    print(f"Highlight New Exclude: {highlight_profanity(new_exclude_text, level='all')}")

except Exception as e:
    print(f"korcen: Error during changing paths test: {e}")
finally:
    if os.path.exists(alt_include_file):
        os.remove(alt_include_file)
    if os.path.exists(alt_exclude_file):
        os.remove(alt_exclude_file)
    print("korcen: Temporary test files removed.")
    set_custom_filter_paths()


print("\n--- Original Tests ---")
print("--- Boolean Checks (all levels) ---")
print(f"'시발놈아' (general): {general('시발놈아')}")
print(f"'보지마' (sexual - false positive): {sexual('보지마')}")
print(f"'내 보ㅈㅣ 보여줄게' (sexual): {sexual('내 보ㅈㅣ 보여줄게')}")
print(f"'틀딱년 나가' (belittle): {belittle('틀딱년 나가')}")
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
```


Copyright© All rights reserved.
