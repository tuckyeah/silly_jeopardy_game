from game import *
import dictionary

# OKAY, LET'S PLAY


# ask the user for their input
# if their answer matches the right answer,
# tell them they're right and ask another question
# if they get it wrong
# tell them they're wrong and ask them if they want to play again

# TODO:
# give list of five categories
# pick a category
# ask random question from that chosen category


while True:

	question = new_question() # make a Question	
	question.ask_question() # ... and ask it

	guess = get_player_guess()

	if not question.check_ans(guess):
		print "Oh no! That doesn't appear to be the correct answer."

		if not play_again():
			print "Goodbye"
			exit(0)

	print """

Great work! Okay, next question... 

	"""