def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Function Call
result = binary_search(arr, x)

# Output
print(result) 