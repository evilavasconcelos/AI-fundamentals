#Vacuum World - Modelos
class State:
    def __init__(self, name, isDirtyA, isDirtyB, agentLocation, neighbors):
        self.name = name
        self.isDirtyA = isDirtyA
        self.isDirtyB = isDirtyB
        self.agentLocation = agentLocation
        self.neighbors = neighbors

s0=State("s0", True, True, 'A', [])
s1=State("s1", False, True, 'A', [] )
s2=State("s2", False, True, 'B',[] )
s3=State("s3", False, False, 'B',[])
s4=State("s4", False, False, 'A',[] )
s5=State("s5", True, True, 'A', [])
s6=State("s6", True, False, 'B',[] )
s7=State("s7", True, False, 'A',[] )

neighbors = {
's0': [(s0,"esquerda"), (s1,"aspira"), (s5,"direita")],
's1': [(s1,"esquerda"), (s1,"aspira"),(s2,"direita")],
's2': [(s1,"esquerda"), (s2,"direita"),(s3,"aspira")],
's3': [(s3,"direita"),(s3,"aspira"),(s4, "esquerda")],
's4': [(s3,"direita"), (s4,"esquerda"),(s4,"aspira")],
's5': [(s0,"esquerda"),(s5,"direita"),(s6,"aspira")],
's6': [(s6,"direita"),(s6,"aspira"),(s7,"esquerda")],
's7':[(s4,"aspira"),(s6,"direita"),(s7,"esquerda")]
}