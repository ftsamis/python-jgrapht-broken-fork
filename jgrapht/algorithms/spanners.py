from .. import backend
from ..exceptions import UnsupportedOperationError
from .._errors import raise_status
from .._wrappers import JGraphTLongSet


def _mst_alg(name, graph):
    alg_method_name = 'jgrapht_mst_exec_' + name

    try:
        alg_method = getattr(backend, alg_method_name)
    except AttributeError:
        raise UnsupportedOperationError('Algorithm {} not supported.'.format(name))

    err, weight, mst_handle = alg_method(graph.handle)
    if err:
        raise_status()

    return weight, JGraphTLongSet(mst_handle)


def kruskal(graph):
    r"""Compute the minimum spanning tree using `Kruskal's algorithm <https://en.wikipedia.org/wiki/Kruskal's_algorithm>`_.

    
    If the given graph is connected it computes the minimum spanning tree, otherwise it computes
    the minimum spanning forest. The algorithm runs in time :math:`\mathcal{O}(m \log m)` or
    :math:`\mathcal{O}(m \log n)` in case multiple edges are not allowed and thus :math:`m \le n^2`.
    Here :math:`n` is the number of vertices and :math:`m` the number of edges of the graph.

    :param graph: The input graph
    :returns: A tuple (weight, mst) 
    """
    return _mst_alg('kruskal', graph)

def prim(graph):
    r"""Compute the minimum spanning tree using `Prim's algorithm <https://en.wikipedia.org/wiki/Prim's_algorithm>`_.

    The algorithm was developed by Czech mathematician V. Jarník and later independently by computer scientist
    Robert C. Prim and rediscovered by E. Dijkstra. This implementation uses a Fibonacci Heap in order to 
    achieve a running time of :math:`\mathcal{O}(m+n\log n)` where :math:`n` is the number of vertices and 
    :math:`m` the number of edges of the graph.

    :param graph: The input graph
    :returns: A tuple (weight, mst) 
    """
    return _mst_alg('prim', graph)


def boruvka(graph):
    r"""Compute the minimum spanning tree using `Borůvka's algorithm <https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm>`_.

    This implementation uses a union-find data structure (with union by rank and path compression
    heuristic) in order to track components. In graphs where edges have identical weights, edges with
    equal weights are ordered lexicographically. The running time is :math:`\mathcal{O}((m+n) \log n)` under the
    assumption that the union-find uses path-compression.
    Here :math:`n` is the number of vertices and :math:`m` the number of edges of the graph.

    :param graph: The input graph
    :returns: A tuple (weight, mst) 
    """
    return _mst_alg('boruvka', graph)
    
def multiplicative_greedy(graph, k):
    r"""Greedy algorithm for :math:`(2k-1)`-multiplicative spanner construction (for any integer :math:`k \ge 1`.
 
    The spanner is guaranteed to contain :math:`\mathcal{O}(n^{1+1/k})` edges and the shortest path
    distance between any two vertices in the spanner is at most :math:`2k-1` times the corresponding
    shortest path distance in the original graph. Here :math:`n` denotes the number of vertices of
    the graph.
 
    The algorithm is described in: Althoefer, Das, Dobkin, Joseph, Soares. 
    `On Sparse Spanners of Weighted Graphs <https://doi.org/10.1007/BF02189308>`_. Discrete
    Computational Geometry 9(1):81-100, 1993.

    If the graph is unweighted the algorithm runs in :math:`\mathcal{O}(m n^{1+1/k})` time. Setting
    :math:`k` to infinity will result in a slow version of Kruskal's algorithm where cycle detection
    is performed by a BFS computation. In such a case use the implementation of Kruskal with
    union-find. Here :math:`n` and :math:`m` are the number of vertices and edges of the graph
    respectively.
 
    If the graph is weighted the algorithm runs in :math:`\mathcal{O}(m (n^{1+1/k} + n \log n))` time
    by using Dijkstra's algorithm. Edge weights must be non-negative.

    :param graph: The input graph
    :param k: integer
    :returns: tuple of the form (weight, spanner_edges)
    """
    err, weight, spanner = backend.jgrapht_spanner_exec_greedy_multiplicative(graph.handle, k)
    if err:
        raise_status()
    return weight, JGraphTLongSet(spanner)

