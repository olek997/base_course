def ab(a, b):
    return abs(a * b)

arr_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr_b = [4, 7, 34, 76, -34, 0]

print(list(map (ab, arr_a, arr_b)))