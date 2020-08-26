# constraints = 0 < n < 10**5

def fizzBuzz(n):
    # n is a set of numbers from 1 to n so we must create the list
    lst = list(range(1,n+1))
    # now loop through that lest to check for conditionals
    for i in lst:
    # First check if case is 0 since 0 divided by anything is 0
        if i == 0:
            print(i)
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)    