my_list = [1, -2, 16, -13, 20, 0, 3, 77]
result_list = list() #создали второй пустой список и добавляем в него новые значения

for item in my_list:
    if item < 0:
        result_list.append(-1)
    elif item > 0:
        result_list.append(1)
    else:
        result_list.append(0)
print(result_list)
print(my_list)




new_list = my_list[:]
print(new_list)

for item in range(len(new_list)):
    if new_list[item] > 0:
        new_list[item] = 1
    elif new_list[item] < 0:
        new_list[item] = -1
    else:
        new_list[item] = 0
print(new_list)




sor_list = new_list[:]
print(sor_list)

neg_list = list()
pos_list = list()

for i in sor_list:
    if i > 0:
        pos_list.append (i)
    if i < 0:
        neg_list.append (i)
print(pos_list)
print(neg_list)



print(my_list)
print('min:', min(my_list))
print('max:', max(my_list))

