def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2    #나눗셈 후 정수 부분만 반환
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr



list = [2,5,1,8,3,9,6]
print(merge_sort(list))



