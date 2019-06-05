"""
Dato n e un alfabeto abc stampare tutte le stringhe che rispettino il vincolo:
numero di a minore uguale di b minore uguale di c

per n=1 la stringa è una sola ['c'] .
n=2 ['cc', 'bc', 'cb', 'cc' ]
"""

def sottoseq(n, i=0, sol=[]):
    if i==n: print(sol)
    else:
        for c in 'abc':
            if i==0 or (i>0 and (c >= sol[-1])):
                sol.append(c)
                sottoseq(n, i+1, sol)
                sol.pop()
sottoseq(2)