# Рассчет скидки 2+1. Скрипт рассчитывает стоимость корзины товаров при условии акции "два одинаковых товара по цене одного". Одинаковыми товарами считаются товары с одинаковой стоимостью.
# Входные данные:
# 1-я строка - количество наборов входных данных, в каждом наборе имеются две строки:
#   1-я строка - количество товаров в корзине покупателя.
#   2-я строка - товары в корзине покупателя, выраженные в виде цен в формате price_first price_second_ price_third price_first ... и тд.

from collections import Counter

count_of_carts = int(input())
i = 0

while i < count_of_carts:
    result = 0
    items_count = int(input())
    prices_in_cart = dict(Counter(input().split()))
    for item in prices_in_cart:
        prices_in_cart[item] = ([int(item)] * prices_in_cart[item])
        del prices_in_cart[item][2::3]
        result += sum(prices_in_cart[item])
    i += 1
    print(result)
    

    
    

