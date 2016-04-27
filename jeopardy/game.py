import dictionary
from random import randint

class Question(object):

	def __init__(self):
		self.cat = get_category()
		self.q = ""
		self.ans = ""


def get_question(cat): # gets random question() from dictionary.py
	return dictionary.random_question(cat)

def get_category(): # gets random_category() from dictionary.py
	return dictionary.random_category()

def ask_question():
	qa_pair = 
	

def return_category(cat):
	return cat



cat = get_category()
qa_pair = get_question(cat)

question = Question(cat, qa_pair)

print "Category: " 
print question.cat
print "Question: " 
print question.q
print "Answer: " + question.a 
