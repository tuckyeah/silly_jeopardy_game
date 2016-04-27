import csv
from random import randint

# once we start using bigger files, we'll have to pick a certain number of questions
# and categories to store, and only pull those...

ifile = open('small_jeopardy.csv', 'rb')
reader = csv.reader(ifile)
listData = list(reader)

QUESTIONS = []
ANSWERS = []
CATEGORIES = []
# MAX_ROWS = 0

for row in listData:
	if listData.index(row) == 0:
		continue

	QUESTIONS.append(listData[listData.index(row)][2]) # all questions
	ANSWERS.append(listData[listData.index(row)][3]) # all answers
	CATEGORIES.append(listData[listData.index(row)][0]) # all categories


cat_dict = dict() # creates dictionary of ALL categories and q/a tuples
q_and_a = zip(QUESTIONS, ANSWERS) # creates tuples of questions and answers

for i in range(len(CATEGORIES)):
	if CATEGORIES[i] in cat_dict: # if cat already exists, add qa tuple
		cat_dict[CATEGORIES[i]].append(q_and_a[i])
	else:
		cat_dict[CATEGORIES[i]] = [q_and_a[i]] # create new category entry



def random_category():
	# picks a random category
	return CATEGORIES[randint(0, len(CATEGORIES)-1)] 


def random_question(category):
	# gets any/all question(s) associated with the random category chosen
	cat_questions = cat_dict.get(category) 
	
	# if there's more than one question... 
	if len(cat_questions) > 1: 
		return cat_questions[randint(0, len(cat_questions)-1)] # pick a random question from that array
	else:
		return cat_questions[0]



# TESTING STUFF:
# rand_cat = random_category() # picks a random category

# print "Category: " + rand_cat 
# print random_question(rand_cat)