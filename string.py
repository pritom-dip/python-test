my_list = ['a', 'b', 'c', 'd', 'e']

# print the last element
print(my_list[-1])

# Substring
my_string = "I love python."

# prints "love"
print(my_string[2:6])

# prints "love python."
print(my_string[2:])

# prints "I love python"
print(my_string[:-1])

freq = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
print(freq)

 # file add
with open("my_file.txt", "a") as f:
   f.write("new text")