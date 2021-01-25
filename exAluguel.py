#   Daniel, Eduardo & Yan

class Cliente():
    def __init__(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

class Veiculo():
    def __init__(self, placa, valor):
        self._placa = placa
        self._valor = valor
        self._alugado = False
        self._historico = []

    def alugar(self, cliente, dias):
        self._cliente = cliente
        self._dias = dias

        if self._alugado == True:
            return ("Este carro ja está alugado")
        else:
            self._alugado = True
            self._historico.append(("O veiculo de placa {} foi alugado pelo cliente {} no valor de {}").format(self._placa, self._cliente.getNome(), self.calcularAluguel(dias)))

            return ("O veiculo de placa {} alugado pelo cliente {} no valor de {}").format(self._placa, self._cliente.getNome(), self.calcularAluguel(dias))

    def devolver(self):
        if self._alugado == False:
            return("O veiculo", self._placa, "não estava alugado")
        else:
           self._alugado = False
           return ("O veiculo de placa {} foi devolvido pelo cliente {}").format(self._placa, self._cliente.getNome())


    def listarHistorico(self):
        print("\n Historico ")
        for i in self._historico:
            print(i)

        print("\n")

class Carro(Veiculo):
    def __init__(self, modelo, placa, valor):
        Veiculo.__init__(self, placa, valor)
        self._modelo = modelo

    def calcularAluguel(self, dias):

        return (dias * self._valor)      

class Moto(Veiculo):
    def __init__(self, placa, valor):
        Veiculo.__init__(self, placa, valor)

    def calcularAluguel(self, dias):
        if dias >= 30:
            return (dias * self._valor) * 1.1
        
        else:
            return (dias * self._valor) * 1.2


cliente1 = Cliente("Marco")
cliente2 = Cliente("Antonio")
carro1 = Carro("Celta", "ABC123", 100)
carro2 = Carro("Uno", "XYZ123", 80)
moto1 = Moto("MOT123", 40)
moto2 = Moto("MOT234", 50)
print(carro1.alugar(cliente1, 10))
print(carro1.alugar(cliente1, 10))
print(carro1.devolver())
print(carro1.alugar(cliente2, 15))
carro1.listarHistorico()
print(carro2.devolver())
print(moto1.alugar(cliente1, 20))
print(moto1.devolver())
print(moto1.alugar(cliente2, 30))
moto1.listarHistorico()





