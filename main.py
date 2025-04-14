class Graph:
    def __init__(self, vertices):
        """
        Inicializa um grafo com o número especificado de vértices.
        
        Args:
            vertices (int): Número de vértices no grafo
        """
        self.V = vertices
        
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def add_edge(self, v1, v2):
        """
        Adiciona uma aresta entre dois vértices no grafo não direcionado.
        
        Args:
            v1 (int): Primeiro vértice
            v2 (int): Segundo vértice
        """
        
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1
    
    def hamiltonian_path_util(self, path, pos, visited):
        """
        Função auxiliar recursiva que implementa o backtracking para encontrar
        um caminho hamiltoniano.
        
        Args:
            path (list): Lista que armazena o caminho atual
            pos (int): Posição atual no caminho
            visited (set): Conjunto de vértices já visitados
        
        Returns:
            bool: True se um caminho for encontrado, False caso contrário
        """
        
        if pos == self.V:
            return True
        
        
        for v in range(self.V):
            
            if self._is_valid_next_vertex(v, path, pos, visited):
                
                path[pos] = v
                visited.add(v)
                
                
                if self.hamiltonian_path_util(path, pos + 1, visited):
                    return True
                
                
                
                visited.remove(v)
                path[pos] = -1
        
        return False
    
    def _is_valid_next_vertex(self, v, path, pos, visited):
        """
        Verifica se um vértice pode ser adicionado na posição 'pos' do caminho.
        
        Args:
            v (int): Vértice a ser verificado
            path (list): Caminho atual
            pos (int): Posição atual no caminho
            visited (set): Conjunto de vértices já visitados
        
        Returns:
            bool: True se o vértice pode ser adicionado, False caso contrário
        """
        
        if v in visited:
            return False
        
        
        if pos == 0:
            return True
        
        
        
        last_vertex = path[pos - 1]
        return self.graph[last_vertex][v] == 1
    
    def find_hamiltonian_path(self):
        """
        Encontra um caminho hamiltoniano no grafo, se existir.
        
        Returns:
            list: Lista representando o caminho hamiltoniano ou None se não existir
        """
        
        path = [-1] * self.V
        visited = set()
        
        
        for start in range(self.V):
            path[0] = start
            visited = {start}
            
            if self.hamiltonian_path_util(path, 1, visited):
                return path
            
            visited.remove(start)
            path[0] = -1
        
        return None

def main():
    """
    Função principal para demonstrar o uso do algoritmo.
    """
    
    print("\nExemplo 1: Grafo com caminho hamiltoniano")
    g1 = Graph(5)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 4)
    
    path = g1.find_hamiltonian_path()
    if path:
        print(f"Caminho Hamiltoniano encontrado: {path}")
    else:
        print("Não existe caminho hamiltoniano")
    
    
    print("\nExemplo 2: Grafo sem caminho hamiltoniano")
    g2 = Graph(5)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 2)
    
    path = g2.find_hamiltonian_path()
    if path:
        print(f"Caminho Hamiltoniano encontrado: {path}")
    else:
        print("Não existe caminho hamiltoniano")

if __name__ == "__main__":
    main() 