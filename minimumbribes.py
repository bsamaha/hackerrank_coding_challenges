# input 1 is number of test cases
# input 2 is n spaced integers 1,n+1


def minimumBribes(q):
    # create an array of n spaced integers
    try:
        arr = list(range(q))
    except:
        arr1 = list(range(len(q)))
    # if an index has moved up more than two spaces it is too chaotic
    for i in arr:
        if arr.index(i) < arr[i] - 2:
            print('Too chaotic')
        else:
            print(arr)