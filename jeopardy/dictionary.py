import csv
from random import randint

ifile = open('small_jeopardy.csv', 'rb')
reader = csv.reader(ifile)
listData = list(reader)

QUESTIONS = []
ANSWERS = []
CATEGORIES = []


for row in listData:
	if listData.index(row) == 0:
		continue

	QUESTIONS.append(listData[listData.index(row)][2]) # all questions
	ANSWERS.append(listData[listData.index(row)][3]) # all answers
	CATEGORIES.append(listData[listData.index(row)][0]) # all categories


cat_dict = dict() # dictionary of categories and q/a tuples
q_and_a = zip(QUESTIONS, ANSWERS) # creates tuples of questions and answers

for i in range(len(CATEGORIES)):
	if CATEGORIES[i] in cat_dict: # if cat already exists, add qa tuple
		cat_dict[CATEGORIES[i]].append(q_and_a[i])
	else:
		cat_dict[CATEGORIES[i]] = [q_and_a[i]] # create new category entry

rand_cat = CATEGORIES[randint(0, len(CATEGORIES)-1)]

cat_questions = cat_dict.get(rand_cat)
print rand_cat
print cat_questions

if len(cat_questions) > 1:
	print cat_questions[randint(0, len(cat_questions)-1)]


# tbh idk if i need this anymore?
questions_dict = {} # a dictionary of all our question/answer pairs

for question, answer in q_and_a:
	questions_dict[question] = answer

