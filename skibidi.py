class Graph:
    def __init__(self):
        self.vertices = {}  # Słownik przechowujący listy sąsiedztwa dla każdego wierzchołka

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        # Sprawdzanie, czy wierzchołki istnieją
        if vertex1 in self.vertices and vertex2 in self.vertices:
            # Dodawanie krawędzi obustronnie
            self.vertices[vertex1][vertex2] = weight
            self.vertices[vertex2][vertex1] = weight

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

    def __str__(self):
        result = ""
        for vertex in self.vertices:
            result += str(vertex) + ": "
            for neighbor, weight in self.vertices[vertex].items():
                result += "(" + str(neighbor) + ", " + str(weight) + ") "
            result += "\n"
        return result


# Przykładowe użycie
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 2)

print(g)