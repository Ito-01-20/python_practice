# Question: Write a program which will find all such numbers which are 
# divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# count_list = []

# for i in range(2000, 3201):
# 	if i % 7 == 0 and i % 5 != 0:
# 		count_list.append(i)

# print(count_list)

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x=int(input())
# print(fact(x))

n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)
