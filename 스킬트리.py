#스킬트리
def solution(skill, skill_trees):
    result = 0
    
    # skill_trees 배열 반복문(skill_trees len로 길이를 구한뒤 range로 범위 지정)
    for x in range(len(skill_trees)):
        beforeSkillNumber = -2
        
        # skill 길이 반복문
        for y in skill:
            # 해당 값이 없거나, 이전 스킬 순번 보다 현재 스킬 순번이 더 높음
            if skill_trees[x].find(y) == -1 or (beforeSkillNumber != -1 and beforeSkillNumber < skill_trees[x].find(y)):
                beforeSkillNumber = skill_trees[x].find(y)
            # 그 외에 모든 케이스
            else:
                break
        else:
            result += 1
    return result