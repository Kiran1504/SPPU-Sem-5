class Graph:
    def __init__(self, n, e):
        self.n = n
        self.e = e
        self.adj = []
        for i in range(self.n):
            self.adj.append([])

    def create_graph(self):
        print("Enter adjacent nodes present in that edge: ")
        for i in range(self.e):
            node1, node2 = map(int, input().split())
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
    
    def bfs(self, src):
        visited = [0] * self.n
        q = []
        q.append(src)
        visited[src] = 1
        bfs_arr = []
        while(len(q) > 0):
            node = q.pop(0)
            bfs_arr.append(node)
            for i in self.adj[node]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1

        print("The BFS Traversal of inputted graph is: ", bfs_arr)

    def rec_dfs(self, node, visited, dfs_arr):
        visited[node] = 1
        dfs_arr.append(node)
        for i in self.adj[node]:
            if not visited[i]:
                self.rec_dfs(i, visited, dfs_arr)
    
    def dfs(self, src):
        visited = [0] * self.n
        dfs_arr = []
        self.rec_dfs(src, visited, dfs_arr)
        print("The DFS Traversal of inputted graph is: ", dfs_arr)

if __name__ == "__main__":
    n = int(input("Number of vertices/nodes in a graph: "))
    e = int(input("Number of edges in graph: "))
    graph = Graph(n, e)
    while True:
        try:
            choice = int(input("1. Input Graph\n2.Perform BFS\n3.Perform DFS\n-1. To Exit: "))
            if choice == -1:
                break
            if choice==1:
                graph.create_graph()
            elif choice == 2:
                src = int(input("Enter source node: "))
                graph.bfs(src)
            elif choice == 3:
                src = int(input("Enter source node: "))
                graph.dfs(src)
        except Exception as e:
            print(str(e))
            break