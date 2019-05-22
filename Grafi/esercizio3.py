"""
Bisogna formare dei gruppi di lavoro partizionando un insieme di n studenti 
i cui nomi vanno da 0 a n-1.
I gruppi li forma il docente che ad  ogni studente da la possibilità'
di segnalare un eventuale studente con cui 
non ha nessuna intenzione di formare gruppo. 
Queste informazioni vengono codificate in una 
lista L di n elementi dove L[i] e' lo studente 
segnalato da i (nel caso in cui lo studente  i 
non abbia segnalato nessuno e va d'accordo con tutti allora  L[i]=-1).

Progettare un algoritmo di complessità' O(n)  
che prende come parametro  la lista L e restituisce
il numero minimo di gruppi che 
il docente e' costretto a formare per accontentare 
le richieste di tutti gli studenti. 
Motivare la correttezza e la complessità' del vostro
algoritmo e se possibile scrivetene il codice python.

Ad esempio:
- per la classe di 5 studenti e L=[10103] la funzione 
restituisce 2 (una possibile divisioni in gruppi e' {0,2,4}, {1,3})

- per la classe di 5 studenti e L=[1,2,3,4,0] la funzione 
restituisce 3 (una possibile divisione in gruppi e' {1,4}, {3}, e {0,2})


"""

def groups(L):
    gruppi = dict()
    for i, s in enumerate(L):
        print(s, i)
        if s not in gruppi:
            gruppi[s] = {i}
        else: gruppi[s].add(i)
    print(gruppi)

def g2(L):
    studenti = {x for x in range(len(L))}
    g = [set(studenti) for _ in range(len(L))]
    for i, s in enumerate(L):
        print(g,"aa")
        if s in g[i]:
            g[i].remove(s)
        if i in g[s]:
            g[s].remove(i)
    print(g)



print(groups([1,0,1,0,3]))
