import dictionary
from random import randint
from sys import exit

test_list = list(dictionary.category_list())

rand_cat = test_list[randint(0, len(test_list)-1)]

# get questions assigned to cat

question_list = dictionary.CAT_DICT.get(rand_cat)
test_dict = dict() # make a dictionary of those questions and their values


for question in question_list:
	test_dict[dictionary.QUESTION_VALS.get(question)] = question 

keys = test_dict.keys()

keys = [x.strip(' ') for x in keys]

for i in keys:
	print i + "\n"

choice = raw_input("Enter a value: ")

print test_dict.get(choice)
	