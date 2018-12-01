import networkx as nx
import graphviz
from networkx.drawing.nx_agraph import to_agraph,graphviz_layout

H=nx.DiGraph()
nodes=[(13000,[48,56,28,6]),
       (7514,[0,65,2,37,18,19,20,56,69]),(7541,[8,6]),(7514,[16,48,58]),(7514,[27,28,29]),
       (3251,[0,65,2]),(3251,[18,19,20]),(3251,[56,55,54,3]),(3251,[48,50,37]),
      (7503,[8,6,3,5,22])]
#_nodes=[(c+i[0],{'atm_nos':i[1]}) for c,i in enumerate(nodes)]
_nodes=['frame='+str(i[0])+'\n'+str(i[1]) for c,i in enumerate(nodes)]
H.add_nodes_from(_nodes)
'''
H.add_edges_from([(_nodes[0][0],_nodes[1][0]),(_nodes[0][0],_nodes[2][0]),(_nodes[0][0],_nodes[3][0]),(_nodes[0][0],_nodes[4][0]),
                 (_nodes[1][0],_nodes[5][0]),(_nodes[1][0],_nodes[6][0]),(_nodes[1][0],_nodes[7][0]),(_nodes[1][0],_nodes[8][0]),
                 (_nodes[2][0],_nodes[9][0])])
'''

H.add_edges_from([(_nodes[0],_nodes[1]),(_nodes[0],_nodes[2]),(_nodes[0],_nodes[3]),(_nodes[0],_nodes[4]),
                 (_nodes[1],_nodes[5]),(_nodes[1],_nodes[6]),(_nodes[1],_nodes[7]),(_nodes[1],_nodes[8]),
                 (_nodes[2],_nodes[9])])

nx.draw(H,pos=graphviz_layout(H,prog='dot'),with_labels=True)
aH=to_agraph(H)
U=graphviz.Source(aH)
