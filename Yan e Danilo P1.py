#Danilo Vasconcellos     202010702  |   Yan Gianini             202011128

class Pessoa():
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

class Hospital(Pessoa):
    def __init__(self, nome, CNPJ, chefe = None):
        super().__init__(nome)
        self.CNPJ = CNPJ
        self.chefe = chefe

    def getCNPJ(self):
        return self.CNPJ

    def setCNPJ(self, CNPJ):
        self.CNPJ = CNPJ

    def getChefe(self):
        if self.chefe == None:
            return "Sem chefe"
        else:
            return self.chefe.getNome()

    def setChefe(self, chefe):
        self.chefe = chefe

    def getEspecialidadeChefe(self):
        if self.chefe.getEspecialidade() == None:
            return "Chefe sem especialidade"

        else:
            return self.chefe.getEspecialidade()     

class Cidade():
    def __init__(self, cidade, hospital = None):
        self.cidade = cidade
        self.hospital = hospital

    def getCidade(self):
        if self.cidade == None:
            return "Sem cidade"

        else:
            return self.cidade
    
    def setCidade(self, cidade):
        self.cidade = cidade

    def getHospital(self):
        if self.hospital == None:
            return "Cidade sem hospital"

        else:
            return self.hospital.getNome()

    def setHospital(self, hospital):
        self.hospital = hospital

    def getNomeChefe(self):
        if self.hospital == None:
            return "Cidade sem hospital"

        else:
            return self.hospital.getChefe()

class PessoaFisica(Pessoa):
    def __init__(self, nome, CPF):
        super().__init__(nome)
        self.CPF = CPF

    def getCPF(self):
        return self.CPF

    def setCPF(self, CPF):
        self.CPF = CPF
    
class Paciente(PessoaFisica):
    def __init__(self, nome, CPF, medicoResponsavel = None):
        super().__init__(nome, CPF)
        self.medicoResponsavel = medicoResponsavel

    def getMedicoResponsavel(self):
        if self.medicoResponsavel == None:
            return "Sem medico responsavel"

        else:
            return self.medicoResponsavel.getNome()

    def setMedicoResponsavel(self, medicoResponsavel):
        self.medicoResponsavel = medicoResponsavel

class Medico(PessoaFisica):
    def __init__(self, nome, CPF, especialidade = None, hospital = None):
        super().__init__(nome, CPF)
        self.especialidade = especialidade

    def getEspecialidade(self):
        return self.especialidade.getEspecialidade()

    def setEspecialidade(self, especialidade):
        self.especialidade = especialidade

    def getNomeHospital(self):
        return self.hospital.getNome()

    def getHospital(self):
        if self.hospital == None:
            return "Medico sem Hospital"

        else:
            return self.hospital

    def setHospital(self, hospital):
        self.hospital = hospital

class Especialidade():
    def __init__(self, especialidade):
        self.especialidade = especialidade

    def getEspecialidade(self):
        return self.especialidade

    def setEspecialidade(self, especialidade):
        self.especialidade = especialidade



#1) Qual a especialidade do médico chefe de um hospital?

hospital1 = Hospital("Lourenço Jorge", "938537000150")
chefe1 = Medico("Danilo", "13454100771")
hospital1.setChefe(chefe1)
especialidade1 = Especialidade("Cardiologista")
chefe1.setEspecialidade(especialidade1)
print("1) Qual a especialidade do médico chefe de um hospital?\n" + hospital1.getEspecialidadeChefe())


#2) Qual o nome do hospital que um médico trabalha?

medico1 = Medico("Yan", "18835404703")
hospital2 = Hospital("Gianini & Vasconcellos", "183235000153")
medico1.setHospital(hospital2)
print("\n2) Qual o nome do hospital que um médico trabalha?\n" + medico1.getNomeHospital())

#3) Qual o nome do médico que atende um paciente?

paciente1 = Paciente("Marco", "22233344455")
paciente1.setMedicoResponsavel(medico1)
print("\n3) Qual o nome do médico que atende um paciente?\n" + paciente1.getMedicoResponsavel())

#4) Qual o CPF de um paciente?

print("\n4) Qual o CPF de um paciente?\n" + paciente1.getCPF())

#5) Qual o CNPJ de um hospital?

print("\n5) Qual o CNPJ de um hospital?\n" + hospital1.getCNPJ())

#6) IMPORTANTE: cada aluno/dupla deve acrescentar uma nova classe e responder a alguma pergunta que relacione essa classe a uma outra existente no modelo
#nova classe : Cidade
#nova pergunta: Qual o nome do chefe do hospital de uma cidade 
chefe2 = Medico("Antonio", "77788899900")
hospital3 = Hospital("Albert Einstein", "187236000150")
hospital3.setChefe(chefe2)
cidade1 = Cidade("Barra do piraí")
cidade1.setHospital(hospital3)
print("\n6) Qual o nome do chefe do hospital de uma cidade?\n " + cidade1.getNomeChefe())
