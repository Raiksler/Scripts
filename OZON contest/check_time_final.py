# Скрипт определяет, пересекаются ли заданные временные промежутки в наборе или нет. В случае, если пересечений между промежутками нет, выводится YES
# Скрипт оптимизирован для использования с PyPy и способен эффективно обрабатывать данные при сверхвысоких нагрузках.
# Входные данные:
# 1-я строка - количество наборов данных
# 2-я строка - количество промежутков в наборе
# 3+ строка - временные промежутки в формате hh:mm:ss-hh:mm:ss

from collections import Counter   

def intersection_checker(line):
    try: 
        return sorted_tuple[sorted_tuple.index(line[0]) + 1] != line[1]
    except IndexError:
        return True

def unpacker(sort_set):
    result = []
    for item in sort_set:
        result.append(item[0])
        result.append(item[1])
    return tuple(result)

def find_double_dots(dots):
    counted = Counter(dots)
    for item, num in counted.items():
        if num > 2:
            return True
            
    
def checker():
    current_set = 0
    result = []
    while current_set < sets_num:
        num_of_lines = int(input())
        global lines_in_set
        lines_in_set = set()
        i = 0
        breaker = 0
        while i < num_of_lines:                                   # Добавление временных интервалов в набор       
            if breaker == 0:
                line = tuple(input().split('-'))
                line = tuple(((tuple(map(int, line[0].split(':'))), tuple(map(int, line[1].split(':'))))))
                if (0 <= line[0][0] < 24 and 0 <= line[1][0] < 24) and (0 <= line[0][1] < 60 and 0 <= line[1][1] < 60) and (0 <= line[0][2] < 60 and 0<= line[1][2] < 60):
                    line = (sum((line[0][0] * 3600, line[0][1] * 60, line[0][2])), sum((line[1][0] * 3600, line[1][1] * 60, line[1][2])))
                    lines_in_set.add(line)
                else: 
                    breaker = 1
            else:
                input()
            i += 1
        if breaker == 1: 
            result.append('NO')
            current_set += 1
            continue
        global sorted_tuple
        sorted_tuple = sorted(unpacker(lines_in_set))
        if len(sorted_tuple) < num_of_lines * 2 or find_double_dots(sorted_tuple) == True:                     # Проверка дубликатов
            result.append('NO')
            current_set += 1
            continue
        if any(map(intersection_checker, lines_in_set)):         # Проверка пересечений
            result.append('NO')
            current_set += 1
            continue
        result.append('YES')
        current_set += 1
    for item in result:
        print(item)
    
lines_in_set = set()
sorted_tuple = tuple()
sets_num = int(input())
checker()