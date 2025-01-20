# DFS-based exploration for data retrieval in case of node failure

class DistributedSystem:
    def __init__(self, num_nodes):
        # Initialize the system with num_nodes (servers)
        self.num_nodes = num_nodes
        self.graph = {i: [] for i in range(num_nodes)}  # Adjacency list for representing connections
    
    def add_connection(self, node1, node2):
        # Add bidirectional connection between two nodes (servers)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
    
    def dfs(self, start, visited, failed_nodes):
        
        visited.add(start)

        # Explore all connected nodes
        for neighbor in self.graph[start]:
            if neighbor not in visited and neighbor not in failed_nodes:
                self.dfs(neighbor, visited, failed_nodes)

    def find_backup_nodes(self, failed_node:set, data_source_node):
        visited = set()

        self.dfs(data_source_node, visited, failed_node)

        if len(visited) == 1:
            print("No backup nodes found. Data cannot be retrieved.")
        else:
            print(f"\nData can be retrieved from the following backup nodes for the source node {data_source_node} even if node(s) {failed_node if len(failed_node) else "'No failure node'"} fails:")
            print(visited)


n = int(input("Enter number of server devices: "))
distributed_system = DistributedSystem(n)
failed_nodes = set()

while True:
    try:
        i = int(input("\nEnter choice:\n1. To Add connection.\n2. To find backup nodes.\n3. Mark a failure node.\n4. To restart a failed node.\n-1. To exit: "))
        if i == -1:
            print("Terminating.....")
            break
        if i == 1:
            count = int(input("Enter no of pairs/connections to be added: "))
            i = 0
            while i < count:
                a, b = map(int, input("Enter adjacent nodes: ").split())
                if a < n and b < n:
                    distributed_system.add_connection(a, b)
                    i += 1
                else:
                    print("Wrong input of nodes!!!")
                    continue
            print("Connections added.")
        elif i == 2:
            src = int(input("Input the source server to find backup for: "))
            if src < n:
                distributed_system.find_backup_nodes(failed_nodes, src)
            else:
                print("Wrong input for src")
        elif i == 3:
            failed_node = int(input("Input a failed node for simulation test: "))
            if failed_node < n:
                failed_nodes.add(failed_node)
                print("added failed node.")
            else:
                print("Wrong input")
        elif i == 4:
            node = int(input("Input a failed node for simulation test: "))
            if node < n:
                failed_nodes.remove(node)
                print("removed a failed node.")
            else:
                print("Wrong input")
        else:
            print("Wrong input.")
    except Exception as e:
        print(f"Error Occurred {e}")
        print("Terminating.....")
        break
