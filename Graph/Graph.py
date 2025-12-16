"""

============================================================================
#
#                  GRAPH MASTERY SHEET
#
============================================================================
PHASE 0: PREREQUISITES
* Graph representation: adjacency list, matrix, edge list
* Key definitions: directed/undirected, weighted/unweighted, sparse/dense
* Basic complexity considerations for graph traversal
============================================================================
"""
# From Dictionary to Adjacency List 

# graphAdjList = {1:[1,2],2:[3,4],3:[2,1],4:[1,2,3]}
# print(graphAdjList.keys())


# From Dictionary to Adjacency Matrix
"""
graphAdjMat = {1:[1,2],2:[3,4],3:[2,1],4:[1,2,3]}
nodes = sorted(graphAdjMat)
n = len(nodes)
node = {node: i for i , node in enumerate(nodes)}

adj_matrix = [[0]*n for _ in range(n)]
print(adj_matrix)

for u in graphAdjMat:
    for v in graphAdjMat[u]:
        adj_matrix[node[u]][node[v]] =1 
print(adj_matrix)
"""
# from collections import defaultdict 

# Creating undirected Graph
from collections import defaultdict 
def create_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph
edges = [(1,2),(2,3),(1,3),(1,4)]
graph = create_graph(edges)
print(graph)

# Creating the Directed Grapgh
from collections import defaultdict 
def create_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        # graph[v].append(u)
    return graph
edges = [(1,2),(2,3),(1,3),(1,4)]
# 1 -- 2 , 
graph = create_graph(edges)
print(graph)

"""
PHASE 1: REPRESENTATION + BASIC TRAVERSAL
1. Path Exists (simple BFS) https://leetcode.com/problems/find-if-path-exists-in-graph/ (1971)
2. Number of Provinces (connectivity warm-up) https://leetcode.com/problems/number-of-provinces/ (547)
3. Graph Bipartite https://leetcode.com/problems/is-graph-bipartite/ (785)
4. Clone Graph https://leetcode.com/problems/clone-graph/ (133)
5. Keys and Rooms https://leetcode.com/problems/keys-and-rooms/ (841)

============================================================================
PHASE 2: CONNECTED COMPONENTS & GRID-AS-GRAPH 
6. Number of Islands https://leetcode.com/problems/number-of-islands/ (200) 
7. Number of Islands II (Incremental Union-Find) https://leetcode.com/problems/number-of-islands-ii/ (305) 
8. Surrounded Regions https://leetcode.com/problems/surrounded-regions/ (130) 
9. Pacific Atlantic Water Flow https://leetcode.com/problems/pacific-atlantic-water-flow/ (417) 
10. Walls and Gates https://leetcode.com/problems/walls-and-gates/ (286)

============================================================================
PHASE 3: CYCLE DETECTION + DAG FOUNDATIONS 
11. Course Schedule (cycle detection in directed graph) https://leetcode.com/problems/course-schedule/ (207) 
12. Course Schedule II (topological order) https://leetcode.com/problems/course-schedule-ii/ (210) 
13. Eventual Safe States https://leetcode.com/problems/find-eventual-safe-states/ (802) 
14. Graph Valid Tree https://leetcode.com/problems/graph-valid-tree/ (261)

============================================================================
PHASE 4: TRANSFORMATION GRAPHS 
15. Word Ladder https://leetcode.com/problems/word-ladder/ (127) 
16. Word Ladder II https://leetcode.com/problems/word-ladder-ii/ (126) 
17. Open the Lock https://leetcode.com/problems/open-the-lock/ (752) 
18. Bus Routes https://leetcode.com/problems/bus-routes/ (815)

============================================================================
PHASE 5: UNION–FIND MASTER PROBLEMS 
19. Redundant Connection https://leetcode.com/problems/redundant-connection/ (684) 
20. Redundant Connection II https://leetcode.com/problems/redundant-connection-ii/ (685) 
21. Most Stones Removed https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/ (947) 
22. Evaluate Division https://leetcode.com/problems/evaluate-division/ (399)

============================================================================
PHASE 6: CLASSIC SHORTEST PATH 
23. Shortest Path in Binary Matrix https://leetcode.com/problems/shortest-path-in-binary-matrix/ (1091) 
24. Network Delay Time https://leetcode.com/problems/network-delay-time/ (743) 
25. Cheapest Flights Within K Stops https://leetcode.com/problems/cheapest-flights-within-k-stops/ (787) 
26. Path With Minimum Effort https://leetcode.com/problems/path-with-minimum-effort/ (1631) 
27. Floyd-Warshall (All-pairs shortest path) Conceptual understanding (see tutorials)

============================================================================
PHASE 7: MINIMUM SPANNING TREE 
28. Min Cost to Connect All Points https://leetcode.com/problems/min-cost-to-connect-all-points/ (1584) 
29. Connecting Cities With Minimum Cost https://leetcode.com/problems/connecting-cities-with-minimum-cost/ (1135)

============================================================================
PHASE 8: ADVANCED BFS/DFS & HARD PROBLEMS 
30. Shortest Bridge https://leetcode.com/problems/shortest-bridge/ (934) 
31. Swim in Rising Water https://leetcode.com/problems/swim-in-rising-water/ (778) 
32. Reconstruct Itinerary https://leetcode.com/problems/reconstruct-itinerary/ (332) 
33. Critical Connections (Bridges via Tarjan) https://leetcode.com/problems/critical-connections-in-a-network/ (1192) 
34. 0/1 BFS (Deque technique) Suggested: https://leetcode.com/problems/minimum-cost-to-make-grid-valid/ (1368)


============================================================================
PHASE 9: SCC + ARTICULATION POINTS + TREE DP 
35. Strongly Connected Components (Kosaraju / Tarjan) Suggested: https://leetcode.com/problems/strongly-connected-components-of-a-directed-graph/ (2617) 
36. Articulation Points (Cut vertices) Practice Tarjan low-link algorithm variants (no direct LeetCode official problem) 
37. Tree Diameter https://leetcode.com/problems/tree-diameter/ (1245) 
38. Sum of Distances in Tree https://leetcode.com/problems/sum-of-distances-in-tree/ (834) 
39. Longest Path in DAG (custom practice)


============================================================================
PHASE 10: MASTER PROBLEMS + NETWORK FLOW 
40. Parallel Courses III https://leetcode.com/problems/parallel-courses-iii/ (2050) 41. Snakes and Ladders https://leetcode.com/problems/snakes-and-ladders/ (909) 42. Shortest Path Visiting All Nodes https://leetcode.com/problems/shortest-path-visiting-all-nodes/ (847) 43. Max Flow / Min Cut Suggested classic problems: - Maximum Bipartite Matching https://leetcode.com/problems/maximum-bipartite-matching/ (788) - Study Ford-Fulkerson, Dinic’s algorithm tutorials and implement accordingly
=============================================================================

"""

