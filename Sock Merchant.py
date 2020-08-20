# %%
from collections import defaultdict

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    """[Find how many pairs can be made from a list of integers]

    Args:
        n ([int]): [nymber of socks]
        ar ([list of integers]): [inventory of socks]

    Returns:
        [type]: [description]
    """
    sock_dict = defaultdict(int)

    # For each sock (val) in the sock inventory add one to the value count creating a dictionary
    for val in ar:
        sock_dict[val] += 1
    print(sock_dict)

    # initialize counter
    cnt = 0

    # Divide item count by 2 discarding remainders to get number of pairs possible
    for pair in sock_dict.values():
        cnt += pair // 2
        
    # Return the answer
    return cnt

