price_rub = int(input())
price_kop = int(input())
amount = int(input())
price = (price_rub * 100 + price_kop) * amount 
print(price // 100,  price % 100)