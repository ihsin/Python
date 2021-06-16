import re

# MATCHES:


def patternMatchedInText(text, pattern):
    if re.search(patterns, text):
        return True
    else:
        return False

#a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
patterns = '[a-zA-Z0-9.]'
print(patternMatchedInText('#@$%***', patterns)) #False
print(patternMatchedInText('AWD', patterns)) #True

#a string that has an a followed by zero or more b's
patterns = 'ab*'
print(patternMatchedInText('#dsa', patterns)) #True
print(patternMatchedInText('#@$%***', patterns)) #False

#a string that has an a followed by one or more b's
patterns = 'ab+'
print(patternMatchedInText('#@$%a', patterns)) #False
print(patternMatchedInText('#@$%abb', patterns)) #True

#a string that has an a followed by zero or one 'b'
patterns = 'ab?'
print(patternMatchedInText('#@$%a', patterns)) #True
print(patternMatchedInText('#@$%abb', patterns)) #True

#a string that has an a followed by three 'b'
patterns = 'ab{3}?'
print(patternMatchedInText('#@$%a', patterns)) #False
print(patternMatchedInText('#@$%abbb', patterns)) #True

#a string that has an a followed by two to three 'b'.
patterns = 'ab{2,3}'
print(patternMatchedInText('#@$%abbb', patterns)) #True
print(patternMatchedInText('#@$%abb', patterns)) #True

#sequences of one upper case letter followed by lower case letters.
patterns = '[A-Z]+[a-z]+'
print(patternMatchedInText('Aaa', patterns)) #True
print(patternMatchedInText('AAAsacas', patterns)) #True

