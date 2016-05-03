from nose.tools import *
from jeopardy.dictionary import *

def test_category_list():
	assert_equal(len(category_list()), 5)
	result = category_list()
	assert_equal(len(result), 5)

	result = category_list(3)
	assert_equal(len(result), 3)

	for i in result:
		assert(type(i) is str and len(i) > 0)

def test_random_category():
	one_list = random_category()
	other_list = random_category()

	assert(one_list != other_list)
	assert(len(one_list) > 0)

VALUES = [2000, 3200, 400, 200, 1200, 800, 1600, 600, 1000]

def test_value_dictionary():
	keys = return_keys()
	assert_equal(len(keys), 9)

	rand_val = keys[randint(0, len(keys)-1)]

	assert_equal(type(convert_value(rand_val)), int) # tests that convert works
	
	num = convert_value(rand_val)
	assert(num in VALUES)

	rand_q = VAL_DICT[rand_val]
	
	assert_equal(type(rand_q), tuple)
	assert(rand_q[0] in QUESTIONS)
	assert(rand_q[1] in ANSWERS)

