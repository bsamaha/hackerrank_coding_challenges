"""Pseudo:
can only skip 1 at a time
shortest route is to constantly skip a cloud 

start at 0
if index[n+2] == 0 then jump to that index
else jump to index[n+1] 
"""

# %%

c = [0,0,1,0,0,1,0]

def jumpingOnClouds(c):
    # Initialize empty list to dump path in here
    total_cloud = len(c)
    counter = 0
    result = 0

    while counter <= total_cloud:
        if counter + 2 < total_cloud and c[counter+2] == 0:
            counter = counter + 2
            result += 1
            print('skip',counter,result)

        elif counter + 1 < total_cloud and c[counter+1] == 0:
            counter += 1
            result += 1
            print('next',counter,result)
        else:
            counter += 1
    return result





# %%
jumpingOnClouds(c)
# %%
