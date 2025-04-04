def generate_subset(n, k, subset):
    if n == k:
        print(subset)
        return
    else:
        generate_subset(n, k+1, subset)
        subset.append(k+1)
        generate_subset(n,k+1,subset)
        subset.pop()

generate_subset(4,0,[])