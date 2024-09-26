arr = [("홍길동", 95), ("이순신", 77)]
#####

arr.sort(key=lambda x: x[1])

for elem in arr:
    print(elem[0], end=" ")