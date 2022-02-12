# ployd-warshall
import sys
input=sys.stdin.readline
INF=int(1e9)
# 노드와 간선의 개수
n,m=map(int, input().split())
# graph
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
	graph[i][i]=0
# 모든 간선 정보
for _ in range(m):
	a,b,c=map(int, input().split())
	graph[a][b]=c

for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])

# 결과 출력
for i in range(1,n+1):
	for j in range(1,n+1):
		if graph[i][j]==INF:
			print("INFINITY",end=' ')
		else:
			print(graph[i][j],end=' ')
	print()
