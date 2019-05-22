def sorgentiDAG(T):
    nodi = set(T.keys())
    for adjList in T.values():
        for nodo in adjList:
            if nodo in nodi:
                nodi.remove(nodo)
    return nodi

def getGrafoNonDiretto(T):
    T1 = {i:[] for i in T}
    for k, v in T.items():
        T1[k].extend(v)
        for n in v:
            T1[n].append(k)
    return T1


def trovaRadice(T):
    def dfs(T,G, curr, Root, costoDaRadice=0):
        #aggiungo il nodo corrente ai visitati
        visited.add(curr)
        #per ogni nodo adiacente al corrente nel grafo non diretto
        for child in G[curr]:
            #se non è stato visitato
            if child not in visited:
                #setta la distanza del figlio
                dist[child] = dist[curr]+ (1 if child in T[curr] else -1) + costoDaRadice
                #se è una radice ed è più conveniente
                if child in possibiliRadici and dist[child] < 0:
                    Root = child
                    costoDaRadice = dist[child]*(-1)
                Root, costoDaRadice = dfs(T,G, child, Root, costoDaRadice)
        return Root, costoDaRadice

    #le possibili radici sono i nodi sorgenti di un DAG
    possibiliRadici = sorgentiDAG(T)
    #scelgo una radice a caso
    r1 = possibiliRadici.pop()
    #inizializzo con un set vuoto l'insieme dei nodi visitati
    visited = set()

    dist = {r1:0}
    return dfs(T, getGrafoNonDiretto(T), r1, r1, 0)[0]


#------- TESTS -------
if __name__ == "__main__":
    A2 = {
        0:[1,2,3],
        1:[],
        2:[],
        3:[],
        4:[1],
        5:[4],
        6:[5],
        7:[6],
    }



    A1 = {
        0:[1],
        1:[],
        2:[1],
        3:[2,4],
        4:[],
        5:[4,6],
        6:[],
        7:[6],
    }


    A3 = {
        0:[],
        1:[0]
    }

    A4 = {
        1:[2,3],
        2:[4],
        3:[],
        4:[5],
        5:[6],
        6:[],
        7:[3],
        8:[7],
    }

    A5 = {
        1:[2,3,9],
        2:[4],
        3:[],
        4:[5],
        5:[6],
        6:[],
        7:[3],
        8:[7],
        9:[10],
        10:[],
        11:[10],
        12:[11]
    }

    tests = [A1,A2,A3,A4,A5]

    # print(trovaRadice(A5))

    for t in tests:
        print("----------")
        print("Test su: ", t)
        print("La radice conveniente e'",trovaRadice(t))
        print("----------")