def copy(t):
    t2 = []
    for i in range(len(t)):
        t2.append([el for el in t[i]])
    return t2
            
def largest_square(sq):
    """
    Data una matrice quadrata binaria M di dimensione n*n 
    si vuole sapere qual è il massimo m per cui la matrice 
    quadrata m * m di soli uni risulta sottomatrice di M.
    """
    t = copy(sq)
    n = len(t)
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            if t[i][j] != 0:
                t[i][j] = 1+min(t[i+1][j], t[i][j+1], t[i+1][j+1])
    l = t[0][0]
    for i in range(n):
        for j in range(n):
            if t[i][j]>l:
                l = t[i][j]
    return l, t

sq = [
        [1,0,1,1,1], 
        [1,1,1,1,1],
        [1,1,1,0,1],
        [1,1,1,1,1],
        [1,1,0,1,1]
    ]

if __name__ == "__main__":
    from pprint import pprint as pp
    l, t = largest_square(sq)
    print("Il quadrato più grande è ",l,"*",l)
    pp(largest_square(sq))