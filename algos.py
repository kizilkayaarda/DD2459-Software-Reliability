def binarySearch(arr, key):
    l = 0
    r = len(arr) - 1
    
    while True:
        mid = (l + r) // 2
        
        if arr[mid] > key:
            r = mid - 1
        else:
            l = mid + 1

        if arr[mid] == key or l > r:
            break

    if arr[mid] == key:
        return mid
    return -1

def insertionSort(arr):

    for  i in range(1, len(arr)):
        nextItem = arr[i]
        loc = i

        while loc > 0 and arr[loc - 1] > nextItem:
            arr[loc] = arr[loc - 1]
            loc -= 1

        arr[loc] = nextItem
    
    return arr

def isMember(arr, key):
    insertionSort(arr)
    loc = binarySearch(arr, key)
    return loc != -1 






