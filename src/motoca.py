from pessoa import Pessoa

class Motoca:

    def __init__(self, potencia: int):
        self.potencia = potencia
        self.pessoa = None
        self.tempo = 0

    def getPessoa(self):
        return self.pessoa

    def getTempo(self):
        return self.tempo

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.pessoa is None:
           self.pessoa = pessoa
           return True
        return False
    
    def descer(self):
        if self.pessoa is not None:
            self.pessoa = None
            return True
        return False

    def colocarTempo(self, tempo: int):
        if tempo >= 0:
            self.tempo +=tempo
            return True
        return False

    def dirigir(self, tempo: int):
        if self.pessoa is None:
            return False
        try:
            idade = int(self.pessoa.getIdade())
        except:
            print("Idade invalida")
            return False
# O try e o except foram adicionados para garantir que, caso a idade não seja um número inteiro,
# o método retornar False, conforme esperado nos testes.
        if idade > 10:
            print("Não está mais apto a passear de moto")
            return False
        if tempo <= 0:
            return False
        if self.tempo == 0:
            return False
        if tempo <= self.tempo:
            self.tempo -= tempo
            return True
        else:
            andou = self.tempo
            self.tempo = 0
            print(f"A pessoa andou por {andou} minutos")
            return True
        
    def buzinar(self):
        resultado = "P"
        try:
            pot = int(self.potencia)
        except:
            pot = 0
        for _ in range(max(0, pot)):
            resultado += "e"
        resultado += "m"
        return resultado
