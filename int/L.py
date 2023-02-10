hour_1 = int(input())
min_1 = int(input())
sec_1 = int(input())
hour_2 = int(input())
min_2 = int(input())
sec_2 = int(input())
time = hour_2 * 3600 + min_2 * 60 + sec_2 -  hour_1 * 3600 - min_1 * 60 - sec_1
print(time)