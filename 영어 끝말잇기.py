def solution(n, words):
    result = [0, 0]
    
    # index 1 부터 시작하여 0번째 인덱스와 비교
    for i in range(1, len(words)):
        # 이전 단어와 비교
        if words[i][0] != words[i-1][-1]:
            result = [(i%n)+1, (i//n)+1]
            return result
        # 중복 체크
        elif words[i] in words[:i]:
            result = [(i%n)+1, (i//n)+1]
            return result
    else:
        return result

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])