import random
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))
my_list = [1, 'a', 32, 'c', 'd', 31]
print(secrets.choice(my_list))

my_list1 = [1, 'a', 32, 'b', 'c', 31]
print(secrets.choice(my_list1))

my_list2 = [2, 'a', 33, 'b', 'c', 56]
print(secrets.choice(my_list2))

my_list11 = [8, 'a', 32, '78', 'c', 31]
print(secrets.choice(my_list11))



import random
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))


my_list = [1, 'a', 32, 'c', 'd', 31]
print(secrets.choice(my_list))

print(b'Easy \xE2\x9C\x85'.decode("utf-8"))

list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))

count = 0

my_string = "Programiz"
my_char = "r"

for i in my_string:
    if i == my_char:
        count += 1

print(count)