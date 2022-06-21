import collections

def find_duplicate(arr,n):
    map = collections.Counter(arr)
    for k in map:
        if map[k]>1:
            return k


arr = [2,3,4,1,4]
n = len(arr)
print(find_duplicate(arr,n))