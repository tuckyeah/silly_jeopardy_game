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

dict_obj = Dictionary()

def test_dict_obj_size():
	assert_equal(dict_obj.num_cats, 5)