num1 = int(input())
num2 = int(input())
num3 = int(input())
if (num1 % 2 == 0 or num2 % 2 == 0) and num3 % 2 != 0:
	print("YES")
elif (num1 % 2 == 0 or num3 % 2 == 0) and num2 % 2 != 0:
	print("YES")
elif (num2 % 2 == 0 or num3 % 2 == 0) and num1 % 2 != 0:
	print("YES")
else:
	print("NO")