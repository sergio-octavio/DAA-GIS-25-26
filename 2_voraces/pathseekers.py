import heapq

def solve_mission(n, g, target):
    # dist[i] almacenará la distancia mínima encontrada hasta ahora al nodo i
    dist = [10**15] * (n + 1)
    # parent[i] permite reconstruir el camino más corto
    parent = [-1] * (n + 1)
    # visited[i] indica si el nodo i ya ha sido finalizado (extraído de la cola)
    visited = [False] * (n + 1)
    
    dist[0] = 0
    pq = [(0, 0)] # (distancia, nodo)
    
    reached_target = False
    while pq:
        d, u = heapq.heappop(pq)
        
        # Si ya hemos encontrado un camino más corto, ignoramos esta entrada
        if d > dist[u]:
            continue
            
        # Marcamos como activado/visitado. Según la estrategia voraz, solo los nodos
        # finalizados hasta este punto pueden desbloquear tramos.
        visited[u] = True
        
        if u == target:
            reached_target = True
            break
            
        for v, w, p in g[u]:
            # Un tramo solo es atravesable si su restricción p ya fue visitada o no existe
            if p == -1 or (p <= n and visited[p]):
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
    
    if not reached_target or dist[target] >= 10**15:
        print("MISION FALLIDA")
    else:
        path = []
        curr = target
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        # Formato de salida: nodos - coste
        print(f"{' '.join(map(str, path))} - {dist[target]}")

def main():
    # Lectura de N y M
    try:
        line = input().strip().split()
        if not line: return
        n, m = map(int, line)
    except (EOFError, ValueError):
        return

    # Construcción del grafo. Cada arista guarda (destino, peso, restricción)
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            o, d, w, p = map(int, input().strip().split())
            g[o].append((d, w, p))
        except (EOFError, ValueError):
            break

    # Lectura del número de destinos K
    try:
        k_line = input().strip()
        if not k_line: return
        k = int(k_line)
    except (EOFError, ValueError):
        return

    # Procesamiento de cada destino como una misión independiente
    for _ in range(k):
        try:
            target_line = input().strip()
            if not target_line: break
            target = int(target_line)
            solve_mission(n, g, target)
        except (EOFError, ValueError):
            break

main()
