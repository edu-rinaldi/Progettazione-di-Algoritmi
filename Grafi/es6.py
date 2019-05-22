

def es6(m):
    """
    Abbiamo un sistema di m equazioni in n incognite.
    Le incognite sono x0,x1,...xn-1. Le disequazioni sono tutte del tipo xi < xj oppure xi> xj (con 0<=i != j<n).

    Progettare un algoritmo che prende come parametro l'insieme I  delle m disequazioni e in tempo O(n+m) 
    determina se il sistema ha soluzioni intere o meno.
    Ad esempio:
    1)  per il sistema contenente le tre disequazioni
    x1<x2
    x2>x3
    x0>x2
    la risposta deve essere True (una soluzione e' xo=10, x1=3, x2=8 e x3=7)

    2) per il sistema contenente le tre disequazioni
    x1>x2
    x2>x3
    x1<x3
    la risposta deve essere False.

    Motivare bene la correttezza e la complessità' del vostro algoritmo.

    Implementare infine una funzione python che prende  l'insieme  delle disequazioni e in tempo O(n+m) 
    restituisce una lista vuota se il sistema non ammette soluzione altrimenti restituisce una lista L 
    rappresentate la soluzione. 
    
    Nell'insieme di input   ciascuna disequazione  e'  rappresentata da una tripla del tipo  (i, '<' ,j) o ( i,'>',j) 
    ad indicare xi <xj o xi>xj.
    La lista con la soluzione conterrà' n locazioni ed L[i] conterrà' il valore di xi nella soluzione.

    Ad esempio:
    1) la lista del primo sistema sara':
    I={(1, '<' , 2), (2, '>', 3), (0,'>', 2) } e un possibile output  sara' L=[10, 3, 8, 7]
    2) l'insieme del secondo sistema sara' :
    I={(1, '>' , 2), (2, '>', 0), (1,'>', 0) } e l'unico possibile output  sara' L=[ ]
    """

    #costruisco il grafo
    g = costruisciGrafo(m)
    #faccio il sort topologico
    sortTop = sortTopologico(g)
    #mi creo una pool di numeri da pescare per la lista L
    numberPool = list(range(len(sortTop)))
    #inizializzo la lista L con tutti 0
    l = [0 for _ in sortTop]
    #per ogni numero nel sort topologico prendo il massimo nel pool (che sarà in ultima posizione)
    for num in sortTop:
        l[num] = numberPool.pop(len(numberPool)-1)
    print(l)
    return l

def costruisciGrafo(m):
    
    #inizializzo un dizionario vuoto
    g = dict()

    #per ogni disequazione creo un grafo dove ogni nodo è un Xi
    #un arco tra Xi e Xj esiste se e solo se Xi > Xj
    for e in m:
        if e[1] == '>':
            if e[0] in g:
                g[e[0]].append(e[2])
            else:
                g[e[0]] = [e[2]]

            if e[2] not in g:
                g[e[2]] = []
            
        else:
            if e[2] in g:
                g[e[2]].append(e[0])
            else:
                g[e[2]] = [e[0]]

            if e[0] not in g:
                g[e[0]] = []
    return g

def gradoNodo(G):
    """funzione che dato un grafo G restituisce un dizionario con il grado di ogni nodo"""

    #inizializzo un dizionario che mi tiene il conteggio del grado di ogni nodo
    grado = {k: 0 for k in G}
    
    #per ogni arco prendo il nodo in cui entro e gli incremento il contatore
    for arco in G.values():
        for nodo in arco:
            grado[nodo] += 1
    return grado

def sortTopologico(G):

    #calcolo il grado di ogni nodo
    grado = gradoNodo(G)

    #prendo tutte le sorgenti, ovvero tutti i nodi con grado 0 (nessun arco entrante)
    sorgenti = {x for x in G if grado[x] == 0}

    #inizializzo una lista vuota
    st = []

    #finchè ci sono sorgenti
    while len(sorgenti)>0:
        #prendi una sorgente e mettila nella lista del sort
        s = sorgenti.pop()
        st.append(s)
        for y in G[s]:
            #diminuisci il grado di tutti i nodi a cui è connesso
            grado[y] -= 1
            if grado[y] == 0:
                sorgenti.add(y)
    #se i nodi nel sort sono tanti quanti quelli in G allora abbiamo un DAG
    if len(st) == len(G):
        return st
    return []

es6({(1, '<' , 2), (2, '>', 3), (0,'>', 2) })

es6({(1, '>' , 2), (2, '>', 3), (1,'<', 3) })

