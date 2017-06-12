#!/usr/bin/env python 
#coding=utf-8

def getWeight(V,E,u,v):
	if E.has_key(u):
		for i in E[u]:
			if i[1] is v:
				return i[2]
	return 100000

def BFS(V,E,start):
	color=[]
	depth=[]
	for i in range(0,len(V)):
		color.append(-1)
		depth.append(0)
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

def DFS_start(V,E):
	color=[]
	depth=[]
	time=0
	for i in range(0,len(V)):
		color.append(-1)
		depth.append(0)
	for i in V:
		if color[V.index(i)]==-1:
			DFS(V,E,color,time,depth,i)
	return depth

def DFS(V,E,color,time,depth,i):
	depth[V.index(i)]=time
	print " "*depth[V.index(i)],
	print i
	color[V.index(i)]=0
	if E.has_key(i):
		for m in E[i]:
			if color[V.index(m[1])]==-1:
				time=time+1
				DFS(V,E,color,time,depth,m[1])
	color[i]=1	


def Kruskal(V,E):
	visited=[]
	visited_joined=[]
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
		flag=True
		for i in visited_joined:
			if (temp[0]==i[0] and temp[1]==i[1]) or (temp[0]==i[1] and temp[1]==i[0]):
				flag=False
		if flag:
			visited.append(temp)
			n=0
			for t in visited_joined:
				if t[1]==k[1]:
					n=n+1
				if t[0]==k[1]:
					n=n+1
				if t[1]==k[0]:
					n=n+1
				if t[1]==k[1]:
					n=n+1
			if n==2:
				visited_joined.append(temp)			
	return visited

def Prim(V,E):
	visited=[]
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
			n=0
			for k in visited:
				if k[0]==j[0]:
					n=n+1
				if k[1]==j[0]:
					n=n+1
				if k[0]==j[1]:
					n=n+1
				if k[1]==j[1]:
					n=n+1
			if n==1:
				flag=True
			if j[2]<temp[2] and flag:
				temp=j
		if temp[2]==65535:
			continue
		visited.append(temp)
		notvisited.pop(notvisited.index(temp))
	return visited
			
	
	
def Dijikstra(V,E,begin):
	visited=[]
	length=[]
	path=[]
	for i in range(0,len(V)):
		visited.append(False)
	for j in range(0,len(V)):
		if j is not begin:
			length.append(getWeight(V,E,V[begin],V[j]))
			path.append(begin)
		else:
			length.append(0)
			path.append(0)
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
	path=[]
	length=[]
	for j in range(0,len(V)):
		if j is not begin:
			length.append(getWeight(V,E,V[begin],V[j]))
			path.append(begin)
		else:
			length.append(0)
			path.append(0)
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
	DFS_start(V,E)
	print "\nPrim:"
	print Prim(V,E)
	print "\nKruskal:"
	print Kruskal(V,E)

if __name__=="__main__":
	main()
