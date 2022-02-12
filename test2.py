# dijkstra - default
import sys
input=sys.stdin.readline
INF=int(1e9)
# nodes, edges
n,m=map(int, input().split())
# start node
start=int(input())
# graph, distance, visited
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
visited=[False]*(n+1)
# 모든 간선 정보 입력
for _ in range(m):
	a,b,c=map(int,input().split())
	graph[a].append((b,c))
# 다음으로 방문할 노드(최단거리가 가장 짧은) 번호 반환
def get_smallest_node():
	min_value=INF
	index=0
	for i in range(1,n+1):
		if distance[i]<min_value and not visited[i]:
			min_value=distance[i]
			index=i
	return index
# dijkstra
def dijkstra(start):
	# 시작 노드에 대해 초기화
	visited[start]=True
	distance[start]=0
	for i in graph[start]:
		distance[i[0]]=i[1]
 	# 시작노드를 제외한 n-1개의 노드에 대해 반복
	for _ in range(n-1):
		now=get_smallest_node()
		visited[now]=True
		# 현재 노드에서부터 그 인접 노드까지의 거리 갱신
		for i in graph[now]:
			dist=distance[now]+i[1]
			if dist<distance[i[0]]:
				distance[i[0]]=dist

dijkstra(start)
# 결과 출력
for i in range(1,n+1):
	if distance[i]==INF:
		print("INFINITY")
	else:
		print(distance[i])
