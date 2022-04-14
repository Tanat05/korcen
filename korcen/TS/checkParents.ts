export function parents(text: string|any): boolean {
    if(!text) throw new Error('Korean: 확인할 텍스트를 입력해 주세요');
    if(typeof text !== 'string') throw new Error('Korean: String 타입만 입력 가능합니다');
    const newtext = text.toLowerCase()
    text = newtext.replace(/[^ㄱ-힣]/gi, '')
    const your = ["ㄴㄱㅁ", "ㄴ금마", "느금ㅁ", "ㄴㄱ마", "ㄴㄱ빠", "ㄴ금빠"]
    for (const i of your) {
        if (text.includes(i)) {
            return true;
        }
    }
    text = newtext.replace(/[^가-힣]/gi, '')
    const your2 = ["느금마", "느그엄마", "늑엄마", "늑금마", "느그애미", "넉엄마", "느그부모", "느그애비", "느금빠", "느그메", "느그빠"]
    for (const i of your2) {
        if (text.includes(i)) {
            return true;
        }
    }

    text = newtext.replace(/[^가-힣]/gi, '')
    text = text.replace(/도/gi, '')
    const motherfuck = ["니애미", "노애미", "노앰", "앰뒤련",
                "아버지도없는게", "애미도없는게", "애비도없는게", "어머니도없는게", "니애비", "노애비","애미없","애비없","애미뒤","애비뒤"]
    for (const i of motherfuck) {
        if (text.includes(i)) {
            return true;
        }
    }

    return false;
}