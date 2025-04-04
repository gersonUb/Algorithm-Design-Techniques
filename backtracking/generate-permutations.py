def generate_permutation(n, choose, subset, acc):
    if len(subset) == n:
        acc[0] += 1
        print(subset, acc[0]) 
        return
    
    for i in range(1, n + 1):
        if choose[i - 1]:
            continue
        subset.append(i)
        choose[i - 1] = True  
        generate_permutation(n, choose, subset, acc)
        choose[i - 1] = False
        subset.pop() 

acc = [0]
generate_permutation(4, [False, False, False, False], [], acc)