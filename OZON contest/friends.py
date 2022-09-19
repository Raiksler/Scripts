# Возможные друзья. Скрипт симулирует одноименный функционал современных социальных сетей. Задача скрипта, подбирать возможных друзей среди общих.
# Входные данные:
# 1-я строка - количество пользователей и количество пар друзей в формате id_first id_second (ерез пробел)
# 2-я + строки - пары друзей в формате first_id second_id (ерез пробел)
# Для каждого пользователя, скрипт выводит одного или нескольких возможных друзей, в зависимости от количества общих друзей. 

from collections import Counter

def stripper(elem):                                              #Стрипер меняет тип данных!
    return int(elem[0])

def users(num, pairs):
    users = {key: set() for key in map(str, range(1, num + 1))}
    i = 0
    while i < pairs:
        pair = input().split()
        users[pair[0]].add(pair[1])
        users[pair[1]].add(pair[0])
        i += 1
    return users

def possible_friends():
    result = {key: list() for key in map(str, range(1, users_num + 1))}
    for user in user_list:
        for friend in user_list[user]:
            for friend_of_friend in user_list[friend]:
                if friend_of_friend not in user_list[user] and friend_of_friend != user:
                    result[user].append(friend_of_friend)

    for item in result:
        if len(result[item]) == 0:
            result[item].append('0')

    for item in result:
        result[item] = sorted(Counter(result[item]).most_common(), key = lambda element: element[-1])
        biggest = result[item][-1][-1]
        new_item = []
        for element in result[item]:
            if element[-1] == biggest:
                new_item.append(element)
        result[item] = new_item
        result[item] = sorted(list(map(stripper ,result[item])))

    return result

utility_row = input().split()
users_num = int(utility_row[0])
friend_pairs = int(utility_row[1])
user_list = users(users_num, friend_pairs)
possible = possible_friends()
for item in possible:
    possible[item] = ' '.join(map(str, possible[item]))
    print(possible[item])