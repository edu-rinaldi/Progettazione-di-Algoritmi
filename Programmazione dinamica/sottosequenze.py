def sottoseq(x):
    n = len(x)
    t = [[-1 for _ in range(n)] for _ in range(n)]
    t[n-1][n-1] = 1
    for j in range(n-2):
        t[n-1][j] = -1
    
    for i in range(n-2,-1,-1):
        for j in range(n-1,-1,-1):
            if i>j:
                t[i][j] = -1
            if i<j and x[i]<x[j]:
                t[i][j] = t[j][j]
            if i<j and x[i]>=x[j]:
                t[i][j] = 0
            if i==j:
                t[i][j] = max(t[i])+1
    maxindex = 0
    for i in range(1,n-1):
        if t[maxindex][maxindex] < t[i][i]:
            maxindex = i
    val = t[maxindex][maxindex]
    sol = [x[maxindex]]
    while val>1:
        val -= 1
        for j in range(maxindex, n):
            if t[maxindex][j] == val:
                sol.append(x[j])
                maxindex = j
    return sol



from pprint import pprint as pp
seq = [50,4,100,2,48,3,34,30]
seq2 = [50,2,1002,48,3,34,30]
print("Per la sequenza:", seq2,"\nLa soluzione: ", end="")
pp(sottoseq(seq))


