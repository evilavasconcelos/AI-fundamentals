from __future__ import annotations
import queue
import itertools

class State:
    name: str
    transitions: list
    def __init__(self, name):
        self.name = name
        self.transitions: list[Transition] = []

    def addTransition(self, transition: Transition):
        """Adiciona uma transição (estrada) a este estado (cidade)."""
        self.transitions.append(transition)

class Transition:
    destiny: State
    distance: int
    def __init__(self, destiny, distance):
        self.destiny = destiny
        self.distance = distance


class Map:
    states: list[State]
    def __init__(self, states):
        self.states=states

# Heurística: distância em linha reta até Bucareste
h = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

def get_heuristica(estado: State):
    """Função auxiliar para pegar o valor h(n) do dicionário."""
    return h.get(estado.name, float('inf'))

class Node:
    state: State
    pai: Node
    action: Transition
    distance: int

    def __init__(self, state, pai=None, action=None, distance=0):
        self.state = state
        self.pai = pai
        self.action = action
        self.distance = distance

def reconstruir_caminho(node):
    """
    Função auxiliar para reconstruir o caminho a partir do nó objetivo,
    seguindo os ponteiros 'pai' de volta à raiz.
    """
    caminho = []
    custo_total = node.distance # Custo g(n) final

    # Percorre o caminho de volta do nó final até o inicial
    while node.pai is not None:
        caminho.append(node.state.name)
        node = node.pai
    caminho.append(node.state.name) # Adiciona o estado inicial

    # A lista está na ordem inversa (objetivo -> inicial), então a revertemos
    caminho.reverse()

    return caminho, custo_total

# --- Criação dos Estados (Cidades) ---
s0 = State("Arad")
s1 = State("Bucharest")
s2 = State("Craiova")
s3 = State("Drobeta")
s4 = State("Eforie")
s5 = State("Fagaras")
s6 = State("Giurgiu")
s7 = State("Hirsova")
s8 = State("Iasi")
s9 = State("Lugoj")
s10 = State("Mehadia")
s11 = State("Neamt")
s12 = State("Oradea")
s13 = State("Pitesti")
s14 = State("Rimnicu Vilcea")
s15 = State("Sibiu")
s16 = State("Timisoara")
s17 = State("Urziceni")
s18 = State("Vaslui")
s19 = State("Zerind")

# --- Criação das Transições (Estradas) ---
# De/Para Arad (s0)
s0.addTransition(Transition(s19, 75))
s0.addTransition(Transition(s15, 140))
s0.addTransition(Transition(s16, 118))

# De/Para Zerind (s19)
s19.addTransition(Transition(s0, 75))
s19.addTransition(Transition(s12, 71))

# De/Para Oradea (s12)
s12.addTransition(Transition(s19, 71))
s12.addTransition(Transition(s15, 151))

# De/Para Sibiu (s15)
s15.addTransition(Transition(s0, 140))
s15.addTransition(Transition(s12, 151))
s15.addTransition(Transition(s5, 99))
s15.addTransition(Transition(s14, 80))

# De/Para Timisoara (s16)
s16.addTransition(Transition(s0, 118))
s16.addTransition(Transition(s9, 111))

# De/Para Lugoj (s9)
s9.addTransition(Transition(s16, 111))
s9.addTransition(Transition(s10, 70))

# De/Para Mehadia (s10)
s10.addTransition(Transition(s9, 70))
s10.addTransition(Transition(s3, 75))

# De/Para Drobeta (s3)
s3.addTransition(Transition(s10, 75))
s3.addTransition(Transition(s2, 120))

# De/Para Craiova (s2)
s2.addTransition(Transition(s3, 120))
s2.addTransition(Transition(s14, 146))
s2.addTransition(Transition(s13, 138))

# De/Para Rimnicu Vilcea (s14)
s14.addTransition(Transition(s15, 80))
s14.addTransition(Transition(s2, 146))
s14.addTransition(Transition(s13, 97))

# De/Para Fagaras (s5)
s5.addTransition(Transition(s15, 99))
s5.addTransition(Transition(s1, 211))

# De/Para Pitesti (s13)
s13.addTransition(Transition(s14, 97))
s13.addTransition(Transition(s2, 138))
s13.addTransition(Transition(s1, 101))

# De/Para Bucharest (s1)
s1.addTransition(Transition(s5, 211))
s1.addTransition(Transition(s13, 101))
s1.addTransition(Transition(s6, 90))
s1.addTransition(Transition(s17, 85))

# De/Para Giurgiu (s6)
s6.addTransition(Transition(s1, 90))

# De/Para Urziceni (s17)
s17.addTransition(Transition(s1, 85))
s17.addTransition(Transition(s7, 98))
s17.addTransition(Transition(s18, 142))

# De/Para Hirsova (s7)
s7.addTransition(Transition(s17, 98))
s7.addTransition(Transition(s4, 86))

# De/Para Eforie (s4)
s4.addTransition(Transition(s7, 86))

# De/Para Vaslui (s18)
s18.addTransition(Transition(s17, 142))
s18.addTransition(Transition(s8, 92))

# De/Para Iasi (s8)
s8.addTransition(Transition(s18, 92))
s8.addTransition(Transition(s11, 87))

# De/Para Neamt (s11)
s11.addTransition(Transition(s8, 87))


all_states = [
    s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10,
    s11, s12, s13, s14, s15, s16, s17, s18, s19
]

romania_map = Map(all_states)

print("--- Mapa da Romênia criado com sucesso! ---")
print(f"{len(all_states)} estados e suas transições foram carregados.")

def buscaGulosa(romania_map, estado_inicial, estado_objetivo):
    """
    Busca Gulosa (Greedy Best-First)
    Prioridade = h(n) (heurística)
    """
    node = Node(state=estado_inicial, distance=0)
    borda = queue.PriorityQueue()
    count = itertools.count()

    # Prioridade é apenas a heurística h(n)
    prioridade_h = get_heuristica(node.state)
    borda.put((prioridade_h, next(count), node))

    explorados = set()

    while True:
        if borda.empty():
            return "Falha: Caminho não encontrado.", float('inf')

        custo_h_atual, _, node_atual = borda.get()

        if node_atual.state.name == estado_objetivo.name:
            return reconstruir_caminho(node_atual)

        if node_atual.state.name in explorados:
            continue

        explorados.add(node_atual.state.name)

        for transicao in node_atual.state.transitions:
            filho_estado = transicao.destiny

            if filho_estado.name not in explorados:
                novo_custo_g = node_atual.distance + transicao.distance

                filho_node = Node(
                    state=filho_estado,
                    pai=node_atual,
                    action=transicao,
                    distance=novo_custo_g
                )

                prioridade_h_filho = get_heuristica(filho_estado)
                borda.put((prioridade_h_filho, next(count), filho_node))

# --- Execução da Busca Gulosa ---
print("--- 🧭 Resultado da Busca Gulosa (Greedy) ---")
inicio_guloso = s0  # Arad
objetivo_guloso = s1 # Bucharest

caminho_guloso, custo_guloso = buscaGulosa(romania_map, inicio_guloso, objetivo_guloso)

if isinstance(caminho_guloso, str):
    print(caminho_guloso)
else:
    print(f"Caminho: {' -> '.join(caminho_guloso)}")
    print(f"Custo total: {custo_guloso} km")