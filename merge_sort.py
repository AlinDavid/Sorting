
def merge_sort(given_list):
    if len(given_list) > 1:
        mid = len(given_list) // 2
        left = given_list[:mid]
        right = given_list[mid:]

        mergeSort(left)
        mergeSort(right)

        a, b, c = 0, 0, 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                given_list[c] = left[a]
                a = a + 1
            else:
                given_list[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            given_list[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            given_list[c] = right[b]
            b = b + 1
            c = c + 1

    return list
