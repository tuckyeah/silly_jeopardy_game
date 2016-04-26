import dictionary
from random import randint

def get_question():
	question = dictionary.QUESTIONS[randint(0, len(dictionary.QUESTIONS)-1)]
	print question

get_question()