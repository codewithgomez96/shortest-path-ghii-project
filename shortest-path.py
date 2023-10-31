from collections import deque

INFINITY = float("inf")


class Graph:
    def __init__(self):
        """
        Initialize the Graph with an empty set of nodes and an empty adjacency list.
        """
        self.nodes = set()
        self.adjacency_list = {}

    def add_edge(self, start, end, weight):
        """
        Add an edge to the graph.

        Parameters:
        - start (str): The starting node of the edge.
        - end (str): The ending node of the edge.
        - weight (float): The weight (distance) of the edge.
        """
        # Update the set of nodes
        self.nodes.update([start, end])

        # Add edge to the adjacency list
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        self.adjacency_list[start].append((end, weight))

    def shortest_path(self, start_node, end_node):
        """
        Find the shortest path from start_node to end_node in the graph.

        Parameters:
        - start_node (str): The starting node.
        - end_node (str): The ending node.

        Returns:
        - path (deque): A deque containing the nodes in the shortest path.
        - distance_from_start (float): The total distance of the shortest path.
        """
        unvisited_nodes = self.nodes.copy()
        distance_from_start = {
            node: (0 if node == start_node else INFINITY) for node in self.nodes}
        previous_node = {node: None for node in self.nodes}

        while unvisited_nodes:
            current_node = min(
                unvisited_nodes, key=lambda node: distance_from_start[node])
            unvisited_nodes.remove(current_node)

            if distance_from_start[current_node] == INFINITY:
                break

            for neighbor, distance in self.adjacency_list.get(current_node, []):
                new_path = distance_from_start[current_node] + distance
                if new_path < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = new_path
                    previous_node[neighbor] = current_node

            if current_node == end_node:
                break

        path = deque()
        current_node = end_node
        while previous_node[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_node[current_node]
        path.appendleft(start_node)

        return path, distance_from_start[end_node]


def main():
    graph = Graph()

    # Define graph data manually
    graph.add_edge("Mchinji", "Kasungu", 141)
    graph.add_edge("Kasungu", "Mchinji", 141)

    graph.add_edge("Mchinji", "Lilongwe", 109)
    graph.add_edge("Lilongwe", "Mchinji", 109)

    graph.add_edge("Kasungu", "Dowa", 117)
    graph.add_edge("Dowa", "Kasungu", 117)

    graph.add_edge("Lilongwe", "Dowa", 55)
    graph.add_edge("Dowa", "Lilongwe", 55)

    graph.add_edge("Kasungu", "Ntchisi", 66)
    graph.add_edge("Ntchisi", "Kasungu", 66)

    graph.add_edge("Dowa", "Ntchisi", 38)
    graph.add_edge("Ntchisi", "Dowa", 38)

    graph.add_edge("Ntchisi", "Nkhotakota", 66)
    graph.add_edge("Nkhotakota", "Ntchisi", 66)

    graph.add_edge("Dowa", "Salima", 67)
    graph.add_edge("Salima", "Dowa", 67)

    graph.add_edge("Lilongwe", "Dedza", 92)
    graph.add_edge("Dedza", "Lilongwe", 92)

    graph.add_edge("Dedza", "Salima", 96)
    graph.add_edge("Salima", "Dedza", 96)

    graph.add_edge("Salima", "Nkhotakota", 112)
    graph.add_edge("Nkhotakota", "Salima", 112)

    graph.add_edge("Dedza", "Ntchewu", 74)
    graph.add_edge("Ntchewu", "Dedza", 74)

    shortest_path(graph, start="Mchinji",
                  end="Ntchewu",
                  )


def shortest_path(graph, start, end):
    returned_path, returned_distance = graph.shortest_path(start, end)

    print("\nSource/Destination:", start, "->", end)
    print("Shortest path:", list(returned_path))
    print("Total distance of the path:", returned_distance)


if __name__ == "__main__":
    main()
