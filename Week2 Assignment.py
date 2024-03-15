my_list =[]
print("before append:", my_list)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("before append:", my_list)
my_list =[10, 20, 30, 40]
my_list.insert(1, 15)
print('New List:', my_list)
my_list = [10, 15, 20, 30, 40]
your_list =[50, 60, 70]
my_list.extend(your_list)
print(my_list)
my_list =[10, 15, 20, 30, 40, 50, 60, 70]
del my_list[-1]
print(my_list)
my_list =[10, 15, 20, 30, 40, 50, 60]
my_list.sort()
print(my_list)
my_list =[10, 15, 20, 30, 40, 50, 60]
index = my_list.index(30)
print(index)


