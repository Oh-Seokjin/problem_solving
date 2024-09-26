def bs(arr, target, s, e):
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            e = mid-1
        else:
            s = mid+1
    return None


arr = [1, 3, 5, 7, 9, 19, 11, 15, 17, 13]
target = 4
#####
arr.sort()

result = bs(arr, 5, 0, 9)
print(result)