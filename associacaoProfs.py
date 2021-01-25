
class Pessoa():
    def __init__(self, nome, escolaridade = None, cidade = None):
        self.nome = nome
        self.escolaridade = escolaridade
        self.cidade = cidade

    def getEscolaridade(self):
        if self.escolaridade == None:
            return "nenhuma escolaridade"
        else:
            return self.escolaridade.getEscolaridade()
    
    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getEstado(self):
        if self.cidade == None:
            return "nenhuma estado"
        else:
            return self.cidade.getEstado()

    def getCidade(self):
        if self.cidade == None:
            return "nenhuma cidade"
        else:
            return self.cidade.getCidade()

    def setCidade(self, cidade):
        self.cidade = cidade

    def getNome(self):
        return self.nome

class Professor(Pessoa):
    def __init__(self, nome, escolaridade = None, cidade = None, contrato = None):
        super().__init__(nome, escolaridade, cidade)
        self.contrato = contrato

    def getTipoEnsino(self):
        if self.contrato == None:
            return "nenhum tipo"
        else:
            return self.contrato.getTipo()
    
    def getContrato(self):
        if contrato == None:
            return "nenhum contrato"
        else:
            return self.contrato

    def setContrato(self, contrato):
        self.contrato = contrato

    def getDiretor(self):
        if self.contrato == None:
            return "Sem diretor"
        else:
            return self.contrato.getDiretor()

    def getCoordenador(self):
        if self.contrato == None:
            return "Sem coordenador"
        else:
            return self.contrato.getCoordenador()

class Aluno(Pessoa):
    def __init__(self, nome, escolaridade = None, cidade = None, curso = None):
        super().__init__(nome, escolaridade, cidade)
        self.curso = curso

    def getEstadoCurso(self):
        if self.curso == None:
            return "Nenhum curso"
        else:
            return self.curso.getEstado()

    def setCurso(self, curso):
        self.curso = curso

    def getCoordenador(self):
        if self.curso == None:
            return "Nenhum curso"
        else:
            return self.curso.getCoordenador()
    

class Escolaridade():
    def __init__(self, escolaridade):
        self.escolaridade = escolaridade

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getEscolaridade(self):
        return self.escolaridade

class Curso():
    def __init__(self, curso, coordenacao = None, escola = None, tipoEnsino = None):
        self.curso = curso
        self.coordenacao = coordenacao
        self.escola = escola
        self.tipoEnsino = tipoEnsino


    def getCurso(self):
        return self.curso

    def getEscolaridade(self):
        if self.coordenacao == None:
            return ("\nCoordenacao está vazia.")
        return self.coordenacao.getEscolaridade()

    def getEstado(self):
        if self.escola == None:
            return ("\nEscola está vazia.")
        return self.escola.getEstado()

    def getDiretor(self):
        if self.escola == None:
            return ("\nEscola está vazia.")
        return self.escola.getDiretor()

    def getTipo(self):
        if self.tipoEnsino == None:
            return ("\nCoordenacao está vazia.")
        return self.tipoEnsino.getTipo()

    def getCoordenador(self):
        if self.coordenacao == None:
            return ("\nCoordenacao está vazia.")
        return self.coordenacao.getNome()

    def setCurso(self, curso):
        self.curso = curso

    def setCoordenador(self, coordenacao):
        self.coordenacao = coordenacao

    def setEscola(self, escola):
        self.escola = escola

    def setTipo(self, tipoEnsino):
        self.tipoEnsino = tipoEnsino


class TipoEnsino():
    def __init__(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo


class Escola():
    def __init__(self, escola, diretor, cidade = None):
        self.escola = escola
        self.diretor = diretor
        self.cidade = cidade

    def getEscola(self):
        return self.escola

    def setEscola(self):
        self.escola = escola

    def getEscolaridade(self):
        if self.diretor == None:
            return "nenhum diretor"
        else:
            return self.diretor.getEscolaridade() 

    def getDiretor(self):
        return self.diretor.getNome()

    def setDiretor(self):
        self.diretor = diretor

    def getEstado(self):
        if self.cidade == None:
            return "Não possui cidade"
        else:
            return self.cidade.getEstado()

    def setCidade(self, cidade):
        self.cidade = cidade

class Cidade():
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def getCidade(self):
        return self.cidade

    def setCidade(self, cidade):
        self.cidade = cidade

    def getEstado(self):
        if self.estado == None:
            return "não há estado"
        else:
            return self.estado.getEstado()

    def setEstado(self, estado):
        self.estado = estado

class Estado():
    def __init__(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setEstado(self):
        self.estado = estado


escolaridade1 = Escolaridade("Doutor")
professor1 = Professor("Marco", escolaridade1)
print("A)" + professor1.getEscolaridade())


escolaridade2 = Escolaridade("Mestre")
coordenador1 = Professor("Tassio", escolaridade2)
curso1 = Curso("ESW", coordenador1)
print("B)" + curso1.getEscolaridade())


escolaridade3 = Escolaridade("Bacharel")
diretor1 = Professor("Maria", escolaridade3)
escola1 = Escola("USS", diretor1)
print("C)" + escola1.getEscolaridade())


estado1 = Estado("RJ")
aluno1 = Aluno("Yan")
cidade1 = Cidade("BP", estado1)
aluno1.setCidade(cidade1)
print("D)" + aluno1.getEstado())


estado2 = Estado("MG")
cidade2 = Cidade("JF", estado2)
professor1.setCidade(cidade2)
print("E)" + professor1.getCidade())

estado3 = Estado("SC")
cidade3 = Cidade("Florianopolis", estado3)
escola2 = Escola("UFSC", professor1)
escola2.setCidade(cidade3)
curso1.setEscola(escola2)
aluno2 = Aluno("DK")
aluno2.setCurso(curso1)
print("F)" + aluno2.getEstadoCurso())


tipo1 = TipoEnsino("superior")
curso1.setTipo(tipo1)
professor1.setContrato(curso1)

print("G)" + professor1.getTipoEnsino())


curso1.setCoordenador(coordenador1)
aluno1.setCurso(curso1)
print("H)" + aluno1.getCoordenador())


print("I)" + professor1.getDiretor())

'''
a) Qual a escolaridade de um professor?
b) Qual a escolaridade do coordenador de um curso?
c) Qual a escolaridade do diretor de uma escola?
d) Qual o estado de naturalidade de um aluno?
e) Qual a cidade de nascimento de um professor?
f) Qual o estado em que um aluno estuda?
g) Qual o tipo de ensino (ensino fundamental, médio, superior) que um professor foi contratado para lecionar?
h) Quem é o coordenador do curso de um aluno?
i) Quem é o diretor de um professor?
j) Quem é o coordenador de um professor?
'''