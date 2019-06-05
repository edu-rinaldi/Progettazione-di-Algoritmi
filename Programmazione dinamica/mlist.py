def mio_minimo(l):
    print(l)
    minimo = l[0]
    for el in l:
        if minimo == -1 and el != -1:
            minimo = el
        elif el<minimo and el != -1:
            minimo = el
    return minimo
def find_m_list(m):
    """
    Data una matrice n * m di interi M = [mi,j], una M-lista e' una sequenza (m1,j1,m2,j2 ...mn,jm) 
    tale che 1 <= j1 <= ...jm <= m. Il valore di una M-lista è la somma degli elementi che la compongono.
    Progettare un algoritmo che trova un M-lista di valore minimo in O(n * m).
    """

    N, M = len(m), len(m[0])
    tmp = min(N, M)
    off = 0
    minv = 0
    minr = m[N-1][M-1]
    t = [[-1 for _ in range(M)] for _ in range(N)]
    for i in range(N-1, -1, -1):
        if i<N-1:
            minr = -1
        for j in range(M-off-1, M-tmp-off-1, -1):
            if i == N-1:
                print(minr, m[i][j])
                minr = min(m[i][j], minr)
                t[i][j] = minr
            else:
                if minr == -1:
                    t[i][j] = m[i][j]+t[i+1][j+1]
                    minr = t[i][j]
                else:
                    t[i][j] = min(m[i][j]+t[i+1][j+1], minr)
        off+=1
    import pprint
    pprint.pprint(t)
        

m1 = [
    [3,5,8,1,2],
    [4,9,11,3,1],
    [9,2,7,5,10]
]

find_m_list(m1)