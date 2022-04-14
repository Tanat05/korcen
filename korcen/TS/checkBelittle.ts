export function belittle(text: string|any): boolean {
    if(!text) throw new Error('Korean: 확인할 텍스트를 입력해 주세요');
    if(typeof text !== 'string') throw new Error('Korean: String 타입만 입력 가능합니다');
    const newtext = text.toLowerCase()
    text = newtext.replace(/련/gi, '년')
    text = text.replace(/뇬/gi, '년')
    text = text.replace(/놈/gi, '년')
    text = text.replace(/러운지/gi, '')
    text = text.replace(/려운지/gi, '년')
    text = text.replace(/[^가-힣]/gi, '')
    const belittling = ["따까리", "장애년", "찐따년", "싸가지", "창년", "썅년", "버러지", "고아년", "고아년", "개간년", "종간나", "도구년", "걸래년", "썅년", "씹년",
                "창녀", "머저리", "씹쓰래기", "씹쓰레기", "씹장생", "씹자식", "운지", "급식충", "틀딱충", "조센징", "매국노", "똥꼬충", "진지충", "듣보잡",
                "한남충","정신병자","중생아","돌팔이","김치녀","폰팔이","틀딱년"]
    for (const i of belittling) {
        if (text.includes(i)) {
            return true;
        }
    }

    return false;
}