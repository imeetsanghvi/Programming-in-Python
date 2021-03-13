import numpy as np

def initialize():
  graph=np.array([
  [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,0  ,0  ,1],
  [0  ,0  ,0  ,0  ,0  ,1  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,1  ,0  ,0],
  [0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,1  ,0  ,0  ,0  ,0  ,0],
  [0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
  [0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
  [0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0],
  [0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
  [0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0],
  [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0],
  [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0],
  [0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
  [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
  [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,1],
  [0  ,1  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0],
  [0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,1  ,0  ,0  ,0  ,0],
  [1  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,1  ,0  ,0  ,0  ,0  ,0],
  [1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
  [0  ,1  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0],
  [0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0],
  [1  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,1  ,0  ,0  ,0  ,0  ,0  ,0  ,0],
  ])
  heuristic = np.array([366, 0, 160, 242, 161, 176, 77,151,226,244,241,234,380,100,193,253,329,80,199,374])
  return graph,heuristic

def func_start_node():
  snode = int(input('Enter a start node value in between 0-19'))
  snode = snode
  if snode<0 or snode>19:
    print('ERROR ==> Please Enter A Start node Vlaue in between the given range only!!!\n')
    snode = func_start_node()
  return snode

def find_succ(starting_node,graph,heuristic,o_list,c_list):
  print('finding successor function here______________')
  for i in range(0,len(graph[starting_node])):
    if graph[starting_node][i] == 1 and c_list != starting_node:
        o_list.append(i)
        print('Append Function:',o_list)

  return o_list,starting_node,heuristic,c_list

def del_parent(starting_node,graph,heuristic,o_list,c_list):
  o_list.remove(starting_node)
  c_list.append(starting_node)
  return o_list,starting_node,heuristic,c_list

def find_mini(starting_node,graph,heuristic,o_list,c_list):
  print('\n\nfinding minimum function here______________')
  #function to find minimum heuristic value of elements in open list
  print('\n\nOPEN==>',type(o_list),o_list)
  print('CLOSED==>',type(c_list),c_list)
#starting_node = min(heuristic[o_list])
#starting_node = np.argmin(starting_node)
  #for i in range(0,len(o_list)):
  temp = min(heuristic[o_list])
  f=heuristic.tolist().index(temp)
  print(f)
  starting_node = f
  print('next Starting node willl be==> ',starting_node)
  return o_list,starting_node,heuristic,c_list

def gbfs(starting_node,graph,heuristic,o_list,c_list):
  #this is main gbfs function   
  if heuristic[starting_node] == 0:
    print('\n\n***************Goal Node FOund***********') 
    print('\nPath is:==>',c_list)
    print('Goal Node is:',starting_node)
    #checking if the start node selectedis goal node or not
    return starting_node,graph,heuristic,o_list,c_list
  else:
    print('\nNot a Goal Node')
    o_list,starting_node,heuristic,c_list = find_succ(starting_node,graph,heuristic,o_list,c_list)
    
    o_list,starting_node,heuristic,c_list = del_parent(starting_node,graph,heuristic,o_list,c_list)

    o_list,starting_node,heuristic,c_list = find_mini(starting_node,graph,heuristic,o_list,c_list)

    starting_node,graph,heuristic,o_list,c_list = gbfs(starting_node,graph,heuristic,o_list,c_list)
    #we need to find successors of the selected node appends successor to the open list
    #finding the minimum/cheapest value in open list
    #starting_node,graph,heuristic,o_list,c_list = gbfs(starting_node,graph,heuristic,o_list,c_list)
  
#main here
o_list = []
c_list = []
graph,heuristic = initialize()   #this is for static grpah initialization process:
starting_node = func_start_node() #getting usser input for starting node
o_list.append(starting_node) #just to stay safe from none-error
starting_node,graph,heuristic,o_list,c_list = gbfs(starting_node,graph,heuristic,o_list,c_list)