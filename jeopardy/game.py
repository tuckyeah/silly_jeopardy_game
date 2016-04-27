import dictionary
from random import randint
from sys import exit


class Question(object):

	def __init__(self, cat, qa):
		self.cat = cat
		self.q = qa[0] 
		self.ans = qa[1].upper()

	def check_ans(self, guess):
		# returns boolean
		return guess.upper() == self.ans



class Game(object):
	# the Game object should: 
	#	generate a list of categories and ask the player to pick one
	#	return a random question from that category and remove it from
	# 		that category's question list
	# 	keep track of the category list - if a cat has no more questions
	# 		remove it from the cat list and don't offer it anymore
	#	keep track of questions asked? instead of popping them?

	def __init__(self):
		self.max_cats = 5
		self.cat_list = list(dictionary.category_list(self.max_cats))
		self.questions_asked = []
		self.empty_categories = []
		

	def list_categories(self):
		# prints full category list for this game

		for i in range(len(self.cat_list)):
			print str(i+1) +": " + self.cat_list[i]


	def pick_category(self):
		# asks player to pick a category, returns chosen category
		print "Your category choices are: \n"
		self.list_categories()
		print "\n"
		choice = raw_input("CATEGORY (1-5): ")

		return self.cat_list[int(choice)-1]


	def gen_rand_question(self, cat):
		# get a random question from the cat's questions
		# and pop it, so it's not there anymore

		cat_questions = dictionary.CAT_DICT.get(cat)

		if len(cat_questions) > 1:
			ques = cat_questions.pop(randint(0, len(cat_questions)-1))
		else:
			ques = cat_questions.pop(0)
			self.remove_empty_cats(cat)

		return ques


	def remove_empty_cats(self, cat):
		self.cat_list.pop(self.cat_list.index(cat))


	def new_question(self):
		#generates new question object from chosen category
		cat = self.pick_category()
		qa_tuple = self.gen_rand_question(cat)

		return Question(cat, qa_tuple)


	def ask_question(self):
		question = self.new_question()

		# prints out question
		print "Okay PLAYER, the category is: \n"
		print "%s\n" % question.cat
		print "-" * 10
		print "CLUE:"
		print "-" * 10
		print question.q
		print "-" * 10
		print "(answer: %s )" % question.ans
		print "-" * 10
		guess = raw_input(" WHO/WHAT IS: ")


		return question.check_ans(guess.upper())


class Player(object):

	def __init__(self, name):
		self.name = name
		self.rounds_played = 0
		self.score = 0



# GETTER FUNCTIONS


# get input from dictionary.py

def get_question(cat): 
	# gets random question() from dictionary.py
	return dictionary.random_question(cat)

def get_rand_category(): 
	# gets random_category() from dictionary.py
	return dictionary.random_category()


def get_cat_list():
	# gets a list of categories
	return dictionary.category_list()


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
	cat = pick_category()
	qa_pair = get_question(cat)

	return Question(cat, qa_pair)


while True:
	
	play = Game()
	
	while len(play.cat_list) > 0:

		if not play.ask_question():
			print "Oh no! That doesn't appear to the be the correct answer."
			break

		if not play_again():
			print "Goodbye"
			exit(0)



# OKAY, LET'S PLAY


# ask the user for their input
# if their answer matches the right answer,
# tell them they're right and ask another question
# if they get it wrong
# tell them they're wrong and ask them if they want to play again



# while True:

# 	question = new_question() # make a Question	
# 	question.ask_question() # ... and ask it

# 	guess = get_player_guess()

# 	if not question.check_ans(guess):
# 		print "Oh no! That doesn't appear to be the correct answer."

# 		if not play_again():
# 			print "Goodbye"
# 			exit(0)

# 	print """

# Great work! Okay, next question... 

# 	"""










