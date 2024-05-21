class Atleta:
    def __init__(self, peso):
        self.aposentado = False
        self.peso = peso

    def aposentar(self):
        self.aposentado = True
        print("O atleta se Aposentou.")
class Corredor(Atleta):
    def __init__(self,peso):
        super().__init__(peso)

    def correr(self):
        print("O atleta correu até o proximo percurso.")

class Nadador(Atleta):
    def __init__(self,peso):
        super().__init__(peso)

    def nadar(self):
        print("O atleta nadou até o próximo percurso")

class Ciclista(Atleta):
    def __init__(self,peso):
        super().__init__(peso)


    def pedalar(self):
        print("O ciclista escutou Hime Hime e saiu pedalando a todo vapor.")

class Triatleta(Corredor,Nadador,Ciclista):
    def __init__(self,peso):
        super().__init__(peso)