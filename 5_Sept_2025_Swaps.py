def min_swaps_to_group_k(s, k):
    total_k = s.count(k)
    if total_k <= 1:
        return 0  # Already grouped

    # Count non-Ks in the first window
    window_size = total_k
    current_non_k = sum(1 for i in range(window_size) if s[i] != k)
    min_swaps = current_non_k

    for i in range(1, len(s) - window_size + 1):
        # Slide the window: subtract leftmost, add rightmost
        if s[i - 1] != k:
            current_non_k -= 1
        if s[i + window_size - 1] != k:
            current_non_k += 1
        min_swaps = min(min_swaps, current_non_k)

    return min_swaps

#this code defines a function to calculate the minimum number of swaps 
#needed to group all occurrences of a specific element (k) together in a list.