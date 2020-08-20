
# %%
sentence = 'aWESOME is cODING'

def reverse_words_order_and_swap_cases(sentence):
    # Fix order of words
    sentence = sentence.split(' ')
    sentence = sentence[::-1]

    # put back to string and swapcase
    string = ' '.join(map(str,sentence))
        

    return (string.swapcase())

# %%
reverse_words_order_and_swap_cases(sentence)

# %%
