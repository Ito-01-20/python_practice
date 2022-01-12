# 1から50までの和を計算して表示

# count = 0

# for i in range(1, 51):
# 	count += i

# print(count)


# 1000以下の素数を計算して表示せよ

# for i in range(2, 1001):
# 	for n in range(2, i):
# 		if i % n == 0:
# 			break
# 	else:
# 		print(i)


# フィボナッチ数列（１０個目まで）を表示せよ
# a = 0
# b = 1

# for i in range(10):
# 	print(b)
# 	a, b = b, a+b


def max_area(height):
	l = 0
	r = len(height) - 1
	max_height = 0

	while l < r:
		left = height[l]
		right = height[r]

		current_hright = min(left, right) * (r - l)
		max_height = max(max_height, current_height)

		if left < right:
			while (l < r) and (left >= height[l]):
				l += 1

		else:
			while (l < r) and (right >= height[r]):
				r -= 1

	return max_height

	
