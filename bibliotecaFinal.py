#Yan 202011128 & Danilo 202010702

import copy
from datetime import date
from datetime import datetime

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

class Bibliotecario(Pessoa):
    def __init__(self, nome, idFuncionario):
        Pessoa.__init__(self, nome)
        self.idFuncionario = idFuncionario

    def getIdFuncionario(self):
        return self.idFuncionario

    def setIdFuncionario(self, idFuncionario):
        self.idFuncionario = idFuncionario

    def getNome(self):
        return self.nome


class Cliente(Pessoa):
    def __init__(self, nome, registro):
        Pessoa.__init__(self, nome)
        self.registro = registro
        self.historicoAluguel = []


class Aluno(Pessoa):
    def __init__(self, nome, registro, matricula):
        Cliente.__init__(self, nome, registro)       
        self.matricula = matricula


class Professor(Pessoa):
    def __init__(self, nome, registro, escolaridade):
        Cliente.__init__(self, nome, registro)
        self.escolaridade = escolaridade


class Aluguel:
    def __init__(self, cliente, bibliotecario, exemplar):
        self.cliente = cliente
        self.bibliotecario = bibliotecario
        self.exemplar = exemplar
        self.dataAluguel = copy.deepcopy(date.today())
        self.dataRetorno = date.fromordinal(self.dataAluguel.toordinal()+7)

    def getDataAluguel(self):
        return self.dataAluguel

    def setDataAluguel(self, data):
        self.dataAluguel = data

    def getDataRetorno(self):
        return self.dataRetorno

    def calculoMulta(self):
        
        dataAtual = date.fromordinal(date.today().toordinal())
        dataAluguel = date.fromordinal(self.dataAluguel.toordinal())
        if (dataAtual - dataAluguel).days > 7:
            multa = ((dataAtual - dataAluguel).days-7)*5
        else:
            multa = 0
        return multa

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False
        self.historico = []
        self.autor = None
        self.genero = None
        self.exemplar = []

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor.getAutor()

    def setAutor(self, autor):
        self.autor = autor

    def getGenero(self):
        return self.genero.getGenero()

    def setGenero(self, genero):
        self. genero = genero

    def listarHistorico(self):
        print("\nHistórico")
        for i in self.historico:
            print(i)
        print('\n')

    def listarExemplar(self):
        for i in self.exemplar:
            print(i.getExemplar())

    def setExemplar(self, exemplar):
        self.exemplar.append(exemplar)

    def getQuantidade(self):
        return len(self.exemplar)
    
    def Alugar(self, exemplar, cliente, bibliotecario):
        if exemplar.estaEmprestado() == False:
            exemplar.Alugar(cliente, bibliotecario)
            self.historico.append("Livro:{}   Exemplar:{}   Cliente:{}   Bibliotecario:{}   Data Aluguel: {}".format(self.getTitulo(), exemplar.getExemplar(), cliente.getNome(), bibliotecario.getIdFuncionario(), exemplar.getDataAluguel()))
            return True
        return False
    
    def Devolver(self, exemplar):
        if exemplar.estaEmprestado() == True:
            if exemplar.calculoMulta() > 0:
                self.historico.append("{} foi devolvido em {} com uma multa de R${}".format(exemplar.getExemplar(), date.today(), exemplar.calculoMulta()))
            else:
                self.historico.append("{} foi devolvido em {} ".format(exemplar.getExemplar(), date.today()))
            exemplar.Devolver()
            return True
        return False
        

class Exemplar:
    def __init__(self, exemplar):
        self.exemplar = exemplar
        self.emprestado = False

    def getExemplar(self):
        return self.exemplar

    def setExemplar(self, exemplar):
        self.exemplar = exemplar

    def estaEmprestado(self):
        return self.emprestado

    def setEmprestado(self, emprestado):
        self.emprestado = emprestado

    def getDataAluguel(self):
        return self.aluguel.getDataAluguel()

    def getDataRetorno(self):
        return self.aluguel.getDataRetorno()

    def Alugar(self, cliente, bibliotecario):
        self.aluguel = Aluguel(cliente, bibliotecario, self)
        self.setEmprestado(True)
        return True

    def Devolver(self):
        self.aluguel = None
        self.setEmprestado(False)
        return True

    def calculoMulta(self):
        return self.aluguel.calculoMulta()

class Autor:
    def __init__(self, nome):
        self.nome = nome
    def getAutor(self):
        return self.nome

    def setAutor(self, autor):
        self.nome = autor

class Genero:
    def __init__(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero




livro1 = Livro("JOJO")
#print(livro1.getTitulo())
autor1 = Autor("Hirohiko Araki")
livro1.setAutor(autor1)
#print(livro1.getAutor())
genero1 = Genero("Mangaka")
livro1.setGenero(genero1)
#print(livro1.getGenero())
exemplar1 = Exemplar("23303")
livro1.setExemplar(exemplar1)
exemplar2 = Exemplar("23304")
livro1.setExemplar(exemplar2)
#livro1.listarExemplar()



#print("Possui {} Exemplares".format(livro1.getQuantidade()))

cliente1 = Cliente("Yan","20201112983")
bibliotecario1 = Bibliotecario("jefinho", "991119290")
print(livro1.Alugar(exemplar1, cliente1, bibliotecario1))
exemplar1.aluguel.setDataAluguel(datetime.strptime("2020-12-01", "%Y-%m-%d"))
print(livro1.Alugar(exemplar1,cliente1, bibliotecario1 ))
print(livro1.Devolver(exemplar1))
print(livro1.Alugar(exemplar1,cliente1, bibliotecario1 ))
print(livro1.Devolver(exemplar1))
livro1.listarHistorico()


