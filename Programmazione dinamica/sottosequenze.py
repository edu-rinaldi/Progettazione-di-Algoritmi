def sottoseq(x):
    n = len(x)
    t = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if (i == j == n-1) or (j == n-1): 
                t[i][j] = 1
            elif (j >= i) and (x[j] >= x[j+1]): 
                t[i][j] = t[i][j+1]
            elif (j >= i) and (x[j] < x[j+1]):
                t[i][j] = t[i][j+1]+1
    return t



from pprint import pprint as pp
seq = [50,4,100,2,48,3,34,30]
print("Per la sequenza:\t", seq)
pp(sottoseq(seq))