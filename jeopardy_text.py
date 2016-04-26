import csv, random

ifile = open('small_jeopardy.csv', 'rb')
reader = csv.reader(ifile)
listData = list(reader)

QUESTIONS = []
ANSWERS = []

for row in listData:
	if listData.index(row) == 0:
		continue

	QUESTIONS.append(listData[listData.index(row)][2])
	ANSWERS.append(listData[listData.index(row)][3])

print QUESTIONS

q_and_a = zip(QUESTIONS, ANSWERS)
questions_dict = {} # a dictionary of all our question/answer pairs

for question, answer in q_and_a:
	questions_dict[question] = answer


def pick_question():
	question = 
