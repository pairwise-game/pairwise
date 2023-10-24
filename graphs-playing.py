import proj_plane as PP
import networkx as nx

D = PP.make_deck(3, one_index=True, cardnum=True)
D = PP.format_deck(D, 'nums', True)
PP.file_output(D, 'test.txt')
print(D)

# a_list = """
# 1 4 5 10 12
# 2 3 5 9 13
# 3 1 2 3 4
# 4 2 7 10 13
# 5 2 6 9 12
# 6 1 11 12 13
# 7 4 7 9 11
# 8 3 6 10 11
# 9 1 8 9 10
# 10 3 7 8 12
# 11 6 8 13 13
# """
# H = nx.read_adjlist(a_list)

G = nx.read_adjlist('test.txt')
# G = nx.path_graph(4)
# nx.write_adjlist(G, "test.adjlist")

import matplotlib.pyplot as plt
# nx.draw_shell(G, nlist=(['1'], ['2','5','8','11'], ['3','4'], ['6','7'],['9','10'], ['12', '13']), with_labels=True)
# nx.draw_circular(G, with_labels=True)
pos = nx.spiral_layout(G)
nx.draw(G, pos=pos, with_labels = True)
plt.show()