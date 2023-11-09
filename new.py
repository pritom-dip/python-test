import random
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))
my_list = [1, 'a', 32, 'c', 'd', 31]
print(secrets.choice(my_list))

my_list1 = [1, 'a', 32, 'b', 'c', 31]
print(secrets.choice(my_list1))