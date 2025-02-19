import pytest

from jgrapht import create_graph
import jgrapht.algorithms.matching as matching
import jgrapht.algorithms.partition as partition
import jgrapht.generators as generators


def test_bipartite_max_cardinality():
    g = create_graph(directed=False, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)

    for _ in range(0, 6):
        g.add_vertex()

    e03 = g.add_edge(0, 3)
    e13 = g.add_edge(1, 3)
    g.add_edge(2, 3)
    e14 = g.add_edge(1, 4)
    e25 = g.add_edge(2, 5)
    g.set_edge_weight(e13, 15.0)

    weight, m = matching.bipartite_max_cardinality(g)
    assert weight == 3.0
    assert set(m) == set([e03, e14, e25])

    weight, m = matching.bipartite_max_weight(g)
    assert weight == 16.0
    assert set(m) == set([e13, e25])


def test_bipartite_perfect_min_weight():
    bg = create_graph(directed=False, allowing_self_loops=False, allowing_multiple_edges=False, weighted=True)
    generators.complete_bipartite_graph(bg, 10, 10)
    _, part1, part2 = partition.bipartite_partitions(bg)
    weight, _ = matching.bipartite_perfect_min_weight(bg, part1, part2)

    assert weight == 10.0

