def shout():
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = 'congratulations' + '!!!'
    print(shout_word)

shout()

# Define shout with the parameter, word
def shout(word):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')

# Functions that return a single value
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'
    return(shout_word)

yell = shout('congratulations')

print(yell)

# Write functions with multiple parameters
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    shout1 = word1 + '!!!'
    shout2 = word2 + '!!!'
    new_shout = shout1 + shout2

    return new_shout

yell = shout('congratulations', 'you')

print(yell)

# Introduction about tuples
# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums
print(nums)

# Construct even_nums
even_nums = (2, 4, 6)
print(even_nums)