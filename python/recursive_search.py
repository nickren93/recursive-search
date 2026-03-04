
def recursiveSearch(arr, target):

    if len(arr) == 0:
        return False
    elif arr[-1] == target:
        return True        
    
    arr.pop()
    return recursiveSearch(arr, target)


'''
standard answer:

def recursiveSearch(arr, target, i=0):

    if i == len(arr):
        return False

    if arr[i] == target:
        return True

    return recursiveSearch(arr, target, i + 1)
'''