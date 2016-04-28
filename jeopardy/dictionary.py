import csv
import re
from random import randint

# once we start using bigger files, we'll have to pick a certain number of questions
# and categories to store, and only pull those...

ifile = open('small_jeopardy.csv', 'rb')
reader = csv.reader(ifile)
listData = list(reader)

QUESTIONS = []
ANSWERS = []
CATEGORIES = []
VALUES = []
MAX_CATS = 5

# Get categories, questions, answers from spreadsheet
for row in listData:

	#skip header row and any result with a link in it links
	if listData.index(row) == 0 or re.search("href", str(listData[listData.index(row)])):
		continue
	
	CATEGORIES.append(listData[listData.index(row)][0]) # all categories
	VALUES.append(listData[listData.index(row)][1]) # Dollar Amounts
	QUESTIONS.append(listData[listData.index(row)][2]) # all questions
	ANSWERS.append(listData[listData.index(row)][3]) # all answers


# DICTIONARY BUILDING

CAT_DICT = dict() # creates dictionary of ALL categories (with qa tuples assigned below)
q_and_a = zip(QUESTIONS, ANSWERS) # creates tuples of questions and answers


for i in range(len(CATEGORIES)):
	if CATEGORIES[i] in CAT_DICT: # if cat already exists, add qa tuple
		CAT_DICT[CATEGORIES[i]].append(q_and_a[i])
	else:
		CAT_DICT[CATEGORIES[i]] = [q_and_a[i]] # create new category entry

QUESTION_VALS = dict() # dictionary of values mapped to qa_tuples (keys) 

for i in range(len(q_and_a)):
	QUESTION_VALS[q_and_a[i]] = VALUES[i]


# inverse, qa tuples (vals) mapped to vals (keys)
# so we can look up questions by numbers ?
VAL_DICT = {val: qa for qa, val in QUESTION_VALS.items()} 

print VAL_DICT.keys()

# Dictionary Class: creates a list of randomly selected
# categories and their questions? Now idk if I need this...
# 	should this just get like 100 categories or something?
class Dictionary(object):

	def __init__(self, total_cats=False):

		if total_cats:
			self.cat_num = total_cats
		else:
			self.cat_num = MAX_CATS

		self.cat_list =  list(self.get_category_list()) # makes set a list


	def get_category_list(self):
		# returns list of randomly chosen categories from library
		temp_list = set([]) # makes sure they're only unique

		while len(temp_list) < self.cat_num:
			temp_list.add(CATEGORIES[randint(0, len(CATEGORIES)-1)])

		return temp_list


	def get_random_category(self):
		# returns random category
		return CATEGORIES[randint(0, len(CATEGORIES)-1)]


	def get_cat_questions(self, cat=False):
		if cat:
			category = cat
		else:
			category = self.get_random_category()

		return CAT_DICT.get(category)



def category_list(num_cats=False):
	# returns a list of randomly chosen categories from all categories
	cat_list = set([]) # 'set' makes sure we only have unique values
	if not num_cats:
		num_cats = MAX_CATS

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
# TESTING

# for n in range(1, 6):
# 	print "QA TUPLE:"
# 	qa = q_and_a[randint(0, len(q_and_a)-1)]
# 	print qa
# 	print "VALUE: "
# 	print val_dict.get(qa)

# rand_cat = random_category() # picks a random category

# print "Category: " + rand_cat 
# print random_question(rand_cat)

# print len(cat_dict["HISTORY"])
# print random_question("HISTORY")
# print len(cat_dict["HISTORY"])