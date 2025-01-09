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
        """
        Perform DFS to find all nodes connected to the start node, excluding failed nodes.
        This ensures that data can still be retrieved from backup nodes.
        """
        visited.add(start)
        print(f"Visiting node {start} for data retrieval.")
        
        # Explore all connected nodes
        for neighbor in self.graph[start]:
            if neighbor not in visited and neighbor not in failed_nodes:
                self.dfs(neighbor, visited, failed_nodes)

    def find_backup_nodes(self, failed_node, data_source_node):
        """
        Find backup nodes that can store the same data when one node fails.
        If a node fails, DFS is performed to find all available nodes for data retrieval.
        """
        print(f"\nStarting DFS to find backup nodes for data retrieval if node {failed_node} fails.")
        
        # Set of visited nodes to avoid cycles
        visited = set()
        
        # Set of failed nodes (cannot access these)
        failed_nodes = {failed_node}
        
        # Start DFS from the data source node, looking for all backup nodes
        self.dfs(data_source_node, visited, failed_nodes)

        if len(visited) == 1:
            print("No backup nodes found. Data cannot be retrieved.")
        else:
            print("\nData can be retrieved from the following backup nodes:")
            print(visited)


# Initialize the distributed system with 6 nodes (servers)
distributed_system = DistributedSystem(6)

# Add connections between nodes (simulating communication between servers)
distributed_system.add_connection(0, 1)
distributed_system.add_connection(1, 2)
distributed_system.add_connection(2, 3)
distributed_system.add_connection(3, 4)
distributed_system.add_connection(4, 5)
distributed_system.add_connection(0, 5)

# Simulate a failure of node 2
failed_node = 2

# Assume that node 0 holds the data and we need to find backups
data_source_node = 0

# Find backup nodes after the failure of node 2
distributed_system.find_backup_nodes(failed_node, data_source_node)



# pip install requests beautifulsoup4

# import requests
# from bs4 import BeautifulSoup
# from collections import deque

# # BFS Web Crawler
# def bfs_crawl(start_url):
#     visited = set()  # To keep track of visited URLs
#     queue = deque([start_url])  # Queue for BFS
    
#     while queue:
#         url = queue.popleft()  # Get the next URL from the queue
        
#         # If the URL is already visited, skip it
#         if url in visited:
#             continue
        
#         print(f"Visiting: {url}")
#         visited.add(url)  # Mark this URL as visited
        
#         try:
#             # Send a GET request to the URL and parse the HTML content
#             response = requests.get(url)
#             soup = BeautifulSoup(response.text, "html.parser")
            
#             # Find all anchor tags (links) on the page
#             links = soup.find_all("a", href=True)
            
#             # Enqueue all unvisited links
#             for link in links:
#                 new_url = link['href']
#                 if new_url.startswith("http") and new_url not in visited:
#                     queue.append(new_url)
#         except requests.RequestException as e:
#             print(f"Failed to retrieve {url}: {e}")

# # Starting point for the BFS crawler
# start_url = "https://example.com"
# bfs_crawl(start_url)
