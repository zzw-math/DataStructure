from graph_folder.graph_examples import graph_from_edgelist
from graph_folder.shortest_paths import shortest_path_lengths
from graph_folder.shortest_paths import shortest_path_tree
from graph_folder.mst import MST_Prim
from graph_folder.mst import MST_Kruskal


def graph8():
    edge_list = (('a', 'b', 7), ('a', 'd', 5), ('b', 'c', 8),
                 ('b', 'd', 9), ('b', 'e', 7), ('c', 'e', 5),
                 ('d', 'e', 15), ('d', 'f', 6), ('e', 'f', 8),
                 ('e', 'g', 9), ('f', 'g', 11))
    return graph_from_edgelist(edge_list, False)


g = graph8()


def find_vertex(str):
    for v in g.vertices():
        if v.element() == str:
            return v


src = find_vertex('a')
print(src)
cloud = shortest_path_lengths(g, src)
print(cloud)

tree = shortest_path_tree(g, src, cloud)
print(tree)

tree = MST_Prim(g)
print(tree)

tree = MST_Kruskal(g)
print(tree)
