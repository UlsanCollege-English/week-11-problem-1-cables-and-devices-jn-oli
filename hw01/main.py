# python
def build_graph(edges, directed=False):
    """Build adjacency list as a dict: node -> list of neighbors.
       Keeps duplicates. Supports directed/undirected graphs.
    """
    g = {}
    if edges is None:
        return g

    for edge in edges:
        try:
            u, v = edge
        except Exception:
            raise TypeError("edges must be an iterable of 2-tuples (u, v)")

        g.setdefault(u, []).append(v)

        if not directed:
            # undirected: add reverse direction
            g.setdefault(v, []).append(u)
        else:
            # directed: ensure target node exists in dict
            g.setdefault(v, [])

    return g


def degree_dict(g):
    """Return dict: node -> degree (length of neighbor list)."""
    if g is None:
        return {}
    return {u: len(neighbors) for u, neighbors in g.items()}