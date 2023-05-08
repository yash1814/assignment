'''
Write a Python program to count the occurrences of each word in a
given sentence
'''
count = 0

my_string = "RAJVEER"
my_char = "R"

for i in my_string:
    if i == my_char:
        count += 1

print(count)
