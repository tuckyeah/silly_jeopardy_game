import re

STOP_WORDS = ["THE", "A", "AN"]

regex_parens = re.compile(r'\((\w+)\)\s*(\w*)') # matches any text in and outside of parens

# so, to get just the values from inside the parentheticals this is what we want to do

matches = regex_parens.search("(lou) gehrig")

matches.group(1) # gives us 'lou'
matches.group(2) # gives us 'gehrig'

# matches.group() gives us '(lou) gehrig'

string_result = " ".join([matches.group(1), matches.group(2)])
# gives us 'lou gehrig'