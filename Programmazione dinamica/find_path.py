def inside(i,j, m):
    return 0<=i<len(m) and 0<=j<len(m[0])
def es(m):
    from pprint import pprint as pp
    """
    Data una matrice binaria di dimensioni n*n vogliamo verificare se nella matrice è
    possibile raggiungere la cella in basso a destra partendo da quella in alto a sinistra 
    senza mai toccare celle che contengono il numero 1.
    Si tenga conto che dalla generica cella (i,j) ci si pu`o spostare solo nella cella in basso 
    (vale a dire la cella (i + 1, j)) o nella cella a destra (vale a dire la cella (i, j + 1)).
    """

    n = len(m)
    m = [[0 if x==1 else 1 for x in m[i]] for i in range(n)] #matrice negata
    pp(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] == 0: continue
            if inside(i+1, j, m) and m[i+1][j] != 0:
                m[i+1][j] = max(m[i][j]+1, m[i+1][j])
            if inside(i, j+1, m) and m[i][j+1] != 0:
                m[i][j+1] = max(m[i][j]+1, m[i][j+1])
    pp(m)
    return m[n-1][n-1] == ((n-1)*2)+1

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

    print(es(A))
    print(es(B))