# Парное программирование. Дан ряд сотрудников. Каждому сотруднику присвоен абстрактный коэффицент производительности (уровень навыков)
# Скрипт разбивает всех сотрудников на команды по два человека таким образом, чтобы в парах работали сотрудники с наиболее близким уровнем навыков.
# Входные данные:
# 1-я строка - количество наборов данных. В каждом наборе данных присутствуют две строки:
#   1-я строка - количество сотрудников в наборе данных
#   2-я строка - уровень навыков для каждого сотрудника в формате int_first int_second int_third (ерез пробел)

from copy import deepcopy

def minimal_skill_dif(person, group):
    group_for_sorting = deepcopy(group)
    group_for_sorting.remove(person)
    group_for_sorting.sort(key=lambda x: (abs(person[1] - x[1]), x[0]))
    return  group_for_sorting[0]
    
num_of_teams = int(input())
i = 0

while i < num_of_teams:                                         #Обработчик команд
    devs_in_team = int(input())
    devs = input().split()
    devs = list(enumerate(list(map(int, devs)), start=1))
    pairs = []
    pair_i = 0
    while len(pairs) < devs_in_team // 2:                       #Обработчик пар в команде
        sameskill = minimal_skill_dif(devs[0], devs)
        pairs.append([devs[0][0], sameskill[0]])
        devs.remove(devs[0])
        devs.remove(sameskill)
    for item in pairs:
        print(item[0], ' ', item[1])
    print()
    i += 1

