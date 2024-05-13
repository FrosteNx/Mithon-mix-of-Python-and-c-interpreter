def even_split(table):
    
    prefix_sum = 0
    total_sum = sum(table)

    for idx in range(len(table)):
        prefix_sum += table[idx]
        total_sum -= table[idx]

        if prefix_sum == total_sum:
            return idx
    
    return -1

print(even_split([1,2,2,4,1]))