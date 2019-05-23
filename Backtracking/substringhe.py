def stringa2(n):
    """
        ---------------------------------------------
        IMPLEMENTAZIONE CON "PROGRAMMAZIONE DINAMICA"
        ---------------------------------------------
        Stampa tutte le str ternarie in cui non compare '02' or '20'
        O(n)
    """
    t = [[0 for __ in range(n+1)] for _ in range(3)]
    for j in range(n+1):
        for i in range(3):
            if j == 0: t[i][j] = 0
            if j == 1: t[i][j] = 1
            else: t[i][j] = t[1][j-1] + (0 if i==0 else t[2][j-1]) + (t[0][j-1] if i<2 else 0)
    return t[0][n]+t[1][n]+t[2][n]

def stringa(n, i=0, sol=[]):
    """
        --------------------------------
        IMPLEMENTAZIONE CON BACKTRACKING
        --------------------------------
        Stampa tutte le str ternarie in cui non compare '02' or '20'
        O(n*S(n))
    """
    tot=0
    if i == n: return 1
    for x in {'0','1','2'}:
        
        if i>0 and ((sol[-1] == '0' and x == '2') or (sol[-1] == '2' and x == '0')): continue
        sol.append(x)
        tot+=stringa(n, i+1, sol)
        sol.pop()
    return tot

    
if __name__ == "__main__":
    import sys
    if len(sys.argv)>2: 
        if sys.argv[2] == '-d': print(stringa2(int(sys.argv[1])))
        elif sys.argv[2] == '-b': print(stringa(int(sys.argv[1])))
        