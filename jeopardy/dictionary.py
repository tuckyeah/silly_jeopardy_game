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
MAX_CATS = 5

# Get categories, questions, answers from spreadsheet
for row in listData:
	if listData.index(row) == 0:
		continue

	# i'm not sure how to randomize these selections - i keep getting errors
	# that the int isn't in the list range?

	QUESTIONS.append(listData[listData.index(row)][2]) # all questions
	ANSWERS.append(listData[listData.index(row)][3]) # all answers
	CATEGORIES.append(listData[listData.index(row)][0]) # all categories


CAT_DICT = dict() # creates dictionary of ALL categories (with qa tuples assigned below)
q_and_a = zip(QUESTIONS, ANSWERS) # creates tuples of questions and answers

for i in range(len(CATEGORIES)):
	if CATEGORIES[i] in CAT_DICT: # if cat already exists, add qa tuple
		CAT_DICT[CATEGORIES[i]].append(q_and_a[i])
	else:
		CAT_DICT[CATEGORIES[i]] = [q_and_a[i]] # create new category entry



def category_list(num_cats):
	# returns a list of randomly chosen categories from all categories
	cat_list = set([]) # 'set' makes sure we only have unique values

	while len(cat_list) < num_cats:
		num = randint(0, len(CATEGORIES)-1)
		cat_list.add(CATEGORIES[num])

	return cat_list


# keep these around for simple play
def random_category():
	# picks a random category
	return CATEGORIES[randint(0, len(CATEGORIES)-1)] 


def random_question(category):
	# gets any/all question(s) associated with the random category chosen
	cat_questions = CAT_DICT.get(category) 
	
	# if there's more than one question... 
	if len(cat_questions) > 1: 
		return cat_questions[randint(0, len(cat_questions)-1)] 
	else:
		return cat_questions[0]


# TESTING STUFF:
# rand_cat = random_category() # picks a random category

# print "Category: " + rand_cat 
# print random_question(rand_cat)

# print len(cat_dict["HISTORY"])
# print random_question("HISTORY")
# print len(cat_dict["HISTORY"])