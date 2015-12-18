a = [2, 3, 4, 1, 4, 6, 0]


def quick_sort(arr, left, right):
    if left < right:
        key = arr[left]
        low = left
        high = right
        while low < high:
            while low < high and arr[high] >= key:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < key:
                low += 1
            arr[high] = arr[low]
        arr[low] = key

        quick_sort(arr, left, low - 1)
        quick_sort(arr, low + 1, right)


if __name__ == "__main__":
    quick_sort(a, 0, len(a) - 1)
    print a
