def bicolora(G):
    """
    Progettare un algoritmo python che prende come
    parametro un grafo non diretto G di N nodi ed M archi
    rappresentato tramite dizionario, e in tempo O(n+m)
    restituisce una lista con la bicolorazione del grafo
    se il grafo è bicolorabile, restituisce una lista
    vuota altrimenti.
    """




def isBicolorabile(graph, node, visited=set()):
    visited.add(node)
    if isLoopNode(graph, node, node,0, set(), dict())[1]%2:
        return False
    for child in graph[node]:
        if child not in visited:
            if not isBicolorabile(graph, child, visited):
                return False
    return True

def isLoopNode(graph, node, start, count=0, visited=set(), gc=dict()):
    """Dice se da quel nodo parte un loop"""
    visited.add(node)
    gc[node] = count
    for child in graph[node]:
        if child not in visited:
            f, c = isLoopNode(graph, child, start, count+1, visited, gc) 
            if f:
                return True, c
            print("now in", node)
        elif child == start and gc[node] != 1:
            return True, gc[node]+1
        # print("child",child, node)
    return False, 0






    

a = {
    1:[2],
    2:[1,3,5,8],
    3:[4],
    4:[3],
    5:[6,2],
    6:[5,7],
    7:[6,8,9,10],
    8:[7,9,2],
    9:[7,8],
    10:[7]
}

b = {
    1:[2],
    2:[1,3],
    3:[2]
}

c = {
    1: [2,7,8],
    2: [1,8,4],
    3: [7],
    4: [2,6],
    5: [7],
    6: [4,8],
    7: [1,3,5,8],
    8: [1,2,6,7],
}

print(isBicolorabile(a,1))
    
