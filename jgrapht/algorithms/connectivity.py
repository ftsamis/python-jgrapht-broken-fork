from .. import backend
from .._internals._collections import (
    _JGraphTIntegerSetIterator
)

def is_weakly_connected(graph):
    """Computes weakly connected components in a directed graph or 
       connected components in an undirected graph. 
  
    This is a simple BFS based implementation.

    Running time :math:`\mathcal{O}(n+m)`.

    :param graph: the graph.
    :returns: a tuple containing a boolean value on whether the graph is connected
      and an iterator over all connected components. Each component is represented
      as a vertex set
    """
    connected, sets = backend.jgrapht_connectivity_weak_exec_bfs(graph.handle)
    return connected, _JGraphTIntegerSetIterator(sets)


def is_strongly_connected_gabow(graph):
    """Computes strongly connected components in a directed graph. 
  
    This is Cheriyan-Mehlhorn/Gabow's algorithm and can be found at: 
  
      * Gabow, Harold N. "Path-Based Depth-First Search for Strong and Biconnected
        Components; CU-CS-890-99." (1999).

    Running time :math:`\mathcal{O}(n+m)`.

    :param graph: the graph. Must be directed
    :returns: a tuple containing a boolean value on whether the graph is strongly connected
      and an iterator over all connected components. Each component is represented as a 
      vertex set
    """
    connected, sets = backend.jgrapht_connectivity_strong_exec_gabow(graph.handle)
    return connected, _JGraphTIntegerSetIterator(sets)


def is_strongly_connected_kosaraju(graph):
    """Computes strongly connected components in a directed graph. 

    This is an implementation based on:

      * Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction
        to algorithms. MIT press.
    
    Running time :math:`\mathcal{O}(n+m)`.

    :param graph: the graph. Must be directed
    :returns: a tuple containing a boolean value on whether the graph is strongly connected
      and an iterator over all connected components. Each component is represented as a 
      vertex set
    """
    connected, sets = backend.jgrapht_connectivity_strong_exec_kosaraju(graph.handle)
    return connected, _JGraphTIntegerSetIterator(sets)  


def is_connected(graph): 
    """Compute connected components of a graph.

    For directed graphs this method computed strongly connected components.

    :param graph: the graph. Must be directed
    :returns: a tuple containing a boolean value on whether the graph is connected
      and an iterator over all connected components. Each component is represented as a 
      vertex set
    """
    if graph.type.directed:
        return is_strongly_connected_kosaraju(graph)
    else:
        return is_weakly_connected(graph)

