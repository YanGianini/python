'''
Avaliação referente a P2 - Orientação a Objeto

Daniel Coelho Cabral - 202011112
          &
Yan Gianini - 202011128
'''
from datetime import date
from datetime import datetime

class Pessoa():
    def __init__(self, nome):
        self._nome = nome

class Funcionario(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self._dependentes = []
        self._ocorrencias = []
        self._cargo = None

    def getNome(self):
        return self._nome

    def setCargo(self, cargo):
        self._cargo = cargo

    def getSalario(self):
        return self._cargo.getSalario()

    def setOcorrencia(self, ocorrencia):
        self._ocorrencias.append(ocorrencia)

    def calcularSalarioLiquido(self, mes, ano):
        salarioLiquido = self._cargo.getSalario()

        for i in self._ocorrencias:
            if mes == i.getDataOcorrencia().month and ano == i.getDataOcorrencia().year:
                salarioLiquido += i.getValorAcrescimo()
                salarioLiquido -= i.getValorDesconto()
        
        for i in self._dependentes:
            dataNasc = datetime.strptime(i.getData(), '%d/%m/%Y')
            if (ano - dataNasc.year) > 18:
                pass
            elif (ano - dataNasc.year) < 18:
                salarioLiquido += 100
            else:
                if mes > dataNasc.month:
                    pass
                else:
                    salarioLiquido += 100
                
        return salarioLiquido


    def setDependentes(self, nome, dataNascimento):
        self._dependentes.append(Dependente(dataNascimento, nome))

    def exibirDependentes(self):
        for i in self._dependentes:
            print("\nNome:{}  Data de Nascimento:{}   Próximo aniversário:{}  Dia do próximo aniversário:{}".format(i.getNome(), i.getData(), i.getProximoAniversario(), i.getDiaSemana()))


class Dependente(Pessoa):
    def __init__(self, dataNascimento, nome):
        super().__init__(nome)
        self._dataNascimento = dataNascimento 
        self._dataAniversario = 0

    def getNome(self):
        return self._nome

    def getData(self):
        return self._dataNascimento

    def getProximoAniversario(self):
        dataNasc = datetime.strptime(self._dataNascimento, '%d/%m/%Y')
        dataAtual = datetime.strptime(str(date.today()), '%Y-%m-%d')
        dataAniversario = 0
        if (dataNasc.month > dataAtual.month):
            dataAniversario = datetime.strptime("{}/{}/{}".format(dataNasc.day, dataNasc.month, date.today().year), '%d/%m/%Y')
            self._dataAniversario = dataAniversario
            return (dataAniversario - dataAtual).days
        else:
            if (dataNasc.day >= dataAtual.day):
                dataAniversario = datetime.strptime("{}/{}/{}".format(dataNasc.day, dataNasc.month, date.today().year), '%d/%m/%Y')
                self._dataAniversario = dataAniversario
                return (dataAniversario - dataAtual).days
            else:
                dataAniversario = datetime.strptime("{}/{}/{}".format(dataNasc.day, dataNasc.month, (date.fromordinal(date.today().toordinal()+365)).year), '%d/%m/%Y')
                self._dataAniversario = dataAniversario
                return (dataAniversario - dataAtual).days

    def getDiaSemana(self):
        diaSemana = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        return (diaSemana[self._dataAniversario.weekday()])

class Cargo():
    def __init__(self, salarioBruto):
        self._salarioBruto = salarioBruto

    def getSalario(self):
        return self._salarioBruto

class Ocorrencia:
    def __init__(self, dataOcorrencia, valorAcrescimo, valorDesconto, descricaoOcorrencia):
        self._dataOcorrencia = datetime.strptime(dataOcorrencia, '%d/%m/%Y')
        self._valorAcrescimo = valorAcrescimo
        self._valorDesconto = valorDesconto
        self._descricaoOcorrencia = descricaoOcorrencia

    def getDataOcorrencia(self):
        return self._dataOcorrencia

    def getValorAcrescimo(self):
        return self._valorAcrescimo

    def getValorDesconto(self):
        return self._valorDesconto

    def getDescriçãoOcorrencia(self):
        return self._descricaoOcorrencia


#main program

funcionario1 = Funcionario("Dk")
funcionario1.setDependentes("Yan", "10/03/2001")
funcionario1.setDependentes("Daniel", "17/07/2001")
funcionario1.setDependentes('Brall', "16/12/2005")
funcionario1.setDependentes("Jesus", "25/12/2010")
funcionario1.exibirDependentes()

cargo1 = Cargo(5000)
funcionario1.setCargo(cargo1)


ocorrencia1 = Ocorrencia("10/12/2020", 10, 20, "Tropeçou")
funcionario1.setOcorrencia(ocorrencia1)
print("\nO salario Liquido foi de R${}".format(funcionario1.calcularSalarioLiquido(12, 2020)))
