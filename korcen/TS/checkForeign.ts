export function foreign(text: string|any): boolean {
    if(!text) throw new Error('Korean: 확인할 텍스트를 입력해 주세요');
    if(typeof text !== 'string') throw new Error('Korean: String 타입만 입력 가능합니다');
    const newtext = text.toLowerCase()
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

    return false;
}