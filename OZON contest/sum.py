# Простой сумматор
# Входные данные:
# 1-я строка - количество наборов данных
# 2+ строка - слогаемые в формате first second (через пробел)

import sys

rows = int(sys.stdin.readline())
i = 0
while i < rows:
    x = sys.stdin.readline()
    i += 1
    print(str(sum(list(map(int, x.split())))))