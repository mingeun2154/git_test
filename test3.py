# dijkstra_improved
import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)
# 노드, 간선 개수 입력
n,m=map(int, input().split())
# 시작 노드
start=int(input())
# graph, distance
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
# 모든 간선 정보 입력
for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))
# dijkstra
def dijkstra(start):
    q=[]
    # 시작 노드에 대해 초기화
    heapq.heappush(q, (0, start))
    distance[start]=0
    # 반복문
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        # 현재 노드에서 그 인접 노드까지의 거리 갱신
        for i in graph[now]:
            cost=distance[now]+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
# 결과 출력
for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
