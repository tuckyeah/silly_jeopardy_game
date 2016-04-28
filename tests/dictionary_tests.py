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


def test_value_dictionary():
	pass

def test_random_question():
	pass
	