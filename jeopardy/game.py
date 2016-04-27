import dictionary
from random import randint

class Question(object):

	def __init__(self, cat, qa):
		self.cat = cat
		self.q = qa[0] 
		self.ans = qa[1]

	def ask_question(self):
		print "Okay PLAYER, the category is: \n"
		print "%s\n" % self.cat
		print "-" * 10
		print "QUESTION:"
		print "-" * 10
		print self.q
		print "-" * 10

def get_question(cat): # gets random question() from dictionary.py
	return dictionary.random_question(cat)

def get_category(): # gets random_category() from dictionary.py
	return dictionary.random_category()
	

cat = get_category()
qa_pair = get_question(cat)

question = Question(cat, qa_pair)

question.ask_question()
