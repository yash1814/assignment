#  Write a Python function that takes a list of words and returns the length
#  of the longest one.

def count_word_length(my_list):
    counter = 0
    for i in my_list:
        if len(i) >= counter:
            counter = len(i)

print("The word with the longest length is:",counter)



a=['vishal','pankaj','narendra']
max=len(a)
longest=a[0]
for i in a:
    if(len(i)>max):
       max1=len(i)
       longest=i
print("The word with the longest length is:",longest)
