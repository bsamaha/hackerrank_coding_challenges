
# %%
def leftRotateme(d,a):
    # Create the list
    arr = list(range(1,a+1))
    # create temp array to store values
    temp = arr[:d]
    # Cut out d-elements from list
    arr = arr[d:]
    # Add d elements to end of list
    arr.extend(temp)

    return arr

        



# %%
leftRotateme(2,5)
# %%
