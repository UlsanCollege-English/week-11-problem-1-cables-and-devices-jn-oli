def build_graph(edges, directed=False):
    """Builds adjacency list as a dict: node -> list of neighbors.
       Keeps duplicates. Supports directed/undirected graphs.
    """
    g = {}

    for u, v in edges:
        # ensure u exists
        if u not in g:
            g[u] = []
        g[u].append(v)

        if not directed:
            # undirected: add reverse direction
            if v not in g:
                g[v] = []
            g[v].append(u)
        else:
            # directed: only add reverse if it appears as origin later
            if v not in g:
                g[v] = []

    return g


def degree_dict(g):
    """Return dict: node -> degree (length of neighbor list)."""
    return {u: len(g[u]) for u in g}
