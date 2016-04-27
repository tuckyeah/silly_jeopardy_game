import dictionary
from random import randint
from sys import exit


class Question(object):

	def __init__(self, cat, qa):
		self.cat = cat
		self.q = qa[0] 
		self.ans = qa[1].upper()

	def ask_question(self):
		# prints out question
		print "Okay PLAYER, the category is: \n"
		print "%s\n" % self.cat
		print "-" * 10
		print "QUESTION:"
		print "-" * 10
		print self.q
		print "-" * 10
		print "(answer: %s )" % self.ans

	def check_ans(self, guess):
		# returns boolean
		return guess.upper() == self.ans



# GETTER FUNCTIONS


# get input from dictionary.py

def get_question(cat): 
	# gets random question() from dictionary.py
	return dictionary.random_question(cat)

def get_category(): 
	# gets random_category() from dictionary.py
	return dictionary.random_category()

	
# get player input

def get_player_guess():
	guess = raw_input("   WHAT/WHO IS >>> ")
	return guess

def play_again():
	ask = raw_input("Play again? (y/n): ")
	if "y" in ask:
		return True
	else:
		return False


# GAME STUFF

def new_question():
	# makes a new Question object
	cat = get_category()
	qa_pair = get_question(cat)

	return Question(cat, qa_pair)


# OKAY, LET'S PLAY


# ask the user for their input
# if their answer matches the right answer,
# tell them they're right and ask another question
# if they get it wrong
# tell them they're wrong and ask them if they want to play again

PLAYED = 0

while True:

	question = new_question() # make a Question	
	question.ask_question() # ... and ask it

	guess = get_player_guess()

	if not question.check_ans(guess):
		print "Oh no!"

		if not play_again():
			print "Goodbye"
			exit(0)

	print """

Great work! Okay, next question... 

	"""












