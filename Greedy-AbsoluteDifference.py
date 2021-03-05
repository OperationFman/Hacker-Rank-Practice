def minimumAbsoluteDifference(arr):
    arr_list = sorted(arr)
    minimum = 99999
    for i in range(1, len(arr)):
        minimum = min(minimum, abs(arr_list[i - 1] - arr_list[i]))
    
    return minimum

list = [3, -7, 0]
minimumAbsoluteDifference(list)