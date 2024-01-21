def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0

    while low <= high:
        mid = (high + low) // 2
        iterations += 1

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return iterations, mid

    default = -1 if low >= len(arr) else low

    return iterations, default


def main():
    arr = [1.2, 1.3, 2.42, 3.11, 4.4, 4.51, 7.8, 11.2]
    x = 12
    result = binary_search(arr, x)
    print(f"Iterations: {result[0]}")
    print(f"Index: {result[1]}")

    if result[1] != -1:
        print(f"Value: {arr[result[1]]}")
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()
