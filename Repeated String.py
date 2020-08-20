    """
    Given a string s = 'abcac' or whatever...
    and n being the number of times repeated n = 10
    thus making s = abcacabcac
    return number of a's in string (4)



    take string s and repeat its characters n times
    """



# %%
import math
import os
import random
import re
import sys

# %%
# Complete the repeatedString function below.
def repeatedString(s, n):
    # Count number of occurences in string
    # Multiply by the number of wholly repeated strings
    # Then find how far up the string the remainder goes and count a's to that point
    print(s.count('a') * (n//len(s)) + s[:n % len(s)].count('a'))

# %%
string = ''
s = 'ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt'
n = 685118368975
repeatedString(s,n)
