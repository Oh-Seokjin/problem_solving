k = 3
arr1 = [1, 2, 5, 4, 3]
arr2 = [5, 5, 6, 6, 5]
#####

arr1.sort()
arr2.sort(reverse=True)

for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break

print(sum(arr1))