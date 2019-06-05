from find_path import inside
from pprint import pprint as pp
def es(m, k):
    n = len(m)
    t = [[[0 for _ in range(k+1)] for j in range(n)] for i in range(n)]
    t2 = {(i,j):set() for j in range(n) for i in range(n)}
    t[0][0][m[0][0]] += 1
    t2[0,0].add(m[0][0])
    for i in range(n):
        for j in range(n):
            if i==j==0: continue
            if inside(i-1, j, m):
                for kp in t2[i-1,j]:
                    if kp+m[i][j] <=k:
                        t[i][j][kp+m[i][j]] += 1
                        t2[i,j].add(kp+m[i][j])
            if inside(i, j-1, m):
                for kp in t2[i,j-1]:
                    if kp+m[i][j] <=k:
                        t[i][j][kp+m[i][j]] += 1
                        t2[i,j].add(kp+m[i][j])
    return t[n-1][n-1][k]
            

if __name__ == "__main__" :
    A = [
        [0,0,0,0,0,1],
        [0,1,0,1,1,1],
        [0,0,0,1,0,1],
        [0,1,0,0,0,0],
        [0,0,0,0,1,0],
        [1,1,0,1,0,0]
    ]

    B = [
        [0,0,0,0,0,0],
        [0,1,1,1,0,0],
        [0,1,0,0,0,0],
        [0,1,0,1,1,1],
        [0,1,0,0,0,0],
        [0,0,0,0,1,0]
    ]

    C = [
        [1,2,3],
        [4,6,5],
        [3,2,1]
    ]

    print(es(C,12))
