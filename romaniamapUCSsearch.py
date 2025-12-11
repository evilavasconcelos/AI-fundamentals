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
        self.states = states

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
    Função auxiliar para reconstruir o caminho a partir do nó objetivo.
    """
    caminho = []
    custo_total = node.distance

    while node.pai is not None:
        caminho.append(node.state.name)
        node = node.pai
    caminho.append(node.state.name) # Adiciona o estado inicial

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

# --- Criação das Transições ---
s0.addTransition(Transition(s19, 75))
s0.addTransition(Transition(s15, 140))
s0.addTransition(Transition(s16, 118))
s19.addTransition(Transition(s0, 75))
s19.addTransition(Transition(s12, 71))
s12.addTransition(Transition(s19, 71))
s12.addTransition(Transition(s15, 151))
s15.addTransition(Transition(s0, 140))
s15.addTransition(Transition(s12, 151))
s15.addTransition(Transition(s5, 99))
s15.addTransition(Transition(s14, 80))
s16.addTransition(Transition(s0, 118))
s16.addTransition(Transition(s9, 111))
s9.addTransition(Transition(s16, 111))
s9.addTransition(Transition(s10, 70))
s10.addTransition(Transition(s9, 70))
s10.addTransition(Transition(s3, 75))
s3.addTransition(Transition(s10, 75))
s3.addTransition(Transition(s2, 120))
s2.addTransition(Transition(s3, 120))
s2.addTransition(Transition(s14, 146))
s2.addTransition(Transition(s13, 138))
s14.addTransition(Transition(s15, 80))
s14.addTransition(Transition(s2, 146))
s14.addTransition(Transition(s13, 97))
s5.addTransition(Transition(s15, 99))
s5.addTransition(Transition(s1, 211))
s13.addTransition(Transition(s14, 97))
s13.addTransition(Transition(s2, 138))
s13.addTransition(Transition(s1, 101))
s1.addTransition(Transition(s5, 211))
s1.addTransition(Transition(s13, 101))
s1.addTransition(Transition(s6, 90))
s1.addTransition(Transition(s17, 85))
s6.addTransition(Transition(s1, 90))
s17.addTransition(Transition(s1, 85))
s17.addTransition(Transition(s7, 98))
s17.addTransition(Transition(s18, 142))
s7.addTransition(Transition(s17, 98))
s7.addTransition(Transition(s4, 86))
s4.addTransition(Transition(s7, 86))
s18.addTransition(Transition(s17, 142))
s18.addTransition(Transition(s8, 92))
s8.addTransition(Transition(s18, 92))
s8.addTransition(Transition(s11, 87))
s11.addTransition(Transition(s8, 87))

all_states = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19]
romania_map = Map(all_states)

print("--- Mapa da Romênia (Sem Informação) criado com sucesso! ---")

def buscaCustoUniforme(romania_map, estado_inicial, estado_objetivo):
    node = Node(state=estado_inicial, distance=0)

    #Fila de Prioridade
    borda = queue.PriorityQueue()
    count = itertools.count()
    borda.put((node.distance, next(count), node))#é uma fila de tuplas


    explorados = set()


    while True:

        if borda.empty():
            return "Falha: Caminho não encontrado.", float('inf')

        # Remover da borda (menor custo)
        custo_atual, _, node_atual = borda.get()

        #Teste de objetivo AO REMOVER
        if node_atual.state.name == estado_objetivo.name:
            return reconstruir_caminho(node_atual)

        # Adicionar a explorados
        explorados.add(node_atual.state.name)

        #Para cada ação
        for transicao in node_atual.state.transitions:
            # Criar nó filho
            filho_estado = transicao.destiny
            novo_custo = custo_atual + transicao.distance
            filho_node = Node(
                state=filho_estado,
                pai=node_atual,
                action=transicao,
                distance=novo_custo
            )

            if filho_estado.name not in explorados:
                borda.put((filho_node.distance, next(count), filho_node))

# --- Execução UCS ---
print("\n--- 💰 Resultado da Busca de Custo Uniforme (UCS) ---")
caminho_ucs, custo_ucs = buscaCustoUniforme(romania_map, s0, s1)
if isinstance(caminho_ucs, str): print(caminho_ucs)
else: print(f"Caminho: {' -> '.join(caminho_ucs)} (Custo: {custo_ucs} km)")