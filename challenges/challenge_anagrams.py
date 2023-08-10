def quicksort(string):
    if len(string) <= 1:
        return string
    else:
        pivot = string[0]
        left = [x for x in string[1:] if x < pivot]
        right = [x for x in string[1:] if x >= pivot]
        return (quicksort(left) + [pivot] + quicksort(right))


def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return ('', '', False)

    first_sorted = ''.join(quicksort(first_string.lower()))
    second_sorted = ''.join(quicksort(second_string.lower()))
    return (first_sorted, second_sorted, first_sorted == second_sorted)
