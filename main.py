# 1)
def bounded_subsets(arr, limit):   # limited by sum powerset generator, binary method
    filtered = [i for i in arr if i <= limit]   # filter the arr for relevant items
    size = len(filtered)
    sets = pow(size, 2)
    yield []               # because limit >= 0 and len(arr) >= 0
    for i in range(sets):  # for every possible subset
        sum = 0
        res = []
        yflag = True
        for j in range(size):  # extract items corresponding the binary of i
            if i & (1 << j) > 0 or size == 1:
                sum += filtered[j]
                if sum > limit:    # check that the set sum doesn't go over the limit
                    yflag = False
                    break
                else:
                    res.append(filtered[j])
        if yflag and len(res) > 0:   # if the subset is valid yield
            yield res


for i in bounded_subsets([],0):
    print(i)   # prints []
print('----')
for i in bounded_subsets([1],1):
    print(i)   # prints [] [1]
print('----')
for i in bounded_subsets([1,2,3],0):
    print(i)   # prints []
print('----')
for i in bounded_subsets([1,2,3],1):
    print(i)   # prints [] [1]
print('----')
for i in bounded_subsets([1,2,3],4):
    print(i)   # prints [] [1] [2] [1,2] [3] [1,3]
print('----')



# 2)



# 3)
# https://www.codingame.com/training/hard/the-labyrinth