# Write a Python function to insert a string in the middle of a string.
'''
def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))
'''
def insert_string(str,word):
    return str[:6 ]+word+str[ 6:]
print(insert_string("how you?","are"))
'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
'''
