def count_shops(N, k):
    result = []

    for i in range(N):
        visited = set()
        current = i
        while current not in visited:
            visited.add(current)
            current = k[current]
        result.append(len(visited))
    
    return result
# This code defines a function to count the number of unique shops visited
# starting from each shop in a list, where `k` represents the next shop to visit from the current one.
# It uses a set to track visited shops and returns a list of counts for each starting shop.
