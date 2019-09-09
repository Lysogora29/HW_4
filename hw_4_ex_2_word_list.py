some_list = [i for i in input("Enter words: ").split()] # элементы вводить через пробел
for i in some_list:
    print(i)

sort_list = sorted(some_list, key=len)
for i in sort_list:
    print(i)

for i in reversed(sort_list):
    print(i)