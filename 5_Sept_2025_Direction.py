def min_changes_to_return(s):
    if len(s) % 2 != 0:
        return -1

    from collections import Counter
    cnt = Counter(s)
    
    dx = abs(cnt['E'] - cnt['W'])
    dy = abs(cnt['N'] - cnt['S'])

    if (dx + dy) % 2 != 0:
        return -1

    return (dx + dy) // 2
#this code defines a function to calculate the minimum number of changes needed to return to the starting point in a grid, 
#given a string of directions. It uses the Counter class from the collections module to count occurrences of each direction
#and then calculates the differences in counts for opposite directions. 
#If the total difference is odd, it returns -1, indicating that it's impossible to return to the starting point; 
#otherwise, it returns half of the total difference.