# n: the number of steps Gary takes
# s: a string describing his path
# s = [DDUUUUDD] Down a valley of 2 steps, up a mountain of 4 steps, and back to sea level at two steps

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.

# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

# Output: Print a single integer that denotes the number of valleys Gary walked through during his hike.

def countingValleys(n, s):
    """[Count the number of local minima in an area]

    Args:
        n ([int]): [number of steps gary takes]
        s ([str]): [order of direction [UUDD]]

    Returns:
        valleys[int]: [number of local minima found]
    """
    # Establish sea level
    level = 0

    # Establish valley counter
    valleys = 0

    # Iterate through the list of directions
    for letter in s:
        # Add to level if you go up from baseline
        if letter == "U":
            level += 1
            # If you go up 1 step from the bottom you have created another local minima meaning you have a valley
            if level == 0:
                valleys += 1
        # If you don't go up from baseline you go down and you can't count a valley until you go up
        else:
            level -= 1
             
    return valleys
