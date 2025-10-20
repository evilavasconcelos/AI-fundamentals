#Vacuum World - Agente Simples
class Perception:
    def __init__(self, location, isDirty):
        self.location = location
        self.isDirty = isDirty
    

class Action:
    def __init__(self, name):
        self.name = name

class Environment:
    def __init__(self, isDirtyA=True, isDirtyB=True, agentLocation='A'):
        self.agentLocation = agentLocation
        self.isDirtyA = isDirtyA
        self.isDirtyB = isDirtyB

    def currentState(self):
       A = "🦠" if self.isDirtyA else "🫧"
       B = "🦠" if self.isDirtyB else "🫧"
       if self.agentLocation == 'A':
            return f"[Sala A: 🤖 {A}]  [Sala B: {B}]"
       else:
            return f"[Sala A: {A}]  [Sala B: 🤖 {B}]"

    # NOTE: o parâmetro aqui é 'name' (string). Usamos self.* para acessar atributos.
    def act(self, name):
        if name == 'aspirar':
            if self.agentLocation == 'A':
                self.isDirtyA = False
            else:
                self.isDirtyB = False
        elif name == 'direita':
            self.agentLocation = 'B'
        elif name == 'esquerda':
            self.agentLocation = 'A'


    def get_perception(self):
        if self.agentLocation == 'A':
            return Perception('A', self.isDirtyA)
        else:
            return Perception('B', self.isDirtyB)
        
    def show(self):
        print(f"Localização do Agente: {self.agentLocation}, Sujeira em A: {self.isDirtyA}, Sujeira em B: {self.isDirtyB}")

class Agent:
    def __init__(self, name="agente"):
        self.name=name
    
    def perceive(self, environment):
       return environment.get_perception()
    
    def act(self, perception):
        if perception.isDirty:
            return Action('aspirar')
        elif perception.location == 'A':
            return Action('direita')
        else:
            return Action('esquerda')
        
class VacuumWorld:
    def __init__(self, environment, agent):
        self.environment = environment
        self.agent = agent
    
    def step(self):
        perception = self.agent.perceive(self.environment)
        action = self.agent.act(perception)
        
        print (f"Percepção: {perception.location}, {'🦠' if perception.isDirty else '🫧'}")
        print (f"Ação: {action.name}\n")

        self.environment.act(action.name)

    def run(self, steps):
        for i in range(1, steps + 1):
            print(f"Passo {i}")
            print(self.environment.currentState())
            self.step()
            print("----------------------------------------")
        print("FIM!\n")


if __name__ == "__main__":
    environment = Environment(isDirtyA=True, isDirtyB=True, agentLocation='A')
    agent = Agent()
    world = VacuumWorld(environment, agent)
    world.run(6)
