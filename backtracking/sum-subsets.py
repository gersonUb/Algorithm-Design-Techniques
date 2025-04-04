def exist_sum_subsets(subset, k, i):
    print(subset,k,i)
    if k == 0:
        return True
    if k < 0 or i >= len(subset):
        return False
    else:
        without_current = exist_sum_subsets(subset, k, i + 1)
        with_current = exist_sum_subsets(subset, k - subset[i], i + 1)
    
        return without_current or with_current

result = exist_sum_subsets([6, 12, 6], 12, 0)
print(result)

