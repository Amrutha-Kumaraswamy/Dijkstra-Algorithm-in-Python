#!/usr/bin/env python
from collections import defaultdict, deque



class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)
    #target = open('Output.dat', 'w+')
    target.write(str(visited[destination]));
    target.write('\n')
    #print visited[destination]
    #print list(full_path)
    
    for element in full_path: 
        parts = element.strip("[").split(',')
        #print parts
	for s in parts:
    		#print ', '.join(str(item) for item in s)
		target.write(str(''.join(str(item) for item in s)));
		target.write('\n')
    #print 'FFFF'
    target.write('FFFF')
    target.write('\n')
    

    return visited[destination], list(full_path)

if __name__ == '__main__':
    graph = Graph()
    f=open("Graph.dat","r")
    x=f.readlines()
    count=len(x)-1
    #print count
    for node in range(1, count+1):
        graph.add_node(str(node))
    myarray=[None]*count
    #print myarray
    count_num=0
    for i in range(0, count):
        myarray[i]=x[i+1]
	#print myarray[i]
    for i in range(1, count+1):
	index=1
	arr=myarray[i-1]
	for j in range(1,count+1):
		count_num=count_num+1
		#print index
		if index>(len(arr)-1):
			break
		#print arr[index]
		if arr[index]=='0':
			#print 'in if continue'
			if index <17:
			    index=index+2
			else:
			    index=index+3
			continue
		#print index
		#print str(i), str(j),int(arr[index])
		graph.add_edge(str(i), str(j),int(arr[index]))
		if index <17:
                    index=index+2
                else:
                    index=index+3

    fp=open("Input.dat","r")
    target = open('Output.dat', 'w+'); 
    a1=fp.readlines()
    in_len=((len(a1)-1)/3)
    #print in_len
    #a=[None]*len(a1)
    #print a
    l=0
    for k in range(1,in_len+1):
	in1=a1[l]
	in2=a1[l+1]	
	#print str(in1),str(in2)
	l=l+3	
    	#shortest_path(graph, str(in1[0]), str(in2[0])) # output: (25, ['1', '2', '4']
	shortest_path(graph,str(filter(str.isdigit,in1)),str(filter(str.isdigit,in2)))
	#target=open("Output.dat",'w+')
	#target.write(shortest_path(graph, str(in1[0]), str(in2[0])))
    target.write('0')
	#target.close() 
