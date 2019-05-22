from math import pow
def sottoseq(n):
    s = set()
    strN = str(n)
    s.add(int(strN[0]+strN[1]+strN[2]+strN[3]+strN[4]+strN[5]))
    s.add(int(strN[1]+strN[2]+strN[3]+strN[4]+strN[5]+strN[6]))
    s.add(int(strN[0]+strN[2]+strN[3]+strN[4]+strN[5]+strN[6]))
    s.add(int(strN[0]+strN[1]+strN[3]+strN[4]+strN[5]+strN[6]))
    s.add(int(strN[0]+strN[1]+strN[2]+strN[4]+strN[5]+strN[6]))
    s.add(int(strN[0]+strN[1]+strN[2]+strN[3]+strN[5]+strN[6]))
    
    return s


def es4(L, a, b):
    """
    Abbiamo una lista L contente n interi ciascuno composto da esattamente 
    7 cifre decimali.
    Diciamo che c'e' una trasformazione elementare dall'intero 
    x all'intero y se i due interi appartengono alla lista 
    e differiscono esattamente in una cifra.
    Data la lista L e due suoi numeri a e b, vogliamo sapere 
    se e' possibile da a ottenere b tramite una sequenza
    di trasformazioni elementari.

    progettare un algoritmo che prende come parametri L, a e b e
    risolve il problema in tempo O(n).
    Motivare la correttezza e la complessità' dell'algoritmo proposto
    e infine fornire il codice python della funzione corrispondente 
    all'algoritmo.

    Ad esempio per 
    L=[1022250, 1022201, 1023450, 1025250, 1025550, 2023450, 2023550,2025550]

    - per a=1025550 e b= 1023450 la risposta e' True
    - per a=1022250 e b=1022201 la risposta e' False
    """
    
    #per ogni num ottengo le sottoseq.
    
    diz = dict()
    sottoseqN = dict()
    for n in L:
        sottoseqN[n] = sottoseq(n)
        for s in sottoseqN[n]:
            if s not in diz:
                diz[s] = {n}
            else:
                diz[s].add(n)
            
    g = dict()
    for n in L:
        for s in sottoseqN[n]:
            if len(diz[s])>1:
                if n not in g:
                    g[n] = diz[s]
                else:
                    g[n].union(diz[s])
                if n in g[n]:
                    g[n].difference_update({n})
    print(sottoseqN[1025250].intersection(sottoseqN[1022250]))
    print(g)
            

    

L=  [1022250, 1022201, 1023450, 1025250, 1025550, 2023450, 2023550,2025550]
print(es4(L,1,2))


