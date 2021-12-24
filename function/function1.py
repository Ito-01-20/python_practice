money_list = []

average = 0
while True:
	money = int(input("所持金を入力してください"))
	if money == 0:
		break
	money_list.append(money)


if len(money_list) != 0:
	s = sum (money_list)
	n = len(money_list)
	average = s / n

print(f"全員の所持金の平均は{average}です")