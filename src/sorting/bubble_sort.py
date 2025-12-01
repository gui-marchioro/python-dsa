def  bubble_sort(arr: list[int]) -> list[int]:
    arr_len = len(arr)
    if arr_len < 2:
        return arr
    has_swiped = True
    while has_swiped:
        l, r = 0, 1
        has_swiped = False
        while r < arr_len:
            if arr[l] > arr[r]:
                has_swiped = True
                arr[l], arr[r] = arr[r], arr[l]
            r += 1
            l += 1
    return arr


if __name__ == "__main__":
    array = [4, 2, 5, 1]
    array = bubble_sort(array)
    print(array)
