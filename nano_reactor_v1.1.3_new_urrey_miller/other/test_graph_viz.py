import networkx as nx
import graphviz
from networkx.drawing.nx_agraph import to_agraph,graphviz_layout

G=nx.read_gexf("/home/vanka/siddharth/tamal/nano_reactor_v1.1.2/output/imp_results/tracking_results/path_hcho_31_05_2018_without_filter_v1.0.6_with_bug.gexf")
aG=to_agraph(G)
U=graphviz.Source(aG,filename='path_hcho_31_05_2018_without_filter_v1.0.6_with_bug',format='png')
U.render(cleanup=False)
