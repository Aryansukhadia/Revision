def index_pairs_with_diff(arr, k):
    n = len(arr)
    result = [0] * n
    value_to_indices = {}

    for i, val in enumerate(arr):
        if val in value_to_indices:
            value_to_indices[val].append(i)
        else:
            value_to_indices[val] = [i]

    for i in range(n):
        target1 = arr[i] + k
        target2 = arr[i] - k

        found = False
        for target in (target1, target2):
            if target in value_to_indices:
                for j in value_to_indices[target]:
                    if j != i:
                        found = True
                        break
            if found:
                break
        result[i] = 1 if found else 0

    return result

# this code defines a function to find pairs of indices in an array where the absolute difference 
# between the values at those indices is equal to a given value k.    

