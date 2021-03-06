def heap_sort(arr):
    def heapify(a):
        i = int(len(arr) / 2) - 1
        while i >= 0:
            sink(arr, i, len(arr) - 1)
            i -= 1

    def sink(a, i, n):
        while 2 * i <= n:
            j = 2 * i
            if j + 1 <= n and arr[j] < arr[j + 1]:
                j += 1
            if arr[i] >= arr[j]:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i = j

    heapify(arr)
    end = len(arr) - 1

    while end > 0:
        arr[0], arr[end] = arr[end], arr[0]
        sink(arr, 0, end-1)
        end -= 1


if __name__ == '__main__':
    arr = [4, 7, 10, 2, 0, 5, -9, 13]
    heap_sort(arr)
    print(arr)
    assert arr == [-9, 0, 2, 4, 5, 7, 10, 13]
