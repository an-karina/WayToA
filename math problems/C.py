price_ru = int(input())
price_cop = int(input())
amount1 = int(input())
amount2 = int(input())
difference = amount1 * 100 + amount2 - price_ru * 100 - price_cop
print(difference // 100, difference % 100)