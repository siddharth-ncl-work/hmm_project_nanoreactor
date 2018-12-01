import networkx as nx
import numpy as np
import math 
from input.molecules.bond_lengths import bl
from input.molecules.molecule_class import molecule_class

atoms=-1
cords=-1
file_name='/home/vanka/tamal/prebiotic_synthesis/sugar_synthesis_HCNH2O_0.75timestep_after1000000.md/scr/coors.xyz'
frame_adj_mat=-1
frame_labels=-1
frame_graph=-1

def init():
  global frame_adj_mat
  global frame_labels
  frame_labels={i:cords[i][0] for i in range(atoms)}
  frame_label_file=open('output/frame_labels.csv','w')
  for i in range(atoms):
    frame_label_file.write(str(i)+' '+cords[i][0]+'\n')
  frame_adj_mat=np.zeros((atoms,atoms))
  
def readFile(file,frame):
  global atoms
  global cords
  is_found=-1
  _atoms=atoms=int(rfile.readline())
  while _atoms!='':
    atoms=int(_atoms)
    f=int(file.readline().split()[1])
    print f
    if f==frame:
      cords=[file.readline().split() for i in range(atoms)]
      for i in range(atoms):
        cords[i][1:]=map(float,cords[i][1:])
      is_found=1
      init()
      break
    else:
      for i in range(atoms):file.readline()
    _atoms=rfile.readline()
  return is_found

def getAdjMat():
  global frame_adj_mat
  global cords
  for i in range(atoms):
    for j in range(i+1,atoms):
      d=getDist(cords[i][1:],cords[j][1:])
      if d<=bl[cords[i][0]][cords[j][0]]:  #can use atomic radii
        frame_adj_mat[i][j]=frame_adj_mat[j][i]=1
        print '%s %s %d %d %f'%(cords[i][0],cords[j][0],i,j,d)
 
def getGraph():
  global frame_graph
  global frame_labels
  frame_graph=nx.from_numpy_matrix(frame_adj_mat)
  nx.set_node_attributes(frame_graph,'element',frame_labels)

def getDist(v1,v2):
  d=0.0
  for i in range(len(v1)):
    d+=(v2[i]-v1[i])**2
  return math.sqrt(d)

def writeCsvFile(wfile):  #add frame number
  global frame_adj_mat
  wfile.write('elements,')
  for i in range(atoms):
    if i!=atoms-1:
      wfile.write(str(i)+',')
    else:
      wfile.write(str(i)+'\n')
  for row in range(atoms):
    wfile.write(str(row)+','+cords[row][0]+',')
    for col in range(atoms):
      if col!=atoms-1:
        wfile.write(str(frame_adj_mat[row][col])+',')
      else:
        wfile.write(str(frame_adj_mat[row][col])+'\n')

##test_write_frame_cords
def writeTestFile():
  test_file=open('test.xyz','w')
  test_file.write(str(atoms)+'\n\n')
  for i in cords:
    for j in i:
      test_file.write(str(j)+'   ')
    test_file.write('\n')

def _main_(file,frame,molecule=-2):
  global frame_graph
  if readFile(file,frame)==1:print 'Successfully Found Frame '+str(frame)
  else:
    print 'Error:Frame %d is not present'%frame
    return -1
  getAdjMat()
  getGraph()
  #molecule.mol_graph
  print frame_graph.nodes()
  print frame_graph.edges()
  print nx.get_node_attributes(frame_graph,'element')
  wfile=open('output/frame_adjancency_matrix.csv','w')
  writeCsvFile(wfile)
  

rfile=open(file_name,'r')
_main_(frame=10,file=rfile)

#mol1=molecule_class('input/molecules/hcn.xyz')
#writeTestFile()
