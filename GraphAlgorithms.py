#!/usr/bin/env python 
#coding=utf-8

def getWeight(V,E,u,v):
	if E.has_key(u):
		for i in E[u]:
			if i[1] is v:
				return i[2]
	return 100000

def BFS(V,E,start):
	color=[-1]*len(V)
	depth=[0]*len(V)
	queue=[]
	queue.append(start)
	color[start]=0
	while len(queue)>0:
		p=queue.pop(0)
		print " "*depth[p],
		print V[p]
		if E.has_key(V[p]):
			for j in E[V[p]]:
				if color[V.index(j[1])]==-1:
					queue.append(V.index(j[1]))
					depth[V.index(j[1])]=depth[p]+1
					color[V.index(j[1])]=0
		color[p]=1
	return depth

time=0

def DFS_start(V,E):
        global time
	color=[-1]*len(V)
	startTime=[0]*len(V)
        finishTime=[0]*len(V)
	for i in V:
		if color[V.index(i)]==-1:
			DFS(V,E,color,startTime,finishTime,i)
	return startTime,finishTime

def DFS(V,E,color,startTime,finishTime,i):
        global time
        time=time+1
	startTime[V.index(i)]=time
	print " "*startTime[V.index(i)],
	print i
	color[V.index(i)]=0
	if E.has_key(i):
		for m in E[i]:
			if color[V.index(m[1])]==-1:
				DFS(V,E,color,startTime,finishTime,m[1])
	color[i]=1	
        time=time+1
        finishTime[V.index(i)]=time


def TopologicalSort(V,E):
    indegree=[0]*len(V)
    visited=[]
    for i in E:
        for j in E[i]:
            indegree[V.index(j[1])]=indegree[V.index(j[1])]+1
    while 0 in indegree:
            pos=indegree.index(0)
            visited.append(V[pos])
            if E.has_key(V[pos]):
                for j in E[V[pos]]:
                    indegree[j[1]]=indegree[j[1]]-1
            indegree[pos]=-1
    if len(visited)<len(V):
        return []
    return visited
                

def TopologicalSort_dfs(V,E):
    indgree=[0]*len(V)
    visited=[]
    color=[0]*len(V)
    for i in E:
        for j in E[i]:
            indgree[V.index(j[1])]=indgree[V.index(j[1])]+1
    if 0 not in indgree:
        return []
    Queue=[]
    for begin in range(0,len(indgree)):
        if indgree[begin]==0:
            Queue.append(begin)
            while len(Queue)>0:
                current=Queue.pop(0)
                flag=False
                if E.has_key(V[current]):
                    for i in E[V[current]]:
                        if color[V.index(i[1])] is not 1:
                            flag=True
                            if color[V.index(i[1])] is not -1:
                                Queue.append(V.index(i[1]))
                                color[V.index(i[1])]=-1
                            break
                if not flag:
                    visited.insert(0,V[current])
                    color[current]=1
                else:
                    Queue.append(V[current])
                    color[current]=-1
    return visited




def Kruskal(V,E):
	visited=[]
	visitedpoints=[]
	notvisited=[]
	for m in E:
		for n in E[m]:
			notvisited.append(n)
	while len(visited)<len(V)-1 and len(notvisited)>0:
		temp=(0,0,65535)
		for j in notvisited:
			if j[2]<temp[2]:
				temp=j
		notvisited.pop(notvisited.index(temp))
                if visitedpoints.count(temp[0])+visitedpoints.count(temp[1])<2:
			visited.append(temp)
                        for i in temp[0],temp[1]:
                            if not i in visitedpoints:
			        visitedpoints.append(i)			
	return visited

def Prim(V,E):
	visited=[]
	visitedpoints=[]
        notvisited=[]
	for m in E:
		for n in E[m]:
			notvisited.append(n)
	while len(visited)<len(V)-1 and len(notvisited)>0:
		temp=(0,0,65535)
		for j in notvisited:
			flag=False
			if len(visited)==0:
				flag=True
			n=visitedpoints.count(j[0])+visitedpoints.count(j[1])
			if n==1:
				flag=True
			if j[2]<temp[2] and flag:
				temp=j
		if temp[2]==65535:
			continue
		visited.append(temp)
                for m in temp[0],temp[1]:
                    if m not in visitedpoints:
                        visitedpoints.append(m)
		notvisited.pop(notvisited.index(temp))
	return visited
			
	
	
def Dijikstra(V,E,begin):
	visited=[False]*len(V)
	length=[0]*len(V)
	path=[0]*len(V)
	for i in range(0,len(V)):
		visited.append(False)
	for j in range(0,len(V)):
		if j is not begin:
			length[j]=getWeight(V,E,V[begin],V[j])
			path[j]=begin
	while False in visited:
		min=100000
		pos=-1
		for j in range(0,len(V)):
			if not visited[j]:
				if length[j]<min:
					pos=j
					min=length[j]
		visited[pos]=True
		for m in range(0,len(V)):
			if not visited[m]:
				if length[pos]+getWeight(V,E,V[pos],V[m])<length[m]:
					length[m]=length[pos]+getWeight(V,E,V[pos],V[m])
					path[m]=pos
	return path,length



def Bellman_Ford(V,E,begin):
	path=[0]*len(V)
	length=[0]*len(V)
	for j in range(0,len(V)):
		if j is not begin:
			length[j]=getWeight(V,E,V[begin],V[j])
			path[j]=begin
	for i in range(0,len(V)):
		for j in range(0,len(V)):
			for k in range(0,len(V)):
				if j!=k and length[j]+getWeight(V,E,V[j],V[k])<length[k]:
					path[k]=j
					length[k]=length[j]+getWeight(V,E,V[j],V[k])
	return path,length
					


def Floyd(V,E):
	path=[]
	length=[]
	for i in range(0,len(V)):
		path.append([])
		length.append([])
		for j in range(0,len(V)):
			if i!=j:
				length[i].append(getWeight(V,E,V[i],V[j]))
				path[i].append(i)
			else:
				path[i].append(i)
				length[i].append(0)
	for i in range(0,len(V)):
		for j in range(0,len(V)):
			for k in range(0,len(V)):
					if length[j][i]+length[i][k]<length[j][k]:
						length[j][k]=length[j][i]+length[i][k]
						path[j][k]=path[i][k]
	return length,path
	
def main():		
	V=[]
	E={}
	
	print "input the Vertexts,-1 for an end"
	a=int(input())
	while a is not -1:
		if a not in V:
			V.append(a)
		a=int(input())
	print "input the Edeges, * for an end"
	b=raw_input()
	while b!="*":
		m,n,s=b.split(" ")
		if int(m) in V and int(n) in V and int(s)>0:
			if E.has_key(int(m)):
				E[int(m)].append((int(m),int(n),int(s)))
			else:
				E[int(m)]=[]
				E[int(m)].append((int(m),int(n),int(s)))
		b=raw_input()
	print "\nthe graph you inputed is:"
	print V
	print E
	print "\nBellman_Ford:"
	path,length=Bellman_Ford(V,E,0)
	for i in range(0,len(V)):
		p=[]
		t=i
		print str(t)+":",
		while t is not 0:
			p.append(V[t])
			t=path[t]
		print 0,
		while len(p)>0:
			print p.pop(),
		print "\t"+str(length[i])
	print "\nFloyd:"
	print Floyd(V,E)
	print "\nBFS:"
	BFS(V,E,0)
	print "\nDFS:"
	firstTime,lastTime=DFS_start(V,E)
        for i in range(0,len(V)):
            print "%d,%4d,%4d"%(V[i],firstTime[i],lastTime[i])
        print "ToplogicalSort:"
        ans=TopologicalSort(V,E)
        print ans
        if len(ans)>0:
            print "TopologicalSort:dfs"
            print TopologicalSort_dfs(V,E)
        
        print "\nPrim:"
	print Prim(V,E)
	print "\nKruskal:"
	print Kruskal(V,E)

if __name__=="__main__":
	main()
