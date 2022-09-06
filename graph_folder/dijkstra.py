from priority_queue_folder.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


def dijkstra_short_path(g, src):
    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}
    for v in g.vertices():
        if v in src:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator[v] = pq.add(d[v], v)
        while not pq.is_empty():
            key, u = pq.remove_min()
            cloud[u] = key
            del pqlocator[u]
            for e in g.incident_edges(u):  # outgoing edges (u,v)
                v = e.opposite(u)
                if v not in cloud:
                    wgt = e.element()
                    if d[u] + wgt < d[v]:  # better path to v?
                        d[v] = d[u] + wgt  # update the distance
                        pq.update(pqlocator[v], d[v], v)  # update the pq entry
        return cloud


