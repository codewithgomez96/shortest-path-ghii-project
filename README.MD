# Shortest Path Finder

This Python project demonstrates Dijkstra's algorithm to find the shortest path of road networks and districts of the Central Region in Malawi but it can be used in other apllications to find the shortest path  in a graph. It includes a `Graph` class that allows you to define a graph by adding edges between nodes and find the shortest path between two nodes/places.

## Table of Contents

- [Usage](#usage)
- [Graph Data Format](#graph-data-format)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)

## Usage

1. **Clone this repository** to your local machine:

   git clone https://github.com/your-username/shortest-path-finder.git


2. **Run the script** to find the shortest path between nodes in the graph.
   You can modify the graph data directly in the script.

   python shortest_path.py


3. **Replace the graph data** in the shortest_path.py script with your own graph data if needed.

## Graph Data Format

    To define edges in the graph, use the add_edge method in the Graph class. The format is:
   
    graph.add_edge("Start_Node", "End_Node", Weight)


### Example

    Here's an example of adding edges to the graph:
    graph.add_edge("Mchinji", "Kasungu", 141)
    graph.add_edge("Kasungu", "Mchinji", 141)

## Requirements

    This project has been tested with Python 3.

## License

    This project is licensed under the MIT License. See the LICENSE file for details.
    Feel free to contribute or report issues.
