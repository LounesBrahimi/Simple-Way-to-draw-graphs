import networkx as nx
import matplotlib.pyplot as plt

g=nx.read_edgelist('file.txt', create_using=nx.Graph(), nodetype=int)

nx.draw(g)

plt.show()