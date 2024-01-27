def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    closest_index = None

    while low <= high:
        mid = (high + low) // 2
        iterations += 1

        if arr[mid] < x:
            low = mid + 1
        else:
            closest_index = mid
            high = mid - 1

    if closest_index is not None:
        return iterations, arr[closest_index]
    else:
        return iterations, "not found"


def main():
    arr = [1.2, 1.3, 2.42, 3.11, 4.4, 4.51, 7.8, 11.2]
    x = 13
    result = binary_search(arr, x)
    print(f"Iterations: {result[0]}")
    print(f"Value: {result[1]}")

    if result[1] is not None:
        print("Element found in array")
    else:
        print("Element is not present in array")


if __name__ == "__main__":
    main()
